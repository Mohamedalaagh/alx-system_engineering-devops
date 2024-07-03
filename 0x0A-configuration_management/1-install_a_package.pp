#!/usr/bin/pup
# Install an especific the version of flask (2.4.2)
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
