#!/usr/bin/env python
import os
from argparse import ArgumentParser
from concurrent import futures
from collections import defaultdict
from functools import partial
from json import dumps
from multiprocessing import cpu_count
from sys import argv
from uuid import uuid4

import requests
import urllib3
from bs4 import BeautifulSoup
from markdown import markdown


# Ignore security hazard since certs SHOULD be trusted (https)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Avoid rate limiting (tcp)
URL_BOT_ID = f'Bot {str(uuid4())}'


def extract_urls_from_html(content):
    soup = BeautifulSoup(content, 'html.parser')
    html_urls = set()
    for a in soup.find_all('a', href=True):
        url = a['href']
        if url.startswith('http'):
            html_urls.add(url)
    return html_urls


def extract_urls(discover_path):
    exclude = ['.git', '.vscode']
    all_urls = defaultdict(list)
    max_strlen = -1
    for root, dirs, files in os.walk(discover_path, topdown=True):
        dirs[:] = [d for d in dirs if d not in exclude]
        short_root = root.replace(discover_path, '')
        for file in files:
            output = f'Currently checking: file={file}'
            file_path = os.path.join(root, file)
            if max_strlen < len(output):
                max_strlen = len(output)
            print(output.ljust(max_strlen), end='\r')
            if file_path.endswith('.html'):
                content = open(file_path)
                extract_urls_from_html(content)
            elif file_path.endswith('.markdown'):
                content = markdown(open(file_path).read())
            else:
                continue
            html_urls = extract_urls_from_html(content)
            for url in html_urls:
                all_urls[url].append(os.path.join(short_root, file))
    return all_urls


def run_workers(work, data, threads, **kwargs):
    work_partial = partial(work, **kwargs)
    with futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_result = {
            executor.submit(work_partial, arg): arg
            for arg in data
        }
        for future in futures.as_completed(future_to_result):
            yield future.result()


def get_url_status(url, timeout, retries):
    for local in ('localhost', '127.0.0.1', 'app_server'):
        if url.startswith('http://' + local):
            return (url, 0)
    clean_url = url.strip('?.')
    try:
        with requests.Session() as session:
            adapter = requests.adapters.HTTPAdapter(max_retries=retries)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            response = session.get(
                clean_url, verify=False, timeout=timeout,
                headers={'User-Agent': URL_BOT_ID})
            return (clean_url, response.status_code)
    except requests.exceptions.Timeout:
        return (clean_url, 504)
    except requests.exceptions.TooManyRedirects:
        return (clean_url, -301)
    except requests.exceptions.ConnectionError:
        return (clean_url, -1)


def bad_url(url_status):
    if url_status == -301 or url_status == -1:
        return True
    elif url_status == 401 or url_status == 403:
        return False
    elif url_status == 503:
        return False
    elif url_status >= 400:
        return True
    return False


def parse_args(argv):
    parser = ArgumentParser(
        description='Check for bad urls in the HTML content.',
        add_help=True)
    parser.add_argument(
        '-timeout', '--url-timeout',
        default=10.0,
        type=float,
        dest='timeout',
        help='Timeout in seconds to wait for url')
    parser.add_argument(
        '-retries', '--url-retries',
        default=5,
        type=int,
        dest='retries',
        help='Number of url retries')
    parser.add_argument(
        '-threads', '--num-threads',
        default=cpu_count()*4,
        type=int,
        dest='threads',
        help='Number of threads to run with')
    return parser.parse_args(argv)


def main():
    args = parse_args(argv[1:])
    print('Extract urls...')
    all_urls = extract_urls(os.getcwd())
    print('\nCheck urls...')
    bad_url_status = {}
    url_id = 1
    max_strlen = -1
    for url_path, url_status in run_workers(
            get_url_status, all_urls.keys(),
            threads=args.threads, timeout=args.timeout, retries=args.retries):
        output = (
            f'Currently checking: id={url_id} '
            f'host={urllib3.util.parse_url(url_path).host}'
        )
        if max_strlen < len(output):
            max_strlen = len(output)
        print(output.ljust(max_strlen), end='\r')
        if bad_url(url_status) is True:
            bad_url_status[url_path] = url_status
        url_id += 1
    bad_url_location = {
        bad_url: all_urls[bad_url]
        for bad_url in bad_url_status
    }
    status_content = dumps(bad_url_status, indent=4)
    location_content = dumps(bad_url_location, indent=4)
    print(f'\nBad url status: {status_content}')
    print(f'\nBad url locations: {location_content}')


if __name__ == '__main__':
    main()
