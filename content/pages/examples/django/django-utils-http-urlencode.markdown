title: django.utils.http urlencode Example Code
category: page
slug: django-utils-http-urlencode-examples
sortorder: 500011475
toc: False
sidebartitle: django.utils.http urlencode
meta: Python example code for the urlencode callable from the django.utils.http module of the Django project.


urlencode is a callable within the django.utils.http module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / utils.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/utils.py)

```python
# utils.py
import unicodedata
from collections import OrderedDict
from datetime import timedelta

from django.conf import settings
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import FieldDoesNotExist, ValidationError
from django.db import models
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.utils.encoding import force_str
~~from django.utils.http import base36_to_int, int_to_base36, urlencode
from django.utils.timezone import now

from ..exceptions import ImmediateHttpResponse
from ..utils import (
    get_request_param,
    get_user_model,
    import_callable,
    valid_email_or_none,
)
from . import app_settings, signals
from .adapter import get_adapter
from .app_settings import EmailVerificationMethod


def _unicode_ci_compare(s1, s2):
    norm_s1 = unicodedata.normalize('NFKC', s1).casefold()
    norm_s2 = unicodedata.normalize('NFKC', s2).casefold()
    return norm_s1 == norm_s2


def get_next_redirect_url(request, redirect_field_name="next"):
    redirect_to = get_request_param(request, redirect_field_name)
    if not get_adapter(request).is_safe_url(redirect_to):
        redirect_to = None


## ... source file abbreviated to get to urlencode examples ...


    from .models import EmailAddress
    User = get_user_model()
    mails = EmailAddress.objects.filter(email__iexact=email)
    if is_active is not None:
        mails = mails.filter(user__is_active=is_active)
    users = []
    for e in mails.prefetch_related('user'):
        if _unicode_ci_compare(e.email, email):
            users.append(e.user)
    if app_settings.USER_MODEL_EMAIL_FIELD:
        q_dict = {app_settings.USER_MODEL_EMAIL_FIELD + '__iexact': email}
        user_qs = User.objects.filter(**q_dict)
        if is_active is not None:
            user_qs = user_qs.filter(is_active=is_active)
        for user in user_qs.iterator():
            user_email = getattr(user, app_settings.USER_MODEL_EMAIL_FIELD)
            if _unicode_ci_compare(user_email, email):
                users.append(user)
    return list(set(users))


def passthrough_next_redirect_url(request, url, redirect_field_name):
    assert url.find("?") < 0  # TODO: Handle this case properly
    next_url = get_next_redirect_url(request, redirect_field_name)
    if next_url:
~~        url = url + '?' + urlencode({redirect_field_name: next_url})
    return url


def user_pk_to_url_str(user):
    User = get_user_model()
    if issubclass(type(User._meta.pk), models.UUIDField):
        if isinstance(user.pk, str):
            return user.pk
        return user.pk.hex

    ret = user.pk
    if isinstance(ret, int):
        ret = int_to_base36(user.pk)
    return str(ret)


def url_str_to_user_pk(s):
    User = get_user_model()
    if getattr(User._meta.pk, 'remote_field', None):
        pk_field = User._meta.pk.remote_field.to._meta.pk
    else:
        pk_field = User._meta.pk
    if issubclass(type(pk_field), models.UUIDField):
        return pk_field.to_python(s)


## ... source file continues with no further urlencode examples...

```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / templatetags / cms_tags.py**](https://github.com/divio/django-cms/blob/develop/cms/templatetags/cms_tags.py)

```python
# cms_tags.py
from collections import namedtuple, OrderedDict
from copy import copy
from datetime import datetime

from django import template
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import mail_managers
from django.db.models import Model
from django.middleware.common import BrokenLinkEmailsMiddleware
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_text, smart_text
from django.utils.html import escape
~~from django.utils.http import urlencode
from django.utils.translation import (
    get_language,
    override as force_language,
    ugettext_lazy as _,
)

from six import string_types, integer_types

from classytags.arguments import (Argument, MultiValueArgument,
                                  MultiKeywordArgument)
from classytags.core import Options, Tag
from classytags.helpers import InclusionTag, AsTag
from classytags.parser import Parser
from classytags.utils import flatten_context
from classytags.values import ListValue, StringValue

from cms.cache.page import get_page_url_cache, set_page_url_cache
from cms.exceptions import PlaceholderNotFound
from cms.models import Page, Placeholder as PlaceholderModel, CMSPlugin, StaticPlaceholder
from cms.plugin_pool import plugin_pool
from cms.toolbar.utils import get_toolbar_from_request
from cms.utils import get_current_site, get_language_from_request, get_site_id
from cms.utils.compat.dj import get_middleware
from cms.utils.moderator import use_draft


## ... source file abbreviated to get to urlencode examples ...


                else:
                    url_base = method
            else:
                if not editmode:
                    view_url = 'admin:%s_%s_add' % (
                        opts.app_label, opts.model_name)
                    url_base = reverse(view_url)
                elif not edit_fields:
                    if not view_url:
                        view_url = 'admin:%s_%s_change' % (
                            opts.app_label, opts.model_name)
                    if isinstance(instance, Page):
                        url_base = reverse(view_url, args=(instance.pk, language))
                    else:
                        url_base = reverse(view_url, args=(instance.pk,))
                else:
                    if not view_url:
                        view_url = 'admin:%s_%s_edit_field' % (
                            opts.app_label, opts.model_name)
                    if view_url.endswith('_changelist'):
                        url_base = reverse(view_url)
                    else:
                        url_base = reverse(view_url, args=(instance.pk, language))
                    querystring['edit_fields'] = ",".join(context['edit_fields'])
            if editmode:
~~                extra_context['edit_url'] = "%s?%s" % (url_base, urlencode(querystring))
            else:
                extra_context['edit_url'] = "%s" % url_base
            extra_context['refresh_page'] = True
            if getattr(context['request'], 'current_page', None):
                extra_context['redirect_on_close'] = context['request'].current_page.get_absolute_url(language)
            else:
                extra_context['redirect_on_close'] = ''
        return extra_context

    def _get_content(self, context, instance, attribute, language, filters):
        extra_context = copy(context)
        attr_value = None
        if hasattr(instance, 'lazy_translation_getter'):
            attr_value = instance.lazy_translation_getter(attribute, '')
        if not attr_value:
            attr_value = getattr(instance, attribute, '')
        extra_context['content'] = attr_value
        if callable(extra_context['content']):
            if isinstance(instance, Page):
                extra_context['content'] = extra_context['content'](language)
            else:
                extra_context['content'] = extra_context['content'](context['request'])
        if filters:
            expression = self.parser.compile_filter("content|%s" % (filters))


## ... source file continues with no further urlencode examples...

```


## Example 3 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / tools.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/tools.py)

```python
# tools.py
from __future__ import absolute_import, unicode_literals

from django.contrib.admin.options import IS_POPUP_VAR
from django.core.exceptions import PermissionDenied
~~from django.utils.http import urlencode


ALLOWED_PICK_TYPES = ('folder', 'file')


def check_files_edit_permissions(request, files):
    for f in files:
        if not f.has_edit_permission(request):
            raise PermissionDenied


def check_folder_edit_permissions(request, folders):
    for f in folders:
        if not f.has_edit_permission(request):
            raise PermissionDenied
        check_files_edit_permissions(request, f.files)
        check_folder_edit_permissions(request, f.children.all())


def check_files_read_permissions(request, files):
    for f in files:
        if not f.has_read_permission(request):
            raise PermissionDenied



## ... source file abbreviated to get to urlencode examples ...


        IS_POPUP_VAR in request.GET
        or 'pop' in request.GET
        or IS_POPUP_VAR in request.POST
        or 'pop' in request.POST
    )


def popup_pick_type(request):
    pick_type = request.GET.get('_pick', request.POST.get('_pick'))
    if pick_type in ALLOWED_PICK_TYPES:
        return pick_type
    return None


def admin_url_params(request, params=None):
    params = params or {}
    if popup_status(request):
        params[IS_POPUP_VAR] = '1'
    pick_type = popup_pick_type(request)
    if pick_type:
        params['_pick'] = pick_type
    return params


def admin_url_params_encoded(request, first_separator='?', params=None):
~~    params = urlencode(
        sorted(admin_url_params(request, params=params).items())
    )
    if not params:
        return ''
    return '{0}{1}'.format(first_separator, params)


class AdminContext(dict):
    def __init__(self, request):
        super(AdminContext, self).__init__()
        self.update(admin_url_params(request))

    def __missing__(self, key):
        if key == 'popup':
            return self.get(IS_POPUP_VAR, False) == '1'
        elif key == 'pick':
            return self.get('_pick', '')
        elif key.startswith('pick_'):
            return self.get('_pick', '') == key.split('pick_')[1]

    def __getattr__(self, name):
        if name in ('popup', 'pick') or name.startswith('pick_'):
            return self.get(name)
        raise AttributeError


## ... source file continues with no further urlencode examples...

```


## Example 4 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / widgets.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./widgets.py)

```python
# widgets.py
from collections.abc import Iterable
from copy import deepcopy
from itertools import chain
from re import search, sub

from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms.utils import flatatt
from django.utils.datastructures import MultiValueDict
from django.utils.encoding import force_str
~~from django.utils.http import urlencode
from django.utils.safestring import mark_safe
from django.utils.translation import gettext as _


class LinkWidget(forms.Widget):
    def __init__(self, attrs=None, choices=()):
        super().__init__(attrs)

        self.choices = choices

    def value_from_datadict(self, data, files, name):
        value = super().value_from_datadict(data, files, name)
        self.data = data
        return value

    def render(self, name, value, attrs=None, choices=(), renderer=None):
        if not hasattr(self, 'data'):
            self.data = {}
        if value is None:
            value = ''
        final_attrs = self.build_attrs(self.attrs, extra_attrs=attrs)
        output = ['<ul%s>' % flatatt(final_attrs)]
        options = self.render_options(choices, [value], name)
        if options:


## ... source file abbreviated to get to urlencode examples ...


    def render_options(self, choices, selected_choices, name):
        selected_choices = set(force_str(v) for v in selected_choices)
        output = []
        for option_value, option_label in chain(self.choices, choices):
            if isinstance(option_label, (list, tuple)):
                for option in option_label:
                    output.append(
                        self.render_option(name, selected_choices, *option))
            else:
                output.append(
                    self.render_option(name, selected_choices,
                                       option_value, option_label))
        return '\n'.join(output)

    def render_option(self, name, selected_choices,
                      option_value, option_label):
        option_value = force_str(option_value)
        if option_label == BLANK_CHOICE_DASH[0][1]:
            option_label = _("All")
        data = self.data.copy()
        data[name] = option_value
        selected = data == self.data or option_value in selected_choices
        try:
            url = data.urlencode()
        except AttributeError:
~~            url = urlencode(data)
        return self.option_string() % {
            'attrs': selected and ' class="selected"' or '',
            'query_string': url,
            'label': force_str(option_label)
        }

    def option_string(self):
        return '<li><a%(attrs)s href="?%(query_string)s">%(label)s</a></li>'


class SuffixedMultiWidget(forms.MultiWidget):
    suffixes = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        assert len(self.widgets) == len(self.suffixes)
        assert len(self.suffixes) == len(set(self.suffixes))

    def suffixed(self, name, suffix):
        return '_'.join([name, suffix]) if suffix else name

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)


## ... source file continues with no further urlencode examples...

```


## Example 5 from django-rest-framework
[Django REST Framework](https://github.com/encode/django-rest-framework)
([project homepage and documentation](https://www.django-rest-framework.org/),
[PyPI package information](https://pypi.org/project/djangorestframework/)
and [more resources on Full Stack Python](/django-rest-framework-drf.html)),
often abbreviated as "DRF", is a popular [Django](/django.html) extension
for building [web APIs](/application-programming-interfaces.html).
The project has fantastic documentation and a wonderful
[quickstart](https://www.django-rest-framework.org/tutorial/quickstart/)
that serve as examples of how to make it easier for newcomers
to get started.

The project is open sourced under the
[Encode OSS Ltd. license](https://github.com/encode/django-rest-framework/blob/master/LICENSE.md).

[**django-rest-framework / rest_framework / test.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./test.py)

```python
# test.py
import io
from importlib import import_module

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.handlers.wsgi import WSGIHandler
from django.test import override_settings, testcases
from django.test.client import Client as DjangoClient
from django.test.client import ClientHandler
from django.test.client import RequestFactory as DjangoRequestFactory
from django.utils.encoding import force_bytes
~~from django.utils.http import urlencode

from rest_framework.compat import coreapi, requests
from rest_framework.settings import api_settings


def force_authenticate(request, user=None, token=None):
    request._force_auth_user = user
    request._force_auth_token = token


if requests is not None:
    class HeaderDict(requests.packages.urllib3._collections.HTTPHeaderDict):
        def get_all(self, key, default):
            return self.getheaders(key)

    class MockOriginalResponse:
        def __init__(self, headers):
            self.msg = HeaderDict(headers)
            self.closed = False

        def isclosed(self):
            return self.closed

        def close(self):


## ... source file abbreviated to get to urlencode examples ...


            format = format or self.default_format

            assert format in self.renderer_classes, (
                "Invalid format '{}'. Available formats are {}. "
                "Set TEST_REQUEST_RENDERER_CLASSES to enable "
                "extra request formats.".format(
                    format,
                    ', '.join(["'" + fmt + "'" for fmt in self.renderer_classes])
                )
            )

            renderer = self.renderer_classes[format]()
            ret = renderer.render(data)

            content_type = "{}; charset={}".format(
                renderer.media_type, renderer.charset
            )

            if isinstance(ret, str):
                ret = ret.encode(renderer.charset)

        return ret, content_type

    def get(self, path, data=None, **extra):
        r = {
~~            'QUERY_STRING': urlencode(data or {}, doseq=True),
        }
        if not data and '?' in path:
            query_string = force_bytes(path.split('?')[1])
            query_string = query_string.decode('iso-8859-1')
            r['QUERY_STRING'] = query_string
        r.update(extra)
        return self.generic('GET', path, **r)

    def post(self, path, data=None, format=None, content_type=None, **extra):
        data, content_type = self._encode_data(data, format, content_type)
        return self.generic('POST', path, data, content_type, **extra)

    def put(self, path, data=None, format=None, content_type=None, **extra):
        data, content_type = self._encode_data(data, format, content_type)
        return self.generic('PUT', path, data, content_type, **extra)

    def patch(self, path, data=None, format=None, content_type=None, **extra):
        data, content_type = self._encode_data(data, format, content_type)
        return self.generic('PATCH', path, data, content_type, **extra)

    def delete(self, path, data=None, format=None, content_type=None, **extra):
        data, content_type = self._encode_data(data, format, content_type)
        return self.generic('DELETE', path, data, content_type, **extra)



## ... source file continues with no further urlencode examples...

```


## Example 6 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / templatetags / django_tables2.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/templatetags/django_tables2.py)

```python
# django_tables2.py
import re
from collections import OrderedDict

from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template import Node, TemplateSyntaxError
from django.template.loader import get_template, select_template
from django.templatetags.l10n import register as l10n_register
from django.utils.html import escape
~~from django.utils.http import urlencode

import django_tables2 as tables
from django_tables2.paginators import LazyPaginator
from django_tables2.utils import AttributeDict

register = template.Library()
kwarg_re = re.compile(r"(?:(.+)=)?(.+)")
context_processor_error_msg = (
    "Tag {%% %s %%} requires django.template.context_processors.request to be "
    "in the template configuration in "
    "settings.TEMPLATES[]OPTIONS.context_processors) in order for the included "
    "template tags to function correctly."
)


def token_kwargs(bits, parser):
    if not bits:
        return {}
    kwargs = OrderedDict()
    while bits:
        match = kwarg_re.match(bits[0])
        if not match or not match.group(1):
            return kwargs
        key, value = match.groups()


## ... source file abbreviated to get to urlencode examples ...




class QuerystringNode(Node):
    def __init__(self, updates, removals, asvar=None):
        super().__init__()
        self.updates = updates
        self.removals = removals
        self.asvar = asvar

    def render(self, context):
        if "request" not in context:
            raise ImproperlyConfigured(context_processor_error_msg % "querystring")

        params = dict(context["request"].GET)
        for key, value in self.updates.items():
            if isinstance(key, str):
                params[key] = value
                continue
            key = key.resolve(context)
            value = value.resolve(context)
            if key not in ("", None):
                params[key] = value
        for removal in self.removals:
            params.pop(removal.resolve(context), None)

~~        value = escape("?" + urlencode(params, doseq=True))

        if self.asvar:
            context[str(self.asvar)] = value
            return ""
        else:
            return value


@register.tag
def querystring(parser, token):
    bits = token.split_contents()
    tag = bits.pop(0)
    updates = token_kwargs(bits, parser)

    asvar_key = None
    for key in updates:
        if str(key) == "as":
            asvar_key = key

    if asvar_key is not None:
        asvar = updates[asvar_key]
        del updates[asvar_key]
    else:
        asvar = None


## ... source file continues with no further urlencode examples...

```


## Example 7 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / users / utils.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/users/utils.py)

```python
# utils.py
import hashlib
from django.conf import settings
~~from django.utils.http import urlencode

from wagtail.core.compat import AUTH_USER_APP_LABEL, AUTH_USER_MODEL_NAME

delete_user_perm = "{0}.delete_{1}".format(AUTH_USER_APP_LABEL, AUTH_USER_MODEL_NAME.lower())


def user_can_delete_user(current_user, user_to_delete):
    if not current_user.has_perm(delete_user_perm):
        return False

    if current_user == user_to_delete:
        return False

    if user_to_delete.is_superuser and not current_user.is_superuser:
        return False

    return True


def get_gravatar_url(email, size=50):
    default = "mm"
    size = int(size) * 2  # requested at retina size by default and scaled down at point of use with css
    gravatar_provider_url = getattr(settings, 'WAGTAIL_GRAVATAR_PROVIDER_URL', '//www.gravatar.com/avatar')

    if (not email) or (gravatar_provider_url is None):
        return None

    gravatar_url = "{gravatar_provider_url}/{hash}?{params}".format(
        gravatar_provider_url=gravatar_provider_url.rstrip('/'),
        hash=hashlib.md5(email.lower().encode('utf-8')).hexdigest(),
~~        params=urlencode({'s': size, 'd': default})
    )

    return gravatar_url



## ... source file continues with no further urlencode examples...

```

