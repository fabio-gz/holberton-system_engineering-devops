#!/usr/bin/python3
""" returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    about = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'MyUser'}

    try:
        data = requests.get(about, headers=headers, allow_redirects=False)
        r = data.json().get('data').get('subscribers')
        return(r)
    except:
        return 0
