#!/usr/bin/python3
"""for a given employee ID, returns information about his/her TODO list
"""
import requests
import sys

if __name__ == '__main__':
    todos = requests.get('http://jsonplaceholder.typicode.com/todos',
                         params={'userId': sys.argv[1]})
    users = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(sys.argv[1]))

    tasks = 0
    done = 0
    l_task = []

    for i in todos.json():
        tasks += 1
        if i.get('completed') is True:
            done += 1
            l_task.append(i)

    user_name = users.json().get('name')
    print('Employee {} is done with tasks({}/{}):'.
          format(user_name, done, tasks))
    for j in l_task:
        print('\t', j.get('title'))
