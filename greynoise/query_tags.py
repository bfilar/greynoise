# Query all IPs that have a given tag
#
# GreyNoise adds scanner tags to IP addresses. This function retrieves
# all tags currently in use.
#

import requests
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')
url = config.get('api', 'QUERY_TAGS_API')


def query_tag(tag):
    r = requests.post(url, ({'tag': tag}))
    if r.status_code == 200:
        return r.json()['records']
    else:
        return {}


def query_tags(tags):
    tags_list = []
    for tag in tags:
        r = requests.post(url, ({'tag': tag}))
        if r.status_code == 200:
            tags_list.extend(r.json()['records'])
        else:
            tags_list.extend([])

    return tags_list
