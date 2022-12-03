#!/usr/bin/python3
""" REST API """

import json
import sys

import requests

if __name__ == "__main__":

    ID = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(ID)

    username = requests.get(url=user_url).json()["username"]

    responses = requests.get(url=todos_url).json()

    todo_list = []
    for r in responses:
        todo_dict = {}
        todo_dict["task"] = r.get('title')
        todo_dict["completed"] = r.get('completed')
        todo_dict["username"] = username
        todo_list.append(todo_dict)

    json_dict = {}
    json_dict[ID] = todo_list

    with open(f"{ID}.json", 'w') as f:
        json.dump(json_dict, f)
