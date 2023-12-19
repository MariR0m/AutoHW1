import pytest
from check_post import get_login, post_create
import requests
import yaml


@pytest.fixture()
def token():
    return get_login()


@pytest.fixture()
def post():
    return post_create()