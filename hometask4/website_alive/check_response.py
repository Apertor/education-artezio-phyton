from hometask4.website_alive import make_request


def site_check(url):
    """Site response check"""
    return make_request.get_site(url).status_code == 200
