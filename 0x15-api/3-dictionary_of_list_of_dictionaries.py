#!/usr/bin/python3
"""
script that, using a REST API,
for a given employee ID, returns
information about his/her TODO list progress.
export data to a json file.
"""
import json
import requests


if __name__ == '__main__':
    """retrieve data from an api"""

    # get the user data
    usr_req = requests.get("https://jsonplaceholder.typicode.com/users")
    usr_data = usr_req.json()

    # get the todo data
    todo_req = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo_data = todo_req.json()

    # create a dictionary to map user IDs to usernames
    username_map = {user['id']: user['username'] for user in usr_data}
    user_tasks = {}

    for todo in todo_data:
        user_id = str(todo['userId'])  # Convert user ID to string
        task_info = {
            'username': username_map[todo['userId']],
            'task': todo['title'],
            'completed': todo['completed']
        }
        # Append task info to the list associated with the user ID
        if user_id in user_tasks:
            user_tasks[user_id].append(task_info)
        else:
            user_tasks[user_id] = [task_info]

    # write the json file
    json_file = "todo_all_employees.json"
    with open(json_file, mode='w') as f:
        json.dump(user_tasks, f)
