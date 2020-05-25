title: flask.helpers make_response Python code examples
category: page
slug: flask-helpers-make-response-examples
sortorder: 500021000
toc: False
sidebartitle: flask.helpers make_response
meta: Python example code for the make_response function from the flask.helpers module of the Flask project.


make_response is a function within the flask.helpers module of the Flask project.


## Example 1 from newspie
[NewsPie](https://github.com/skamieniarz/newspie) is a minimalistic news
aggregator created with [Flask](/flask.html) and the
[News API](https://newsapi.org/).

NewsPie is provided as open source under the
[MIT license](https://github.com/skamieniarz/newspie/blob/master/LICENSE).

[**newspie / news.py**](https://github.com/skamieniarz/newspie/blob/master/././news.py)

```python
# -*- coding: utf-8 -*-
'''
NewsPie - a minimalistic news aggregator built with Flask and powered by
News API (https://newsapi.org/).

Created by @skamieniarz (https://github.com/skamieniarz) in 2019.
'''
import configparser
import json
import logging
import os

import requests
import requests_cache
from dateutil import parser
~~from flask import (Flask, make_response, redirect, render_template, request,
                   url_for)

CONFIG = configparser.ConfigParser()
CONFIG.read('config.ini')
API_KEY = os.environ.get('NEWS_API_KEY')
TOP_HEADLINES = CONFIG['ENDPOINTS']['TOP_HEADLINES']
EVERYTHING = CONFIG['ENDPOINTS']['EVERYTHING']
PAGE_SIZE = int(CONFIG['VARIOUS']['PAGE_SIZE'])

CATEGORIES = ('general', 'sports', 'business', 'entertainment', 'health',
              'science', 'technology')
with open('data/countries.json') as json_file:
    COUNTRIES = json.load(json_file)

logging.basicConfig(level=logging.DEBUG)
requests_cache.install_cache(cache_name='news_cache',
                             backend='sqlite',
                             expire_after=300)

APP = Flask(__name__)


@APP.route('/', methods=['GET', 'POST'])
def root():


## ... source file abbreviated to get to make_response examples ...


    if page > pages:
        page = pages
        return redirect(url_for('search', query=query, page=page))
    articles = parse_articles(response.json())
    return render(articles,
                  page,
                  pages,
                  country=get_cookie('country'),
                  category='search')


def do_post(page, category='general', current_query=None):
    ''' Helper method that handles POST request basing on the input. '''
    new_query = request.form.get('search_query')
    country = request.form.get('country')
    next_page = request.form.get('next_page')
    previous_page = request.form.get('previous_page')
    if new_query is not None and new_query != '':
        return redirect(url_for('search', query=new_query, page=1))
    if country is not None and country != get_cookie('country'):
~~        response = make_response(
            redirect(url_for('category', category=category, page=1)))
        response.set_cookie('country', country)
        return response
    if next_page is not None:
        page = int(next_page) + 1
    elif previous_page is not None:
        page = int(previous_page) - 1
    if category == 'search':
        return redirect(url_for('search', query=current_query, page=page))
    return redirect(url_for('category', category=category, page=page))


def parse_articles(response):
    ''' Parses articles fetched from News API.

    Returns:
        A list of dicts containing publishing date, title, URL and source of
        articles.
    '''
    parsed_articles = []
    if response.get('status') == 'ok':
        for article in response.get('articles'):
            parsed_articles.append({
                'published_at':


## ... source file continues with no further make_response examples...


```


## Example 2 from sandman2
[sandman2](https://github.com/jeffknupp/sandman2)
([project documentation](https://sandman2.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/sandman2/))
is a code library for automatically generating
[RESTful APIs](/application-programming-interfaces.html) from
existing database schemas. This approach is handy for solving
straightforward situations where you want to put an abstraction
layer between one or more applications and your
[relational database](/databases.html) to prevent or reduce
direct database access.

The sandman2 project is provided under the
[Apache License 2.0](https://github.com/jeffknupp/sandman2/blob/master/LICENSE).

[**sandman2 / sandman2 / service.py**](https://github.com/jeffknupp/sandman2/blob/master/sandman2/./service.py)

```python
"""Automatically generated REST API services from SQLAlchemy
ORM models or a database introspection."""

# Third-party imports
~~from flask import request, make_response
import flask
from flask.views import MethodView
from sqlalchemy import asc, desc

# Application imports
from sandman2.exception import NotFoundException, BadRequestException
from sandman2.model import db
from sandman2.decorators import etag, validate_fields


def add_link_headers(response, links):
    """Return *response* with the proper link headers set, based on the contents
    of *links*.

    :param response: :class:`flask.Response` response object for links to be
                     added
    :param dict links: Dictionary of links to be added
    :rtype :class:`flask.Response` :
    """
    link_string = '<{}>; rel=self'.format(links['self'])
    for link in links.values():
        link_string += ', <{}>; rel=related'.format(link)
    response.headers['Link'] = link_string
    return response


## ... source file abbreviated to get to make_response examples ...


                    filters.append(getattr(self.__model__, key) == value)
                else:
                    raise BadRequestException('Invalid field [{}]'.format(key))
            queryset = queryset.filter(*filters).order_by(*order)
        if 'page' in request.args:
            resources = queryset.paginate(page=int(request.args['page']), per_page=limit).items
        else:
            queryset = queryset.limit(limit)
            resources = queryset.all()
        return [r.to_dict() for r in resources]

    def _export(self, collection):
        """Return a CSV of the resources in *collection*.

        :param list collection: A list of resources represented by dicts
        """
        fieldnames = collection[0].keys()
        faux_csv = ','.join(fieldnames) + '\r\n'
        for resource in collection:
            faux_csv += ','.join((str(x) for x in resource.values())) + '\r\n'
~~        response = make_response(faux_csv)
        response.mimetype = 'text/csv'
        return response


    @staticmethod
    def _no_content_response():
        """Return an HTTP 204 "No Content" response.

        :returns: HTTP Response
        """
~~        response = make_response()
        response.status_code = 204
        return response

    @staticmethod
    def _created_response(resource):
        """Return an HTTP 201 "Created" response.

        :returns: HTTP Response
        """
        response = jsonify(resource)
        response.status_code = 201
        return response


## ... source file abbreviated to get to make_response examples ...




## ... source file continues with no further make_response examples...


```

