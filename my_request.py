import requests


def my_request(url):
    """
    It tries to do a get request to the URL received.
    If it fails, it raises an exception and passes.
    """
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
