import requests

def get_site(url):
    """Get Response object"""
    return requests.get(url)
