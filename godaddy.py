import os
import sys
import requests
import socket

# Motivation: I found a problem with GoDaddy:
# they don't work with ANAME / ALIAS and I needed to resolve my website without using 'www'.
# Therefore I thought about doing this script as a workaround.
# What did I do? I get the IP address of type CNAME 'www' and make sure it is the same as type A.

GODADDY_API_BASE_URL = 'https://api.godaddy.com/'
GODADDY_API_VERSION = 'v1'
GODADDY_URL = f'{GODADDY_API_BASE_URL}{GODADDY_API_VERSION}'


GODADDY_KEY = os.getenv('GD_KEY', '').strip("/'")
GODADDY_SECRET = os.getenv('GD_SECRET', '').strip("/'")
SSO_KEY = f"sso-key {GODADDY_KEY}:{GODADDY_SECRET}"

USAGE = f"Usage: python {sys.argv[0]} <domain>"
DOMAIN = (print(USAGE), exit()) if len(sys.argv) <= 1 else sys.argv[1]


def get_dns_record(_domain):
    url = f'{GODADDY_URL}/domains/{_domain}/records/A'
    headers = {
        'Accept': 'application/json',
        'Authorization': SSO_KEY,
    }
    result = requests.get(url, headers=headers)
    return result.text


get_ip_from_a = get_dns_record(DOMAIN)
get_ip_from_cname = socket.getaddrinfo('www.' + DOMAIN, 0)

print(get_ip_from_a)
print(get_ip_from_cname)

# TO DO: If there is an IP difference between CNAME and A, update type A with the CNAME IP.
