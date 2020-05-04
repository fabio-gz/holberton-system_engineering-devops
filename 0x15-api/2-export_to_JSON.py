#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests
import sys

if __name__ == '__main__':
    todos = requests.get('http://jsonplaceholder.typicode.com/todos',
                         params={'userId': sys.argv[1]})
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(sys.argv[1]))

    with open(sys.argv[1] + '.json', mode='w') as f:
        lis = []
        for i in todos.json():
            dic = {}
            dic['task'] = i.get('title')
            dic['completed'] = i.get('completed')
            dic['username'] = users.json().get('username')
            lis.append(dic)
            stru = {sys.argv[1]: lis}

        json.dump(stru, f)
