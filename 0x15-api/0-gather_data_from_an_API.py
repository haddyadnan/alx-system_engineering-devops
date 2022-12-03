#!/usr/bin/python3

"""
Gather Data from an API
returns information about his/her TODO list progress.
"""
import requests

import sys

if __name__ == "__main__":

    ID = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"
    user_url = url + "/users/{}".format(ID)
    todo_url = url + "/todos?userId={}".format(ID)

    name = requests.get(url=user_url).json()["name"]

    responses = requests.get(url=todo_url).json()

    done = 0
    title = []
    for response in responses:
        if response["completed"] is True:
            done += 1
            title.append(response["title"])
    n_todo = len(responses)
    print("Employee {} is done with tasks ({}/{}):".format(name, done, n_todo))
    for t in title:
        print("\t ", t)
