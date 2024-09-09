import requests


def hello():
    c = requests.get('https://api.github.com/repos/insper/dev-aberto/commits')
    info = c.json()
    if 0 in info.keys():
        commit_info = info[0]['commit']['author']
    else:
        commit_info = {
            'date':'2024-09-09T13:56:09Z',
            'name':'Lionel Messi'
        }
    return commit_info['date'], commit_info['name']
