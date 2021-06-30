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
CNAME = os.getenv('GD_CNAME', 'd1q0d30a9d1374.cloudfront.net')
DOMAIN = (print(USAGE), exit()) if len(sys.argv) <= 1 else sys.argv[1]
HEADERS = {
    'Accept': 'application/json',
    'Authorization': SSO_KEY,
}


def get_dns_record(_domain):
    url = f'{GODADDY_URL}/domains/{_domain}/records/A'
    result = requests.get(url, headers=HEADERS)
    return result.json()[0]


def put_dns_record(_domain, _ip):
    url = f'{GODADDY_URL}/domains/{_domain}/records/A'
    payload = [
        {
            "name": "@",
            "data": _ip,
            "ttl": 600,
            "type": "A",
        }
    ]
    result = requests.put(url, headers=HEADERS, json=payload)

    if result.status_code == 200:
        print('Done!')
        print(result.text)
    else:
        print(f'[{result.status_code}] An error occurred.\n{result.text}')


# STARTING -------------------------------------------------------------------------------------------------------------
# VARIABLES ------------------------------------------------------------------------------------------------------------
get_ip_from_a = get_dns_record(DOMAIN)
# Filter IPv4 from CNAME
get_ip_from_cname = list(set([cname[4][0] for cname in socket.getaddrinfo('www.' + DOMAIN, 0, family=socket.AF_INET)]))

# RESULT ---------------------------------------------------------------------------------------------------------------
print(f'Record type A on GoDaddy:\n{get_ip_from_a}\n')
print(f'IPv4 from CNAME: {CNAME}\n{get_ip_from_cname}\n')


if get_ip_from_a['data'] in get_ip_from_cname:
    print('Done! Was found!')
    exit(0)


# ACTION ---------------------------------------------------------------------------------------------------------------
# If there is an IP difference between CNAME and A, update type A with the CNAME IP.
print("Update required!")
confirm = input('Do you want? [Y/N] : ')
if confirm.lower() in ['y', 'yes']:
    put_dns_record(DOMAIN, get_ip_from_cname[0])
