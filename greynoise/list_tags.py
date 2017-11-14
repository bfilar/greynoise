# List GreyNoise Intelligence Tags
#
# GreyNoise adds scanner tags to IP addresses. This function retrieves
# all tags currently in use.
#

import requests

url = 'http://api.greynoise.io:8888/v1/query/list'


def list_tags():
    r = requests.get(url)
    return r.json()
