import os

import requests

base_urls = open('urls.txt')

import errno
import os


for url in base_urls:
    url = url.strip().replace('http://', '').replace('https://', '')
    req_url_base = "{0}/mgWebService.asmx/GetCouncillorsByWard".format(url)

    print(req_url_base)
    try:
        req = requests.get("http://{0}".format(req_url_base))
    except:
        req = requests.get("https://{0}".format(req_url_base))
    path = os.path.join(
        os.path.abspath('.'),
        'data',
        url.replace('http://', '')\
        .replace('www.', '')\
        .replace('applications.', '')\
        .replace('democracy.', '')\
        .split('/')[0]\
        .replace('moderngov.', '')\
        .replace('ww5.', '')
    )
    out_filder = os.makedirs(path, exist_ok=True)
    out_file = open(os.path.join(path, 'CouncillorsByWard.xml'), 'wb')
    out_file.write(req.content)
