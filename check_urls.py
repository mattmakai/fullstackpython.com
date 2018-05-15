#!/usr/bin/env python
from concurrent import futures
import multiprocessing as mp
import os
import json
import uuid

from bs4 import BeautifulSoup
from markdown import markdown
import requests
import urllib3


# Ignore security hazard since certs SHOULD be trusted (https)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Avoid rate limiting (tcp)
URL_BOT_ID = f'Bot {str(uuid.uuid4())}'


def extract_urls_from_html(content, all_urls):
    soup = BeautifulSoup(content, 'html.parser')
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('http'):
            all_urls.add(url)


def extract_urls(discover_path):
    exclude = ['.git', '.vscode']
    all_urls = set()
    max_strlen = -1
    for root, dirs, files in os.walk(discover_path, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude]
        for file in files:
            output = f'Currently checking: file={file}'
            file_path = os.path.join(root, file)
            if max_strlen < len(output):
                max_strlen = len(output)
            print(output.ljust(max_strlen), end='\r')
            if file_path.endswith('.html'):
                content = open(file_path)
                extract_urls_from_html(content, all_urls)
            elif file_path.endswith('.markdown'):
                content = markdown(open(file_path).read())
                extract_urls_from_html(content, all_urls)
    return all_urls


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
            clean_url, verify=False, timeout=10.0,
            headers={'User-Agent': URL_BOT_ID})
        return (clean_url, response.status_code)
    except requests.exceptions.Timeout:
        return (clean_url, 504)
    except requests.exceptions.ConnectionError:
        return (clean_url, -1)
    except requests.exceptions.TooManyRedirects:
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
    all_urls = extract_urls(os.getcwd())
    print('\nCheck urls...')
    bad_urls = {}
    url_id = 1
    max_strlen = -1
    for url_path, url_status in run_workers(get_url_status, all_urls):
        output = f'Currently checking: id={url_id} host={urllib3.util.parse_url(url_path).host}'
        if max_strlen < len(output):
            max_strlen = len(output)
        print(output.ljust(max_strlen), end='\r')
        if bad_url(url_status) is True:
            bad_urls[url_path] = url_status
        url_id += 1
    print(f'\nBad urls: {json.dumps(bad_urls, indent=4)}')


if __name__ == '__main__':
    main()
