title: django.urls resolve Example Code
category: page
slug: django-urls-resolve-examples
sortorder: 500011410
toc: False
sidebartitle: django.urls resolve
meta: Python example code for the resolve callable from the django.urls module of the Django project.


resolve is a callable within the django.urls module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / core / urlresolvers.py**](https://github.com/jrief/django-angular/blob/master/djng/core/urlresolvers.py)

```python
# urlresolvers.py
from inspect import isclass

~~from django.urls import (get_resolver, get_urlconf, resolve, reverse, NoReverseMatch)
from django.core.exceptions import ImproperlyConfigured

try:
    from django.utils.module_loading import import_string
except ImportError:
    from django.utils.module_loading import import_by_path as import_string

from djng.views.mixins import JSONResponseMixin


def _get_remote_methods_for(view_object, url):
    result = {}
    for field in dir(view_object):
        member = getattr(view_object, field, None)
        if callable(member) and hasattr(member, 'allow_rmi'):
            config = {
                'url': url,
                'method': getattr(member, 'allow_rmi'),
                'headers': {'DjNg-Remote-Method': field},
            }
            result.update({field: config})
    return result


def get_all_remote_methods(resolver=None, ns_prefix=''):
    if not resolver:
        resolver = get_resolver(get_urlconf())
    result = {}
    for name in resolver.reverse_dict.keys():
        if not isinstance(name, str):
            continue
        try:
            url = reverse(ns_prefix + name)
~~            resmgr = resolve(url)
            ViewClass = import_string('{0}.{1}'.format(resmgr.func.__module__, resmgr.func.__name__))
            if isclass(ViewClass) and issubclass(ViewClass, JSONResponseMixin):
                result[name] = _get_remote_methods_for(ViewClass, url)
        except (NoReverseMatch, ImproperlyConfigured):
            pass
    for namespace, ns_pattern in resolver.namespace_dict.items():
        sub_res = get_all_remote_methods(ns_pattern[1], ns_prefix + namespace + ':')
        if sub_res:
            result[namespace] = sub_res
    return result


def get_current_remote_methods(view):
    if isinstance(view, JSONResponseMixin):
        return _get_remote_methods_for(view, view.request.path_info)



## ... source file continues with no further resolve examples...

```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / page_rendering.py**](https://github.com/divio/django-cms/blob/develop/cms/./page_rendering.py)

```python
# page_rendering.py
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template.response import TemplateResponse
~~from django.urls import Resolver404, resolve, reverse

from cms import __version__
from cms.cache.page import set_page_cache
from cms.models import Page
from cms.utils.conf import get_cms_setting
from cms.utils.page import get_page_template_from_request
from cms.utils.page_permissions import user_can_change_page, user_can_view_page


def render_page(request, page, current_language, slug):
    context = {}
    context['lang'] = current_language
    context['current_page'] = page
    context['has_change_permissions'] = user_can_change_page(request.user, page)
    context['has_view_permissions'] = user_can_view_page(request.user, page)

    if not context['has_view_permissions']:
        return _handle_no_page(request)

    template = get_page_template_from_request(request)
    response = TemplateResponse(request, template, context)
    response.add_post_render_callback(set_page_cache)

    xframe_options = page.get_xframe_options()
    if xframe_options == Page.X_FRAME_OPTIONS_INHERIT or xframe_options is None:
        return response

    response.xframe_options_exempt = True

    if xframe_options == Page.X_FRAME_OPTIONS_ALLOW:
        return response
    elif xframe_options == Page.X_FRAME_OPTIONS_SAMEORIGIN:
        response['X-Frame-Options'] = 'SAMEORIGIN'
    elif xframe_options == Page.X_FRAME_OPTIONS_DENY:
        response['X-Frame-Options'] = 'DENY'
    return response


def render_object_structure(request, obj):
    context = {
        'object': obj,
        'cms_toolbar': request.toolbar,
    }
    return render(request, 'cms/toolbar/structure.html', context)


def _handle_no_page(request):
    try:
~~        resolve('%s$' % request.path)
    except Resolver404 as e:
        exc = Http404(dict(path=request.path, tried=e.args[0]['tried']))
        raise exc
    raise Http404('CMS Page not found: %s' % request.path)


def _render_welcome_page(request):
    context = {
        'cms_version': __version__,
        'cms_edit_on': get_cms_setting('CMS_TOOLBAR_URL__EDIT_ON'),
        'django_debug': settings.DEBUG,
        'next_url': reverse('pages-root'),
    }
    return TemplateResponse(request, "cms/welcome.html", context)



## ... source file continues with no further resolve examples...

```


## Example 3 from django-debug-toolbar
[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
([project documentation](https://github.com/jazzband/django-debug-toolbar)
and [PyPI page](https://pypi.org/project/django-debug-toolbar/))
grants a developer detailed request-response cycle information while
developing a [Django](/django.html) web application.
The code for django-debug-toolbar is
[open source](https://github.com/jazzband/django-debug-toolbar/blob/master/LICENSE)
and maintained by the developer community group known as
[Jazzband](https://jazzband.co/).

[**django-debug-toolbar / debug_toolbar / panels / request.py**](https://github.com/jazzband/django-debug-toolbar/blob/master/debug_toolbar/panels/request.py)

```python
# request.py
from django.http import Http404
~~from django.urls import resolve
from django.utils.translation import gettext_lazy as _

from debug_toolbar.panels import Panel
from debug_toolbar.utils import get_name_from_obj


class RequestPanel(Panel):

    template = "debug_toolbar/panels/request.html"

    title = _("Request")

    @property
    def nav_subtitle(self):
        view_func = self.get_stats().get("view_func", "")
        return view_func.rsplit(".", 1)[-1]

    def generate_stats(self, request, response):
        self.record_stats(
            {
                "get": [(k, request.GET.getlist(k)) for k in sorted(request.GET)],
                "post": [(k, request.POST.getlist(k)) for k in sorted(request.POST)],
                "cookies": [
                    (k, request.COOKIES.get(k)) for k in sorted(request.COOKIES)
                ],
            }
        )
        view_info = {
            "view_func": _("<no view>"),
            "view_args": "None",
            "view_kwargs": "None",
            "view_urlname": "None",
        }
        try:
~~            match = resolve(request.path)
            func, args, kwargs = match
            view_info["view_func"] = get_name_from_obj(func)
            view_info["view_args"] = args
            view_info["view_kwargs"] = kwargs
            view_info["view_urlname"] = getattr(match, "url_name", _("<unavailable>"))
        except Http404:
            pass
        self.record_stats(view_info)

        if hasattr(request, "session"):
            self.record_stats(
                {
                    "session": [
                        (k, request.session.get(k))
                        for k in sorted(request.session.keys())
                    ]
                }
            )



## ... source file continues with no further resolve examples...

```


## Example 4 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / utils.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/./utils.py)

```python
# utils.py
import datetime
import json
from django.template import Context
from django.utils import translation
from jet import settings
from jet.models import PinnedApplication

try:
    from django.apps.registry import apps
except ImportError:
    try:
        from django.apps import apps # Fix Django 1.7 import issue
    except ImportError:
        pass
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
try:
    from django.core.urlresolvers import reverse, resolve, NoReverseMatch
except ImportError: # Django 1.11
~~    from django.urls import reverse, resolve, NoReverseMatch

from django.contrib.admin import AdminSite
from django.utils.encoding import smart_text
from django.utils.text import capfirst
from django.contrib import messages
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.contrib.admin.options import IncorrectLookupParameters
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict  # Python 2.6


class JsonResponse(HttpResponse):

    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, **kwargs):
        if safe and not isinstance(data, dict):
            raise TypeError('In order to allow non-dict objects to be '
                'serialized set the safe parameter to False')


## ... source file abbreviated to get to resolve examples ...


                    app_dict[app_label] = {
                        'name': name,
                        'app_label': app_label,
                        'app_url': reverse(
                            'admin:app_list',
                            kwargs={'app_label': app_label},
                            current_app=admin_site.name,
                        ),
                        'has_module_perms': has_module_perms,
                        'models': [model_dict],
                    }

    app_list = list(app_dict.values())

    if order:
        app_list.sort(key=lambda x: x['name'].lower())

        for app in app_list:
            app['models'].sort(key=lambda x: x['name'])

    return app_list


def get_admin_site(context):
    try:
~~        current_resolver = resolve(context.get('request').path)
~~        index_resolver = resolve(reverse('%s:index' % current_resolver.namespaces[0]))

        if hasattr(index_resolver.func, 'admin_site'):
            return index_resolver.func.admin_site

        for func_closure in index_resolver.func.__closure__:
            if isinstance(func_closure.cell_contents, AdminSite):
                return func_closure.cell_contents
    except:
        pass

    return admin.site


def get_admin_site_name(context):
    return get_admin_site(context).name


class LazyDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime) or isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, Promise):
            return force_text(obj)
        return self.encode(obj)


## ... source file continues with no further resolve examples...

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

[**django-rest-framework / rest_framework / relations.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./relations.py)

```python
# relations.py
import sys
from collections import OrderedDict
from urllib import parse

from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist
from django.db.models import Manager
from django.db.models.query import QuerySet
~~from django.urls import NoReverseMatch, Resolver404, get_script_prefix, resolve
from django.utils.encoding import smart_str, uri_to_iri
from django.utils.translation import gettext_lazy as _

from rest_framework.fields import (
    Field, empty, get_attribute, is_simple_callable, iter_options
)
from rest_framework.reverse import reverse
from rest_framework.settings import api_settings
from rest_framework.utils import html


def method_overridden(method_name, klass, instance):
    method = getattr(klass, method_name)
    default_method = getattr(method, '__func__', method)  # Python 3 compat
    return default_method is not getattr(instance, method_name).__func__


class ObjectValueError(ValueError):


class ObjectTypeError(TypeError):


class Hyperlink(str):


## ... source file abbreviated to get to resolve examples ...



    def get_url(self, obj, view_name, request, format):
        if hasattr(obj, 'pk') and obj.pk in (None, ''):
            return None

        lookup_value = getattr(obj, self.lookup_field)
        kwargs = {self.lookup_url_kwarg: lookup_value}
        return self.reverse(view_name, kwargs=kwargs, request=request, format=format)

    def to_internal_value(self, data):
        request = self.context.get('request', None)
        try:
            http_prefix = data.startswith(('http:', 'https:'))
        except AttributeError:
            self.fail('incorrect_type', data_type=type(data).__name__)

        if http_prefix:
            data = parse.urlparse(data).path
            prefix = get_script_prefix()
            if data.startswith(prefix):
                data = '/' + data[len(prefix):]

        data = uri_to_iri(parse.unquote(data))

        try:
~~            match = resolve(data)
        except Resolver404:
            self.fail('no_match')

        try:
            expected_viewname = request.versioning_scheme.get_versioned_viewname(
                self.view_name, request
            )
        except AttributeError:
            expected_viewname = self.view_name

        if match.view_name != expected_viewname:
            self.fail('incorrect_match')

        try:
            return self.get_object(match.view_name, match.args, match.kwargs)
        except (ObjectDoesNotExist, ObjectValueError, ObjectTypeError):
            self.fail('does_not_exist')

    def to_representation(self, value):
        assert 'request' in self.context, (
            "`%s` requires the request in the serializer"
            " context. Add `context={'request': request}` when instantiating "
            "the serializer." % self.__class__.__name__
        )


## ... source file continues with no further resolve examples...

```


## Example 6 from django-wiki
[django-wiki](https://github.com/django-wiki/django-wiki)
([project documentation](https://django-wiki.readthedocs.io/en/master/),
[demo](https://demo.django-wiki.org/),
and [PyPI page](https://pypi.org/project/django-wiki/))
is a wiki system code library for [Django](/django.html)
projects that makes it easier to create user-editable content.
The project aims to provide necessary core features and then
have an easy plugin format for additional features, rather than
having every exhaustive feature built into the core system.
django-wiki is a rewrite of an earlier now-defunct project
named [django-simplewiki](https://code.google.com/p/django-simple-wiki/).

The code for django-wiki is provided as open source under the
[GNU General Public License 3.0](https://github.com/django-wiki/django-wiki/blob/master/COPYING).

[**django-wiki / src/wiki / forms.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/./forms.py)

```python
# forms.py
    "UserCreationForm",
    "UserUpdateForm",
    "WikiSlugField",
    "SpamProtectionMixin",
    "CreateRootForm",
    "MoveForm",
    "EditForm",
    "SelectWidgetBootstrap",
    "TextInputPrepend",
    "CreateForm",
    "DeleteForm",
    "PermissionsForm",
    "DirFilterForm",
    "SearchForm",
]

from datetime import timedelta

from django import forms
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core import validators
from django.core.validators import RegexValidator
from django.forms.widgets import HiddenInput
from django.shortcuts import get_object_or_404
~~from django.urls import Resolver404, resolve
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext, gettext_lazy as _, pgettext_lazy
from wiki import models
from wiki.conf import settings
from wiki.core import permissions
from wiki.core.diff import simple_merge
from wiki.core.plugins.base import PluginSettingsFormMixin
from wiki.editors import getEditor

from .forms_account_handling import UserCreationForm, UserUpdateForm

validate_slug_numbers = RegexValidator(
    r"^[0-9]+$",
    _("A 'slug' cannot consist solely of numbers."),
    "invalid",
    inverse_match=True,
)


class WikiSlugField(forms.CharField):

    default_validators = [validators.validate_slug, validate_slug_numbers]



## ... source file abbreviated to get to resolve examples ...


        raise forms.ValidationError(gettext("A slug may not begin with an underscore."))
    if slug == "admin":
        raise forms.ValidationError(gettext("'admin' is not a permitted slug name."))

    if settings.URL_CASE_SENSITIVE:
        already_existing_slug = models.URLPath.objects.filter(slug=slug, parent=urlpath)
    else:
        slug = slug.lower()
        already_existing_slug = models.URLPath.objects.filter(
            slug__iexact=slug, parent=urlpath
        )
    if already_existing_slug:
        already_urlpath = already_existing_slug[0]
        if already_urlpath.article and already_urlpath.article.current_revision.deleted:
            raise forms.ValidationError(
                gettext('A deleted article with slug "%s" already exists.')
                % already_urlpath.slug
            )
        else:
            raise forms.ValidationError(
                gettext('A slug named "%s" already exists.') % already_urlpath.slug
            )

    if settings.CHECK_SLUG_URL_AVAILABLE:
        try:
~~            match = resolve(urlpath.path + "/" + slug + "/")
            if match.app_name != "wiki":
                raise forms.ValidationError(
                    gettext("This slug conflicts with an existing URL.")
                )
        except Resolver404:
            pass

    return slug


User = get_user_model()
Group = apps.get_model(settings.GROUP_MODEL)


class SpamProtectionMixin:


    revision_model = models.ArticleRevision

    def check_spam(self):  # noqa
        request = self.request
        user = None
        ip_address = None
        if request.user.is_authenticated:


## ... source file continues with no further resolve examples...

```

