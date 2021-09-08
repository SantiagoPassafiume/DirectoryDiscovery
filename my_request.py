import requests


def my_request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
