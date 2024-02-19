#!/usr/bin/python3
"""script that, using a REST API,
for a given employee ID, returns
information about his/her TODO list progress."""
import requests
import sys


if __name__ == '__main__':
    """retrieve data from an api"""
    employee_id = sys.argv[1]

    # get the user data
    usr_req = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    usr_data = usr_req.json()
    employee_name = usr_data['name']

    # get todo data
    todo_req = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    todo_data = todo_req.json()

    # calculate tasks
    total = len(todo_data)
    done = sum(1 for todo in todo_data if todo['completed'])

    print(f"Employee {employee_name} is done with tasks({done}/{total}):")

    for todo in todo_data:
        if todo['completed']:
            print(f"\t {todo['title']}")
