#!/usr/bin/python3
""" REST API """

import sys

import requests

if __name__ == "__main__":

    ID = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(ID)

    name = requests.get(url=user_url).json()["name"]

    responses = requests.get(url=todos_url).json()

    done = 0
    title = []
    for response in responses:
        if response["completed"] is True:
            done += 1
            title.append(response["title"])
    print(f"Employee {name} is done with tasks ({done}/{len(responses)}):")
    for t in title:
        print(" \t", t)
