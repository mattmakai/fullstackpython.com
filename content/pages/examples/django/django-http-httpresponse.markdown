title: django.http HttpResponse Python Code Examples
category: page
slug: django-http-httpresponse-examples
sortorder: 500013420
toc: False
sidebartitle: django.http HttpResponse
meta: Example Python code for using the HttpResponse object provided by Django in the django.http module.


[HttpResponse](https://docs.djangoproject.com/en/stable/ref/request-response/#httpresponse-objects)
([source code](https://github.com/django/django/blob/master/django/http/response.py))
provides an inbound HTTP request to a [Django](/django.html) web application
with a text response. This class is most frequently used as a return object
from a Django view.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog_tests / tests.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog_tests/tests.py)

```python
import datetime
import django
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User, AnonymousUser
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
~~from django.http import HttpResponse
from django.test import TestCase, RequestFactory
from django.utils import dateformat, formats, timezone
from dateutil.tz import gettz

from auditlog.middleware import AuditlogMiddleware
from auditlog.models import LogEntry
from auditlog.registry import auditlog
from auditlog_tests.models import (SimpleModel, AltPrimaryKeyModel, 
    UUIDPrimaryKeyModel, ProxyModel, SimpleIncludeModel, 
    SimpleExcludeModel, SimpleMappingModel, RelatedModel, 
    ManyRelatedModel, AdditionalDataIncludedModel, DateTimeFieldModel,
    ChoicesFieldModel, CharfieldTextfieldModel, 
    PostgresArrayFieldModel, NoDeleteHistoryModel)
from auditlog import compat


## ... source file abbreviated to get to HttpResponse examples ...


class MiddlewareTest(TestCase):
    """
    Test the middleware responsible for connecting and 
    disconnecting the signals used in automatic logging.
    """
    def setUp(self):
        self.middleware = AuditlogMiddleware()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test', 
                                             email='test@example.com', 
                                             password='top_secret')

    def test_request_anonymous(self):
        """No actor will be logged when a user is not logged in."""
        # Create a request
        request = self.factory.get('/')
        request.user = AnonymousUser()

        # Run middleware
        self.middleware.process_request(request)

        # Validate result
        self.assertFalse(pre_save.has_listeners(LogEntry))

        # Finalize transaction
        self.middleware.process_exception(request, None)

    def test_request(self):
        """The actor will be logged when a user is logged in."""
        # Create a request
        request = self.factory.get('/')
        request.user = self.user
        # Run middleware
        self.middleware.process_request(request)

        # Validate result
        self.assertTrue(pre_save.has_listeners(LogEntry))

        # Finalize transaction
        self.middleware.process_exception(request, None)

    def test_response(self):
        """The signal will be disconnected when the 
        request is processed."""
        # Create a request
        request = self.factory.get('/')
        request.user = self.user

        # Run middleware
        self.middleware.process_request(request)
        # signal should be present before trying to disconnect it.
        self.assertTrue(pre_save.has_listeners(LogEntry))  
~~        self.middleware.process_response(request, HttpResponse())

        # Validate result
        self.assertFalse(pre_save.has_listeners(LogEntry))

    def test_exception(self):
        """The signal will be disconnected when 
        an exception is raised."""
        # Create a request
        request = self.factory.get('/')
        request.user = self.user

        # Run middleware
        self.middleware.process_request(request)
        # signal should be present before trying to disconnect it.
        self.assertTrue(pre_save.has_listeners(LogEntry))  
        self.middleware.process_exception(request, 
                                          ValidationError("Test"))

        # Validate result
        self.assertFalse(pre_save.has_listeners(LogEntry))


## ... source file continues with no further HttpResponse examples ...
```


## Example 2 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / chair / views**](https://github.com/dccnconf/dccnsys/tree/master/wwwdccn/chair/views)

```python
import csv
import functools
import logging
import math
from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import Q
~~from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.decorators.http import require_GET, require_POST
from django.utils.translation import ugettext_lazy as _

from chair.forms import FilterSubmissionsForm, FilterUsersForm, \
    ChairUploadReviewManuscriptForm, AssignReviewerForm
from conferences.decorators import chair_required
from conferences.models import Conference
from review.models import Reviewer, Review
from submissions.models import Submission
from submissions.forms import SubmissionDetailsForm, AuthorCreateForm, \
    AuthorDeleteForm, InviteAuthorForm, AuthorsReorderForm
from users.models import Profile

ITEMS_PER_PAGE = 10


User = get_user_model()
logger = logging.getLogger(__name__)


## ... source file abbreviated to get to the HttpResponse examples ...


###################################################################
# CSV EXPORTS
###################################################################
@chair_required
@require_GET
def get_submissions_csv(request, pk):
    conference = get_object_or_404(Conference, pk=pk)
    submissions = list(conference.submission_set.all().\
                       order_by('pk'))
    profs = {
        sub: Profile.objects.filter(user__authorship__submission=\
                                    sub).all()
        for sub in submissions
    }

~~    # Create the HttpResponse object with the appropriate CSV header.
~~    response = HttpResponse(content_type='text/csv')
~~    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
~~    response['Content-Disposition'] = \
~~        f'attachment; filename="submissions-{timestamp}.csv"'

~~    writer = csv.writer(response)
    number = 1
    writer.writerow([
        '#', 'ID', 'TITLE', 'AUTHORS', 'COUNTRY', 'CORR_AUTHOR', 
        'CORR_EMAIL', 'LANGUAGE', 'LINK',
    ])

    for sub in submissions:
        authors = ', '.join(pr.get_full_name() \
                            for pr in profs[sub])
        countries = ', '.join(set(p.get_country_display() \
                                  for p in profs[sub]))
        owner = sub.created_by
        corr_author = owner.profile.get_full_name() if owner else ''
        corr_email = owner.email if owner else ''

        if sub.review_manuscript:
            link = request.build_absolute_uri(
                reverse('submissions:download-manuscript', 
                        args=[sub.pk]))
        else:
            link = ''
        stype = sub.stype.get_language_display() if sub.stype else ''

        row = [
            number, sub.pk, sub.title, authors, countries, 
            corr_author, corr_email, stype, link
        ]
        writer.writerow(row)
        number += 1

~~    return response


@chair_required
@require_GET
def get_authors_csv(request, pk):
    conference = get_object_or_404(Conference, pk=pk)

    users = {
        user: list(user.authorship.filter(
            submission__conference=conference
        ).order_by('pk')) for user in User.objects.all()
    }

    # Create the HttpResponse object with appropriate CSV header.
~~    response = HttpResponse(content_type='text/csv')
~~    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
~~    response['Content-Disposition'] = \
~~        f'attachment; filename="authors-{timestamp}.csv"'

~~    writer = csv.writer(response)
    number = 1
    writer.writerow([
        '#', 'ID', 'FULL_NAME', 'FULL_NAME_RUS', 'DEGREE', 
        'COUNTRY', 'CITY', 'AFFILIATION', 'ROLE', 'EMAIL'
    ])

    for user in users:
        prof = user.profile
        row = [
            number, user.pk, prof.get_full_name(), 
            prof.get_full_name_rus(),
            prof.degree, prof.get_country_display(), prof.city,
            prof.affiliation, prof.role, user.email,
        ]
        writer.writerow(row)
        number += 1

~~    return response
```


## Example 3 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / views / mixins.py**](https://github.com/jrief/django-angular/blob/master/djng/views/mixins.py)

```python
# -*- coding: utf-8 -*-
import json
import warnings
from django.core.serializers.json import DjangoJSONEncoder
~~from django.http import (HttpResponse, HttpResponseBadRequest, 
                           HttpResponseForbidden)


def allow_remote_invocation(func, method='auto'):
    """
    All methods which shall be callable through a given Ajax 
    'action' must be decorated with @allowed_action. This is 
    required for safety reasons. It inhibits the caller to 
    invoke all available methods of a class.
    """
    setattr(func, 'allow_rmi', method)
    return func


def allowed_action(func):
    warnings.warn("Decorator `@allowed_action` is deprecated. "
                  "Use `@allow_remote_invocation` instead.", 
                  DeprecationWarning)
    return allow_remote_invocation(func)


class JSONResponseException(Exception):
    """
    Exception class for triggering HTTP 4XX responses with 
    JSON content, where expected.
    """
    status_code = 400

    def __init__(self, message=None, status=None, *args, **kwargs):
        if status is not None:
            self.status_code = status
        super(JSONResponseException, self).__init__(message, *args, 
                                                    **kwargs)


class JSONBaseMixin(object):
    """
    Basic mixin for encoding HTTP responses in JSON format.
    """
    json_encoder = DjangoJSONEncoder
    json_content_type = 'application/json;charset=UTF-8'

~~    def json_response(self, response_data, status=200, **kwargs):
~~        out_data = json.dumps(response_data, cls=self.json_encoder, 
~~                              **kwargs)
~~        response = HttpResponse(out_data, self.json_content_type, 
~~                                status=status)
~~        response['Cache-Control'] = 'no-cache'
~~        return response


## ... source file continues with no further HttpResponse examples ...
```


## Example 4 from django-axes
[django-axes](https://github.com/jazzband/django-axes/)
([project documentation](https://django-axes.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-axes/)
is a code library for [Django](/django.html) projects to track failed
login attempts against a web application. The goal of the project is
to make it easier for you to stop people and scripts from hacking your
Django-powered website.

The code for django-axes is
[open source under the MIT license](https://github.com/jazzband/django-axes/blob/master/LICENSE)
and maintained by the group of developers known as
[Jazzband](https://jazzband.co/).

[**django-axes / axes / tests / test_utils.py**](https://github.com/jazzband/django-axes/blob/master/axes/tests/test_utils.py)

```python
from datetime import timedelta
from hashlib import md5
from unittest.mock import patch

~~from django.http import (JsonResponse, HttpResponseRedirect, 
~~                         HttpResponse, HttpRequest)
from django.test import override_settings, RequestFactory

from axes.apps import AppConfig
from axes.models import AccessAttempt
from axes.tests.base import AxesTestCase
from axes.helpers import (
    get_cache_timeout,
    get_client_str,
    get_client_username,
    get_client_cache_key,
    get_client_parameters,
    get_cool_off_iso8601,
    get_lockout_response,
    is_client_ip_address_blacklisted,
    is_client_ip_address_whitelisted,
    is_ip_address_in_blacklist,
    is_ip_address_in_whitelist,
    is_client_method_whitelisted,
    toggleable,
)


## ... source file abbreviated to get to HttpResponse examples ...


class LockoutResponseTestCase(AxesTestCase):
    def setUp(self):
        self.request = HttpRequest()

    @override_settings(AXES_COOLOFF_TIME=42)
    def test_get_lockout_response_cool_off(self):
        get_lockout_response(request=self.request)

    @override_settings(AXES_LOCKOUT_TEMPLATE='example.html')
    @patch('axes.helpers.render')
    def test_get_lockout_response_lockout_template(self, render):
        self.assertFalse(render.called)
        get_lockout_response(request=self.request)
        self.assertTrue(render.called)

    @override_settings(AXES_LOCKOUT_URL='https://example.com')
    def test_get_lockout_response_lockout_url(self):
        response = get_lockout_response(request=self.request)
        self.assertEqual(type(response), HttpResponseRedirect)

    def test_get_lockout_response_lockout_json(self):
        self.request.is_ajax = lambda: True
        response = get_lockout_response(request=self.request)
        self.assertEqual(type(response), JsonResponse)

~~    def test_get_lockout_response_lockout_response(self):
~~        response = get_lockout_response(request=self.request)
~~        self.assertEqual(type(response), HttpResponse)

```


## Example 5 from django-extensions
[django-extensions](https://github.com/django-extensions/django-extensions)
([project documentation](https://django-extensions.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-extensions/))
is a [Django](/django.html) project that adds a bunch of additional
useful commands to the `manage.py` interface. This 
[GoDjango video](https://www.youtube.com/watch?v=1F6G3ONhr4k) provides a 
quick overview of what you get when you install it into your Python
environment.

The django-extensions project is open sourced under the
[MIT license](https://github.com/django-extensions/django-extensions/blob/master/LICENSE).

[**django-extensions / django_extensions / admin / __init__.py**](https://github.com/django-extensions/django-extensions/blob/master/django_extensions/admin/__init__.py)

```python
# -*- coding: utf-8 -*-
#
# Autocomplete feature for admin panel
#
import six
import operator
from functools import update_wrapper
from six.moves import reduce
from typing import Tuple, Dict, Callable  # NOQA

from django.apps import apps
~~from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
from django.utils.encoding import smart_str
from django.utils.translation import ugettext as _
from django.utils.text import get_text_list
from django.contrib import admin

from django_extensions.admin.widgets import ForeignKeySearchInput


class ForeignKeyAutocompleteAdminMixin(object):
    """
    Admin class for models using the autocomplete feature.

    There are two additional fields:
       - related_search_fields: defines fields of managed model that
         have to be represented by autocomplete input, together with
         a list of target model fields that are searched for
         input string, e.g.:

         related_search_fields = {
            'author': ('first_name', 'email'),
         }

       - related_string_functions: contains optional functions which
         take target model instance as only argument and return string
         representation. By default __unicode__() method of target
         object is used.

    And also an optional additional field to set the limit on the
    results returned by the autocomplete query. You can set this 
    integer value in your settings file using 
    FOREIGNKEY_AUTOCOMPLETE_LIMIT or you can set this per 
    ForeignKeyAutocompleteAdmin basis. If any value
    is set the results will not be limited.
    """

    related_search_fields = {}  # type: Dict[str, Tuple[str]]
    related_string_functions = {}  # type: Dict[str, Callable]
    autocomplete_limit = getattr(settings, 
                                 'FOREIGNKEY_AUTOCOMPLETE_LIMIT', 
                                 None)

    def get_urls(self):
        from django.conf.urls import url

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, 
                                                        **kwargs)
            return update_wrapper(wrapper, view)

        return [
            url(r'foreignkey_autocomplete/$', 
                wrap(self.foreignkey_autocomplete),
                name='%s_%s_autocomplete' % \
                     (self.model._meta.app_label, 
                      self.model._meta.model_name))
        ] + super(ForeignKeyAutocompleteAdminMixin, 
                  self).get_urls()

    def foreignkey_autocomplete(self, request):
        """
        Search in the fields of the given related model and 
        returns the result as a simple string to be used by 
        the jQuery Autocomplete plugin
        """
        query = request.GET.get('q', None)
        app_label = request.GET.get('app_label', None)
        model_name = request.GET.get('model_name', None)
        search_fields = request.GET.get('search_fields', None)
        object_pk = request.GET.get('object_pk', None)

        try:
            to_string_function = \
                self.related_string_functions[model_name]
        except KeyError:
            if six.PY3:
                to_string_function = lambda x: x.__str__()
            else:
                to_string_function = lambda x: x.__unicode__()

        if search_fields and app_label and \
            model_name and (query or object_pk):
            def construct_search(field_name):
                # use different lookup methods depending on the notation
                if field_name.startswith('^'):
                    return "%s__istartswith" % field_name[1:]
                elif field_name.startswith('='):
                    return "%s__iexact" % field_name[1:]
                elif field_name.startswith('@'):
                    return "%s__search" % field_name[1:]
                else:
                    return "%s__icontains" % field_name

            model = apps.get_model(app_label, model_name)

            queryset = model._default_manager.all()
            data = ''
            if query:
                for bit in query.split():
                    or_queries = [models.Q(**{construct_search(\
                                  smart_str(field_name)): \
                                  smart_str(bit)}) for field_name in \
                                  search_fields.split(',')]
                    other_qs = QuerySet(model)
                    other_qs.query.select_related = \
                        queryset.query.select_related
                    other_qs = other_qs.filter(reduce(\
                                               operator.or_, 
                                               or_queries))
                    queryset = queryset & other_qs

                additional_filter = self.get_related_filter(model, 
                                                            request)
                if additional_filter:
                    queryset = queryset.filter(additional_filter)

                if self.autocomplete_limit:
                    queryset = queryset[:self.autocomplete_limit]

                data = ''.join([six.u('%s|%s\n') % \
                        (to_string_function(f), 
                         f.pk) for f in queryset])
            elif object_pk:
                try:
                    obj = queryset.get(pk=object_pk)
                except Exception:  # FIXME: use stricter exception check 
                    pass
                else:
                    data = to_string_function(obj)
~~            return HttpResponse(data, content_type='text/plain')
        return HttpResponseNotFound()


## ... source file continues with no further HttpResponse examples ...
```
