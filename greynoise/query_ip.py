# Query all tags associated with a given IP address
#
# GreyNoise adds scanner tags to IP addresses. This function retrieves
# all tags currently in use.
#

import requests

url = 'http://api.greynoise.io:8888/v1/query/ip'


def query_ip(ip):
    r = requests.post(url, ({'ip': ip}))
    if r.status_code == 200:
        return r.json()
    else:
        return {}
