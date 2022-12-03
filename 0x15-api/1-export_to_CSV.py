#!/usr/bin/python3
""" REST API """

import csv
import sys

import requests

if __name__ == "__main__":

    ID = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(ID)
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(ID)

    username = requests.get(url=user_url).json()["username"]

    responses = requests.get(url=todos_url).json()

    with open(f"{ID}.csv", "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for response in responses:
            writer.writerow(
                [int(ID), username, response["completed"], response["title"]]
            )
