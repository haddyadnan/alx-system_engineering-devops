#!/usr/bin/python3

"""
script to export api data in the JSON format.
"""

import json
import requests

import sys

if __name__ == "__main__":

    ID = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"
    user_url = url + "/users/{}".format(ID)
    todos_url = url + "/todos?userId={}".format(ID)

    username = requests.get(url=user_url).json()["username"]

    responses = requests.get(url=todos_url).json()

    todo_list = []
    for r in responses:
        todo_dict = {}
        todo_dict["task"] = r.get("title")
        todo_dict["completed"] = r.get("completed")
        todo_dict["username"] = username
        todo_list.append(todo_dict)

    json_dict = {}
    json_dict[ID] = todo_list

    with open(f"{ID}.json", "w") as f:
        json.dump(json_dict, f)
