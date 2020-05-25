title: flask.globals request Python code examples
category: page
slug: flask-globals-request-examples
sortorder: 500021000
toc: False
sidebartitle: flask.globals request
meta: Python example code for the request function from the flask.globals module of the Flask project.


request is a function within the flask.globals module of the Flask project.


## Example 1 from flask-sqlalchemy
[flask-sqlalchemy](https://github.com/pallets/flask-sqlalchemy)
([project documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
and
[PyPI information](https://pypi.org/project/Flask-SQLAlchemy/)) is a
[Flask](/flask.html) extension that makes it easier to use
[SQLAlchemy](/sqlalchemy.html) when building Flask apps. flask-sqlalchemy
provides helper functions that reduce the amount of common boilerplate
code that you have to frequently write yourself if you did not use this
library when combining Flask with SQLAlchemy.

flask-sqlalchemy is provided as open source under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/pallets/flask-sqlalchemy/blob/master/LICENSE.rst).

[**flask-sqlalchemy / flask_sqlalchemy / __init__.py**](https://github.com/pallets/flask-sqlalchemy/blob/master/flask_sqlalchemy/./__init__.py)

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import functools
import os
import sys
import time
import warnings
from math import ceil
from operator import itemgetter
from threading import Lock

import sqlalchemy
~~from flask import _app_ctx_stack, abort, current_app, request
from flask.signals import Namespace
from sqlalchemy import event, inspect, orm
from sqlalchemy.engine.url import make_url
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm.exc import UnmappedClassError
from sqlalchemy.orm.session import Session as SessionBase

from flask_sqlalchemy.model import Model
from ._compat import itervalues, string_types, xrange
from .model import DefaultMeta
from . import utils

__version__ = "3.0.0.dev"

# the best timer function for the platform
if sys.platform == 'win32':
    if sys.version_info >= (3, 3):
        _timer = time.perf_counter
    else:
        _timer = time.clock
else:
    _timer = time.time

_signals = Namespace()


## ... source file abbreviated to get to request examples ...


        be limited to that value. If there is no request or they aren't in the
        query, they default to 1 and 20 respectively. If ``count`` is ``False``,
        no query to help determine total page count will be run.

        When ``error_out`` is ``True`` (default), the following rules will
        cause a 404 response:

        * No items are found and ``page`` is not 1.
        * ``page`` is less than 1, or ``per_page`` is negative.
        * ``page`` or ``per_page`` are not ints.

        When ``error_out`` is ``False``, ``page`` and ``per_page`` default to
        1 and 20 respectively.

        Returns a :class:`Pagination` object.
        """

        if request:
            if page is None:
                try:
~~                    page = int(request.args.get('page', 1))
                except (TypeError, ValueError):
                    if error_out:
                        abort(404)

                    page = 1

            if per_page is None:
                try:
~~                    per_page = int(request.args.get('per_page', 20))
                except (TypeError, ValueError):
                    if error_out:
                        abort(404)

                    per_page = 20
        else:
            if page is None:
                page = 1

            if per_page is None:
                per_page = 20

        if max_per_page is not None:
            per_page = min(per_page, max_per_page)



## ... source file abbreviated to get to request examples ...


        if page < 1:
            if error_out:
                abort(404)
            else:
                page = 1

        if per_page < 0:
            if error_out:
                abort(404)


## ... source file continues with no further request examples...


```


## Example 2 from newspie
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


## ... source file abbreviated to get to request examples ...




@APP.errorhandler(404)
def page_not_found(error):
    ''' Not existing pages redirect to the first page of general category. '''
    return redirect(url_for('category', category='general', page=1))


@APP.route('/category/<string:category>', methods=['GET', 'POST'])
def category(category):
    ''' Handles category route.

    Parameters:
        - name: category
          in: path
          description: Name of the news category
        - name: page
          in: query
          description: Number of the page
    '''
~~    page = request.args.get('page', default=1, type=int)
    if page < 1:
        return redirect(url_for('category', category=category, page=1))
~~    if request.method == 'POST' and category in CATEGORIES:
        return do_post(page, category)
    if category in CATEGORIES:
        params = {'page': page, 'category': category, 'pageSize': PAGE_SIZE}
        country = get_cookie('country')
        if country is not None:
            params.update({'country': country})
        response = requests.get(TOP_HEADLINES,
                                params=params,
                                headers={'Authorization': API_KEY})
        if response.status_code == 200:
            pages = count_pages(response.json())
            if page > pages:
                page = pages
                return redirect(url_for('category', category=category, page=page))
            articles = parse_articles(response.json())
            return render(articles, page, pages, country, category)
        elif response.status_code == 401:
            return render_template(CONFIG['VARIOUS']['401_TEMPLATE'])
    return redirect(url_for('category', category='general', page=page))




## ... source file abbreviated to get to request examples ...


@APP.route('/search/<string:query>', methods=['GET', 'POST'])
def search(query):
    ''' Handles category route.

    Parameters:
        - name: query
          in: path
          description: Query string to be searched
        - name: page
          in: query
          description: Number of the page
    '''
~~    page = request.args.get('page', default=1, type=int)
    if page < 1:
        return redirect(url_for('search', query=query, page=1))
    params = {
        'qInTitle': query,
        'sortBy': 'relevancy',
        'page': page,
        'pageSize': PAGE_SIZE
    }
~~    if request.method == 'POST':
        return do_post(page, category='search', current_query=query)
    response = requests.get(EVERYTHING,
                            params=params,
                            headers={'Authorization': API_KEY})
    pages = count_pages(response.json())
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
~~    new_query = request.form.get('search_query')
~~    country = request.form.get('country')
~~    next_page = request.form.get('next_page')
~~    previous_page = request.form.get('previous_page')
    if new_query is not None and new_query != '':
        return redirect(url_for('search', query=new_query, page=1))
    if country is not None and country != get_cookie('country'):
        response = make_response(
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
    ''' Renders the template with appropriate variables. Up to 12 pages
        allowed. '''
    pages = pages if pages <= 12 else 12
    return render_template(CONFIG['VARIOUS']['TEMPLATE'],
                           articles=articles,
                           categories=CATEGORIES,
                           category=category,
                           countries=COUNTRIES,
                           country=country,
                           page=page,
                           pages=pages)


def get_cookie(key):
    ''' Helper method that gets cookie's value.

    Returns:
        A string with a value of a cookie with provided key. If a key is
        missing, None is returned.
    '''
~~    cookie_value = request.cookies.get(key)
    return cookie_value


if __name__ == '__main__':
    APP.run()


## ... source file continues with no further request examples...


```


## Example 3 from sandman2
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


## ... source file abbreviated to get to request examples ...




def jsonify(resource):
    """Return a Flask ``Response`` object containing a
    JSON representation of *resource*.

    :param resource: The resource to act as the basis of the response
    """

    response = flask.jsonify(resource.to_dict())
    response = add_link_headers(response, resource.links())
    return response


def is_valid_method(model, resource=None):
    """Return the error message to be sent to the client if the current
    request passes fails any user-defined validation."""
    validation_function_name = 'is_valid_{}'.format(
~~        request.method.lower())
    if hasattr(model, validation_function_name):
        return getattr(model, validation_function_name)(request, resource)

class Service(MethodView):

    """The *Service* class is a generic extension of Flask's *MethodView*,
    providing default RESTful functionality for a given ORM resource.

    Each service has an associated *__model__* attribute which represents the
    ORM resource it exposes. Services are JSON-only. HTML-based representation
    is available through the admin interface.
    """

    #: The sandman2.model.Model-derived class to expose
    __model__ = None

    #: The string used to describe the elements when a collection is
    #: returned.
    __json_collection_name__ = 'resources'

    def delete(self, resource_id):
        """Return an HTTP response object resulting from a HTTP DELETE call.

        :param resource_id: The value of the resource's primary key
        """
        resource = self._resource(resource_id)
        error_message = is_valid_method(self.__model__, resource)
        if error_message:
            raise BadRequestException(error_message)
        db.session().delete(resource)
        db.session().commit()
        return self._no_content_response()

    @etag
    def get(self, resource_id=None):
        """Return an HTTP response object resulting from an HTTP GET call.

        If *resource_id* is provided, return just the single resource.
        Otherwise, return the full collection.

        :param resource_id: The value of the resource's primary key
        """
~~        if request.path.endswith('meta'):
            return self._meta()

        if resource_id is None:
            error_message = is_valid_method(self.__model__)
            if error_message:
                raise BadRequestException(error_message)

~~            if 'export' in request.args: 
                return self._export(self._all_resources())

            return flask.jsonify({
                self.__json_collection_name__: self._all_resources()
                })
        else:
            resource = self._resource(resource_id)
            error_message = is_valid_method(self.__model__, resource)
            if error_message:
                raise BadRequestException(error_message)
            return jsonify(resource)

    def patch(self, resource_id):
        """Return an HTTP response object resulting from an HTTP PATCH call.

        :returns: ``HTTP 200`` if the resource already exists
        :returns: ``HTTP 400`` if the request is malformed
        :returns: ``HTTP 404`` if the resource is not found
        :param resource_id: The value of the resource's primary key
        """
        resource = self._resource(resource_id)
        error_message = is_valid_method(self.__model__, resource)
        if error_message:
            raise BadRequestException(error_message)
~~        if not request.json:
            raise BadRequestException('No JSON data received')
~~        resource.update(request.json)
        db.session().merge(resource)
        db.session().commit()
        return jsonify(resource)

    @validate_fields
    def post(self):
        """Return the JSON representation of a new resource created through
        an HTTP POST call.

        :returns: ``HTTP 201`` if a resource is properly created
        :returns: ``HTTP 204`` if the resource already exists
        :returns: ``HTTP 400`` if the request is malformed or missing data
        """
~~        resource = self.__model__.query.filter_by(**request.json).first()
        if resource:
            error_message = is_valid_method(self.__model__, resource)
            if error_message:
                raise BadRequestException(error_message)
            return self._no_content_response()

~~        resource = self.__model__(**request.json)  # pylint: disable=not-callable
        error_message = is_valid_method(self.__model__, resource)
        if error_message:
            raise BadRequestException(error_message)
        db.session().add(resource)
        db.session().commit()
        return self._created_response(resource)

    def put(self, resource_id):
        """Return the JSON representation of a new resource created or updated
        through an HTTP PUT call.

        If resource_id is not provided, it is assumed the primary key field is
        included and a totally new resource is created. Otherwise, the existing
        resource referred to by *resource_id* is updated with the provided JSON
        data. This method is idempotent.

        :returns: ``HTTP 201`` if a new resource is created
        :returns: ``HTTP 200`` if a resource is updated
        :returns: ``HTTP 400`` if the request is malformed or missing data
        """
        resource = self.__model__.query.get(resource_id)
        if resource:
            error_message = is_valid_method(self.__model__, resource)
            if error_message:
                raise BadRequestException(error_message)
~~            resource.update(request.json)
            db.session().merge(resource)
            db.session().commit()
            return jsonify(resource)

~~        resource = self.__model__(**request.json)  # pylint: disable=not-callable
        error_message = is_valid_method(self.__model__, resource)
        if error_message:
            raise BadRequestException(error_message)
        db.session().add(resource)
        db.session().commit()
        return self._created_response(resource)

    def _meta(self):
        """Return a description of this resource as reported by the
        database."""
        return flask.jsonify(self.__model__.description())

    def _resource(self, resource_id):
        """Return the ``sandman2.model.Model`` instance with the given
        *resource_id*.

        :rtype: :class:`sandman2.model.Model`
        """
        resource = self.__model__.query.get(resource_id)
        if not resource:
            raise NotFoundException()
        return resource

    def _all_resources(self):
        """Return the complete collection of resources as a list of
        dictionaries.

        :rtype: :class:`sandman2.model.Model`
        """
        queryset = self.__model__.query
~~        args = {k: v for (k, v) in request.args.items() if k not in ('page', 'export')}
        limit = None
        if args:
            filters = []
            order = []
            for key, value in args.items():
                if value.startswith('%'):
                    filters.append(getattr(self.__model__, key).like(str(value), escape='/'))
                elif key == 'sort':
                    direction = desc if value.startswith('-') else asc
                    order.append(direction(getattr(self.__model__, value.lstrip('-'))))
                elif key == 'limit':
                    limit = int(value)
                elif hasattr(self.__model__, key):
                    filters.append(getattr(self.__model__, key) == value)
                else:
                    raise BadRequestException('Invalid field [{}]'.format(key))
            queryset = queryset.filter(*filters).order_by(*order)
~~        if 'page' in request.args:
~~            resources = queryset.paginate(page=int(request.args['page']), per_page=limit).items
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
        response = make_response(faux_csv)
        response.mimetype = 'text/csv'
        return response


    @staticmethod
    def _no_content_response():
        """Return an HTTP 204 "No Content" response.

        :returns: HTTP Response


## ... source file continues with no further request examples...


```

