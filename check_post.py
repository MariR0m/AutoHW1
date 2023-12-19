import yaml
import requests

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def get_login():
    path = data['path']
    post = requests.post(url=path, data={'username': data['username'], 'password': data['password']})
    if post.status_code == 200:
        return post.json()['token']


def get_post(token):
    path = 'https://test-stand.gb.ru/api/posts'
    get = requests.get(url=path, params={"owner": "notMe"}, headers={"X-Auth-Token": token})
    if get.status_code == 200:
        return get.json()
    

def post_create():
    obj_data = requests.post(url=data['url1'], headers={"X-Auth-Token": get_login()}, data={
        'username': data['username'],
        'password': data['password'],
        'title': 'newTitle',
        'description': 'Anything',
        'content':'Hii'})
    return obj_data.json()['description']


if __name__ == '__main__':
    token = get_login()
    post = post_create