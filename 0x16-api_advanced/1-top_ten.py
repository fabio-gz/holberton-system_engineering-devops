#!/usr/bin/python3
"""queries the Reddit API"""
import requests


def top_ten(subreddit):
    """ first 10 hot posts listed"""
    posts = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'user-agent': 'MyUser'}

    try:
        data = requests.get(posts, headers=headers, allow_redirects=False)
        r = data.json().get('data').get('children')
        for i in r[0:10]:
            dat = i.get('data')
            title = dat.get('title')
            print(title)
    except:
        print('None')
