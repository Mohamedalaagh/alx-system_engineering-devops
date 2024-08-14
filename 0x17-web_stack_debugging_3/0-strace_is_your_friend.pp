# Install Apache
package { 'apache2':
  ensure => installed,
}

# Install PHP
package { 'php':
  ensure => installed,
}

# Install WordPress
package { 'wordpress':
  ensure => installed,
  require => Package['apache2'], # Ensure Apache is installed before WordPress
}

# Configure Apache to serve WordPress
file { '/etc/apache2/sites-available/wordpress.conf':
  ensure  => file,
  content => "
<VirtualHost *:80>
    DocumentRoot /usr/share/wordpress
    <Directory /usr/share/wordpress>
        AllowOverride All
    </Directory>
</VirtualHost>
  ",
  require => Package['apache2'], # Ensure Apache is installed before configuration
}

# Enable the WordPress site and reload Apache
exec { 'enable_wordpress_site':
  command => '/usr/sbin/a2ensite wordpress',
  require => File['/etc/apache2/sites-available/wordpress.conf'],
}

exec { 'reload_apache':
  command => '/usr/sbin/service apache2 reload',
  require => Exec['enable_wordpress_site'],
}
