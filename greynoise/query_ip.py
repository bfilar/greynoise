# Query all tags associated with a given IP address
#
# GreyNoise adds scanner tags to IP addresses. This function retrieves
# all tags currently in use.
#

import requests
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')
url = config.get('api', 'QUERY_IP_API')


def query_ip(ip):
    r = requests.post(url, ({'ip': ip}))
    if r.status_code == 200:
        return r.json()['records']
    else:
        return {}


def query_ips(ips):
    ips_list = []
    for ip in ips:
        r = requests.post(url, ({'ip': ip}))
        if r.status_code == 200:
            ips_list.extend(r.json()['records'])
        else:
            ips_list.extend([])

    return ips_list
