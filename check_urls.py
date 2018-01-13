#!/usr/bin/env python
from concurrent import futures
import multiprocessing as mp
import os
import uuid

import requests
import urllib3


# Ignore security hazard since certs SHOULD be trusted (https)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Avoid rate limiting (tcp)
_URL_BOT_ID = 'Bot {id}'.format(id=str(uuid.uuid4()))
URL_HEADERS = {'User-Agent': _URL_BOT_ID}
URL_TIMEOUT = 10.0

# Sources of data (file)
IN_PATH = os.path.join(os.getcwd(), 'urlin.txt')
OUT_PATH = os.path.join(os.getcwd(), 'urlout.txt')

# Collect repository URLs (bash)
_URL_RE = 'https?:\/\/[=a-zA-Z0-9\_\/\?\&\.\-]+'  # proto://host+path+params
_FIND_URLS = "find . -type f | xargs grep -hEo '{regex}'".format(regex=_URL_RE)
_FILTER_URLS = "sed '/Binary/d' | sort | uniq > {urlin}".format(urlin=IN_PATH)
COMMAND = '{find} | {filter}'.format(find=_FIND_URLS, filter=_FILTER_URLS)


def run_workers(work, data, worker_threads=mp.cpu_count()*4):
    with futures.ThreadPoolExecutor(max_workers=worker_threads) as executor:
        future_to_result = {
            executor.submit(work, arg): arg for arg in data}
        for future in futures.as_completed(future_to_result):
            yield future.result()


def get_url_status(url):
    for local in ('localhost', '127.0.0.1', 'app_server'):
        if url.startswith('http://' + local):
            return (url, 0)
    clean_url = url.strip('?.')
    try:
        response = requests.get(
            clean_url, verify=False, timeout=URL_TIMEOUT,
            headers=URL_HEADERS)
        return (clean_url, response.status_code)
    except requests.exceptions.Timeout:
        return (clean_url, 504)
    except requests.exceptions.ConnectionError:
        return (clean_url, -1)


def bad_url(url_status):
    if url_status == -1:
        return True
    elif url_status == 401 or url_status == 403:
        return False
    elif url_status == 503:
        return False
    elif url_status >= 400:
        return True
    return False


def main():
    print('Extract urls...')
    os.system(COMMAND)
    with open(IN_PATH, 'r') as fr:
        urls = map(lambda l: l.strip('\n'), fr.readlines())
    with open(OUT_PATH, 'w') as fw:
        url_id = 1
        max_strlen = -1
        for url_path, url_status in run_workers(get_url_status, urls):
            output = 'Currently checking: id={uid} host={uhost}'.format(
                uid=url_id, uhost=urllib3.util.parse_url(url_path).host)
            if max_strlen < len(output):
                max_strlen = len(output)
            print(output.ljust(max_strlen), end='\r')
            if bad_url(url_status) is True:
                fw.write('{}: {}\n'.format(url_path, url_status))
            url_id += 1
    print('\nDone.')


if __name__ == '__main__':
    main()
