#!/usr/bin/python3
"""export data in the JSON format"""
import json
import requests
import sys

if __name__ == '__main__':
    todos = requests.get('http://jsonplaceholder.typicode.com/todos')
    users = requests.get('https://jsonplaceholder.typicode.com/users')

    with open('todo_all_employees.json', mode='w') as f:
        stru = {}
        for i in users.json():
            u_id = i.get('id')
            lis = []
            for j in todos.json():
                dic = {}
                if j.get('userId') == u_id:
                    dic['task'] = j.get('title')
                    dic['completed'] = j.get('completed')
                    dic['username'] = i.get('username')
                    lis.append(dic)
                    stru.update({u_id: lis})

        json.dump(stru, f)
