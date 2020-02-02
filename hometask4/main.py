from hometask4.website_alive.check_response import site_check

ENTERED_URL = input("Enter url: ")
if site_check(ENTERED_URL):
    print("Site available")
else:
    print("Site is not responding")
