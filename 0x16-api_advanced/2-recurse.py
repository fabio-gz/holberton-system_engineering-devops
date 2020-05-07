#!/usr/bin/python3
"""recursive function"""
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ list containing the titles of all hot articles"""
    posts = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {'user-agent': 'MyUser'}
    payload = {'after': after}

    try:
        data = requests.get(posts, headers=headers, params=payload,
                            allow_redirects=False)
        r = data.json().get('data').get('children')

        for i in r:
            dat = i.get('data')
            title = dat.get('title')
            hot_list.append(title)

            after = data.json().get('data').get('after')
    except:
        return None

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)
