#!/usr/bin/python3
"""
script that, using a REST API,
for a given employee ID, returns
information about his/her TODO list progress.
export data to a json file.
"""
import json
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

    # create a employee task list
    employee_tasks = []
    for todo in todo_data:
        if todo['userId'] == int(employee_id):
            task_info = {
                'task': todo['title'],
                'completed': todo['completed'],
                'username': usr_data['username'],
            }
            employee_tasks.append(task_info)

    # write the json file
    json_file = f"{employee_id}.json"
    with open(json_file, mode='w') as f:
        json.dump({employee_id: employee_tasks}, f)
