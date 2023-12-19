import pytest
from check_post import get_post, post_create

id_check = 93251


def test_1(token):
    output = get_post(token)['data']
    res = []
    for item in output:
        res.append(item['id'])
    assert id_check in res


def test_2(post):
    assert 'Anything' in post_create()