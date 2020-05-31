title: flask.templating render_template Python code examples
category: page
slug: flask-templating-render-template-examples
sortorder: 500021000
toc: False
sidebartitle: flask.templating render_template
meta: Python example code for the render_template function from the flask.templating module of the Flask project.


render_template is a function within the flask.templating module of the Flask project.


## Example 1 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / email.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/./email.py)

```python
# email.py
# -*- coding: utf-8 -*-
"""
    flaskbb.email
    -------------

    This module adds the functionality to send emails

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
import logging
~~from flask import render_template
from flask_mail import Message
from flask_babelplus import lazy_gettext as _

from flaskbb.extensions import mail, celery


logger = logging.getLogger(__name__)


@celery.task
def send_reset_token(token, username, email):
    """Sends the reset token to the user's email address.

    :param token: The token to send to the user
    :param username: The username to whom the email should be sent.
    :param email:  The email address of the user
    """
    send_email(
        subject=_("Password Recovery Confirmation"),
        recipients=[email],
~~        text_body=render_template(
            "email/reset_password.txt",
            username=username,
            token=token
        ),
~~        html_body=render_template(
            "email/reset_password.html",
            username=username,
            token=token
        )
    )


@celery.task
def send_activation_token(token, username, email):
    """Sends the activation token to the user's email address.

    :param token: The token to send to the user
    :param username: The username to whom the email should be sent.
    :param email:  The email address of the user
    """
    send_email(
        subject=_("Account Activation"),
        recipients=[email],
~~        text_body=render_template(
            "email/activate_account.txt",
            username=username,
            token=token
        ),
~~        html_body=render_template(
            "email/activate_account.html",
            username=username,
            token=token
        )
    )


@celery.task
def send_async_email(*args, **kwargs):
    send_email(*args, **kwargs)


def send_email(subject, recipients, text_body, html_body, sender=None):
    """Sends an email to the given recipients.

    :param subject: The subject of the email.
    :param recipients: A list of recipients.
    :param text_body: The text body of the email.
    :param html_body: The html body of the email.
    :param sender: A two-element tuple consisting of name and address.
                   If no sender is given, it will fall back to the one you
                   have configured with ``MAIL_DEFAULT_SENDER``.
    """
    msg = Message(subject, recipients=recipients, sender=sender)


## ... source file continues with no further render_template examples...


```


## Example 2 from flask-base
[flask-base](https://github.com/hack4impact/flask-base)
([project documentation](http://hack4impact.github.io/flask-base/))
provides boilerplate code for new [Flask](/flask.html) web apps.
The purpose of the boilerplate is to stitch together disparate
libraries that are commonly used in Flask projects, such as
[Redis](/redis.html) for fast caching and transient data storage,
[SendGrid](https://www.twilio.com/sendgrid) for transactional email,
[SQLAlchemy](/sqlalchemy.html) for persistent data storage through a
[relational database](/databases.html) backend,
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) for form
handling and many others.

flask-base is provided as open source under the
[MIT license](https://github.com/hack4impact/flask-base/blob/master/LICENSE.md).

[**flask-base / app / email.py**](https://github.com/hack4impact/flask-base/blob/master/app/./email.py)

```python
# email.py
import os

~~from flask import render_template
from flask_mail import Message

from app import create_app
from app import mail


def send_email(recipient, subject, template, **kwargs):
    app = create_app(os.getenv('FLASK_CONFIG') or 'default')
    with app.app_context():
        msg = Message(
            app.config['EMAIL_SUBJECT_PREFIX'] + ' ' + subject,
            sender=app.config['EMAIL_SENDER'],
            recipients=[recipient])
~~        msg.body = render_template(template + '.txt', **kwargs)
~~        msg.html = render_template(template + '.html', **kwargs)
        mail.send(msg)


## ... source file continues with no further render_template examples...


```


## Example 3 from flask_jsondash
[Flask JSONDash](https://github.com/christabor/flask_jsondash) is a
configurable web application built in Flask that creates charts and
dashboards from arbitrary API endpoints. Everything for the web app
is configured in JSON. The code is provided as open source under the
[MIT license](https://github.com/christabor/flask_jsondash/blob/master/LICENSE).

[**flask_jsondash / flask_jsondash / charts_builder.py**](https://github.com/christabor/flask_jsondash/blob/master/flask_jsondash/./charts_builder.py)

```python
# charts_builder.py
# -*- coding: utf-8 -*-

"""
flask_jsondash.charts_builder
-----------------------------

The chart blueprint that houses all functionality.

:copyright: (c) 2016 by Chris Tabor.
:license: MIT, see LICENSE for more details.
"""

import json
import os
import uuid
from datetime import datetime as dt

import jinja2
~~from flask import (Blueprint, current_app, flash, redirect, render_template,
                   request, send_from_directory, url_for)

from flask_jsondash import static, templates

from flask_jsondash import db
from flask_jsondash import settings
from flask_jsondash.utils import setting
from flask_jsondash.utils import adapter
from flask_jsondash import utils
from flask_jsondash.schema import (
    validate_raw_json, InvalidSchemaError,
)

TEMPLATE_DIR = os.path.dirname(templates.__file__)
STATIC_DIR = os.path.dirname(static.__file__)

# Internally required libs that are also shared in `settings.py`
# for charts. These follow the same format as what is loaded in
# `get_active_assets` so that shared libraries are loaded in the same manner
# for simplicty and prevention of duplicate loading.
# Note these are just LABELS, not files.
REQUIRED_STATIC_FAMILES = ['D3']

charts = Blueprint(


## ... source file abbreviated to get to render_template examples ...


    if views:
        pagination = utils.paginator(count=len(views),
                                     page=page, per_page=per_page)
        opts.update(limit=pagination.limit, skip=pagination.skip)
        views = views[pagination.skip:pagination.next]
    else:
        pagination = None
    categorized = utils.categorize_views(views)
    kwargs = dict(
        total=len(views),
        views=categorized,
        view=None,
        paginator=pagination,
        creating=True,
        can_edit_global=auth(authtype='edit_global'),
        total_modules=sum([
            len(view.get('modules', [])) for view in views
            if isinstance(view, dict)
        ]),
    )
~~    return render_template('pages/charts_index.html', **kwargs)


@charts.route('/charts/<c_id>', methods=['GET'])
def view(c_id):
    """Load a json view config from the DB."""
    if not auth(authtype='view', view_id=c_id):
        flash('You do not have access to view this dashboard.', 'error')
        return redirect(url_for('jsondash.dashboard'))
    viewjson = adapter.read(c_id=c_id)
    if not viewjson:
        flash('Could not find view: {}'.format(c_id), 'error')
        return redirect(url_for('jsondash.dashboard'))
    # Remove _id, it's not JSON serializeable.
    if '_id' in viewjson:
        viewjson.pop('_id')
    if 'modules' not in viewjson:
        flash('Invalid configuration - missing modules.', 'error')
        return redirect(url_for('jsondash.dashboard'))
    # Chart family is encoded in chart type value for lookup.
    active_charts = [v.get('family') for v in viewjson['modules']
                     if v.get('family') is not None]
    # If the logged in user is also the creator of this dashboard,
    # let me edit it. Otherwise, defer to any user-supplied auth function
    # for this specific view.
    if metadata(key='username') == viewjson.get('created_by'):
        can_edit = True
    else:
        can_edit = auth(authtype='edit_others', view_id=c_id)
    # Backwards compatible layout type
    layout_type = viewjson.get('layout', 'freeform')
    kwargs = dict(
        id=c_id,
        view=viewjson,
        categories=get_categories(),
        num_rows=(
            None if layout_type == 'freeform' else utils.get_num_rows(viewjson)
        ),
        modules=utils.sort_modules(viewjson),
        assets=get_active_assets(active_charts),
        can_edit=can_edit,
        can_edit_global=auth(authtype='edit_global'),
        is_global=utils.is_global_dashboard(viewjson),
    )
~~    return render_template('pages/chart_detail.html', **kwargs)


@charts.route('/charts/<c_id>/delete', methods=['POST'])
def delete(c_id):
    """Delete a json dashboard config."""
    dash_url = url_for('jsondash.dashboard')
    if not auth(authtype='delete'):
        flash('You do not have access to delete dashboards.', 'error')
        return redirect(dash_url)
    adapter.delete(c_id)
    flash('Deleted dashboard "{}"'.format(c_id))
    return redirect(dash_url)


@charts.route('/charts/<c_id>/update', methods=['POST'])
def update(c_id):
    """Normalize the form POST and setup the json view config object."""
    if not auth(authtype='update'):
        flash('You do not have access to update dashboards.', 'error')
        return redirect(url_for('jsondash.dashboard'))
    viewjson = adapter.read(c_id=c_id)
    if not viewjson:
        flash('Could not find view: {}'.format(c_id), 'error')
        return redirect(url_for('jsondash.dashboard'))


## ... source file continues with no further render_template examples...


```


## Example 4 from flask-phone-input
[flask-phone-input](https://github.com/miguelgrinberg/flask-phone-input)
is an example application that ties together the
[intTellInput.js](https://github.com/jackocnr/intl-tel-input)
JavaScript plugin with the
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) form-handling
library. flask-phone-input is provided as open source under the
[MIT license](https://github.com/miguelgrinberg/flask-phone-input/blob/1a1c227c044474ce0fe133493d7f8b0fb8312409/LICENSE).

[**flask-phone-input / app.py**](https://github.com/miguelgrinberg/flask-phone-input/blob/master/././app.py)

```python
# app.py
~~from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import phonenumbers
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'
Bootstrap(app)


class PhoneForm(FlaskForm):
    phone = StringField('Phone', validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PhoneForm()
    if form.validate_on_submit():
        session['phone'] = form.phone.data
        return redirect(url_for('show_phone'))
~~    return render_template('index.html', form=form)


@app.route('/showphone')
def show_phone():
~~    return render_template('show_phone.html', phone=session['phone'])


## ... source file continues with no further render_template examples...


```


## Example 5 from flask-restx
[Flask RESTX](https://github.com/python-restx/flask-restx) is an
extension that makes it easier to build
[RESTful APIs](/application-programming-interfaces.html) into
your applications. Flask RESTX aims for minimal configuration to
get basic APIs running for existing applications and it exposes
endpoint documentation using [Swagger](https://swagger.io/).

Flask RESTX is provided as open source under the
[BSD  3-Clause license](https://github.com/python-restx/flask-restx/blob/master/LICENSE).

[**flask-restx / flask_restx / apidoc.py**](https://github.com/python-restx/flask-restx/blob/master/flask_restx/./apidoc.py)

```python
# apidoc.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

~~from flask import url_for, Blueprint, render_template


class Apidoc(Blueprint):
    """
    Allow to know if the blueprint has already been registered
    until https://github.com/mitsuhiko/flask/pull/1301 is merged
    """

    def __init__(self, *args, **kwargs):
        self.registered = False
        super(Apidoc, self).__init__(*args, **kwargs)

    def register(self, *args, **kwargs):
        super(Apidoc, self).register(*args, **kwargs)
        self.registered = True


apidoc = Apidoc(
    "restx_doc",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/swaggerui",
)


@apidoc.add_app_template_global
def swagger_static(filename):
    return url_for("restx_doc.static", filename=filename)


def ui_for(api):
    """Render a SwaggerUI for a given API"""
~~    return render_template("swagger-ui.html", title=api.title, specs_url=api.specs_url)


## ... source file continues with no further render_template examples...


```


## Example 6 from Flasky
[Flasky](https://github.com/miguelgrinberg/flasky) is a wonderful
example application by
[Miguel Grinberg](https://github.com/miguelgrinberg) that he builds
while teaching developers how to use [Flask](/flask.html) in
[his books and videos](https://courses.miguelgrinberg.com/). Flasky
is [open sourced under the MIT license](https://github.com/miguelgrinberg/flasky/blob/master/LICENSE).

[**Flasky / app / email.py**](https://github.com/miguelgrinberg/flasky/blob/master/./app/email.py)

```python
# email.py
from threading import Thread
~~from flask import current_app, render_template
from flask_mail import Message
from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + ' ' + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'], recipients=[to])
~~    msg.body = render_template(template + '.txt', **kwargs)
~~    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr


## ... source file continues with no further render_template examples...


```


## Example 7 from newspie
[NewsPie](https://github.com/skamieniarz/newspie) is a minimalistic news
aggregator created with [Flask](/flask.html) and the
[News API](https://newsapi.org/).

NewsPie is provided as open source under the
[MIT license](https://github.com/skamieniarz/newspie/blob/master/LICENSE).

[**newspie / news.py**](https://github.com/skamieniarz/newspie/blob/master/././news.py)

```python
# news.py
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


## ... source file abbreviated to get to render_template examples ...


    if page < 1:
        return redirect(url_for('category', category=category, page=1))
    if request.method == 'POST' and category in CATEGORIES:
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
~~            return render_template(CONFIG['VARIOUS']['401_TEMPLATE'])
    return redirect(url_for('category', category='general', page=page))


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
    page = request.args.get('page', default=1, type=int)
    if page < 1:
        return redirect(url_for('search', query=query, page=1))
    params = {
        'qInTitle': query,
        'sortBy': 'relevancy',
        'page': page,
        'pageSize': PAGE_SIZE
    }


## ... source file abbreviated to get to render_template examples ...


            })
    return parsed_articles


def count_pages(response):
    ''' Helper method that counts number of total pages basing on total
        results from News API response and page size.

    Returns:
        An int with a number of total pages. '''
    pages = 0
    if response.get('status') == 'ok':
        pages = (-(-response.get('totalResults', 0) // PAGE_SIZE))
    return pages


def render(articles, page, pages, country, category):
    ''' Renders the template with appropriate variables. Up to 12 pages
        allowed. '''
    pages = pages if pages <= 12 else 12
~~    return render_template(CONFIG['VARIOUS']['TEMPLATE'],
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
    cookie_value = request.cookies.get(key)
    return cookie_value


if __name__ == '__main__':
    APP.run()


## ... source file continues with no further render_template examples...


```

