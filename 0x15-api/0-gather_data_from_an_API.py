#!/usr/bin/python3
"""
Accessing a REST API for todo lists of employees.
This script fetches and displays the todo list progress for a given employee.
"""

import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/users"
    url = f"{base_url}/{employee_id}"

    # Fetch employee details
    response = requests.get(url)
    employee_name = response.json().get('name')

    # Fetch todo list for the employee
    todo_url = f"{url}/todos"
    response = requests.get(todo_url)
    t = response.json()

    done = 0
    done_tasks = []

    # Collect completed tasks
    for task in t:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    # Display the results
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(t)))
    
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
