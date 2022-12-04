#!/usr/bin/python3

"""
script to export api data in the JSON format.
dict of list of dicts
"""

import json

import requests

if __name__ == "__main__":

    user_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos/"

    todos = requests.get(url=todos_url).json()

    dict_of_list = {}
    for i in range(len(todos)):
        todo_list = []
        username = requests.get(user_url + str(todos[i].get("userId"))).json()[
            "username"
        ]

        for r in todos:
            if todos[i].get("userId") == r.get("userId"):
                todo_dict = {}
                todo_dict["username"] = username
                todo_dict["task"] = r.get("title")
                todo_dict["completed"] = r.get("completed")
                todo_list.append(todo_dict)

        dict_of_list[todos[i].get("userId")] = todo_list

    with open("todo_all_employees.json", "w") as f:
        json.dump(dict_of_list, f)
