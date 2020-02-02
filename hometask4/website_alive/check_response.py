# from hometask4.website_alive.make_request import get_site
from hometask4.website_alive import make_request


def site_check(url):
    """Site response check"""
    return make_request.get_site(url).status_code == 200

ENTERED_URL = input("Enter url: ")
print(site_check(ENTERED_URL))
