#!/usr/bin/python3

"""
script to export api data in the CSV format.
"""

import csv

import requests

import sys

if __name__ == "__main__":

    ID = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com"
    user_url = url + "/users/{}".format(ID)
    todos_url = url + "/todos?userId={}".format(ID)

    username = requests.get(url=user_url).json()["username"]

    responses = requests.get(url=todos_url).json()

    with open(f"{ID}.csv", "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for response in responses:
            writer.writerow(
                [int(ID), username, response["completed"], response["title"]]
            )
