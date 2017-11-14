# Query all IPs that have a given tag
#
# GreyNoise adds scanner tags to IP addresses. This function retrieves
# all tags currently in use.
#

import requests

url = 'http://api.greynoise.io:8888/v1/query/tag'


def query_tags(tag):
    r = requests.post(url, ({'tag': tag}))
    if r.status_code == 200:
        return r.json()
    else:
        return {}
