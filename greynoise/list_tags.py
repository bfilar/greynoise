# List GreyNoise Intelligence Tags
#
# GreyNoise adds scanner tags to IP addresses. This function retrieves
# all tags currently in use.
#

import requests
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')
url = config.get('api', 'LIST_TAGS_API')


def list_tags():
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()['tags']
    else:
        return {}
