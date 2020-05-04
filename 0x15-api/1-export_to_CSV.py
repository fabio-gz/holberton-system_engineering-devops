#!/usr/bin/python3
"""export data in the CSV format"""
import csv
import requests
import sys

if __name__ == '__main__':
    todos = requests.get('http://jsonplaceholder.typicode.com/todos',
                         params={'userId': sys.argv[1]})
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(sys.argv[1]))

    user_name = users.json().get('username')

    with open(sys.argv[1] + '.csv', mode='w') as f:
        e_writer = csv.writer(f, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_ALL)
        for i in todos.json():
            e_writer.writerow([sys.argv[1], user_name, i.get('completed'),
                               i.get('title')])
