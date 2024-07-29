#!/usr/bin/python3
"""
Script to access a REST API for todo lists of employees.
Fetches and displays the todo list progress for a given employee.
"""

import requests
import sys

if __name__ == '__main__':
    # Get the employee ID from command-line arguments
    employee_id = sys.argv[1]

    # Base URL for accessing user information
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{employee_id}"

    # Fetch employee details
    response = requests.get(user_url)
    employee_name = response.json().get('name')

    # Fetch todo list for the employee
    todo_url = f"{user_url}/todos"
    response = requests.get(todo_url)
    tasks = response.json()

    # Variables to track completed tasks
    completed_tasks = []
    num_completed = 0

    # Collect completed tasks
    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            num_completed += 1

    # Display the results
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_completed, len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
