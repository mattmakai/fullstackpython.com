title: django.utils.html escape Example Code
category: page
slug: django-utils-html-escape-examples
sortorder: 500011462
toc: False
sidebartitle: django.utils.html escape
meta: Python example code for the escape callable from the django.utils.html module of the Django project.


escape is a callable within the django.utils.html module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / forms / angular_base.py**](https://github.com/jrief/django-angular/blob/master/djng/forms/angular_base.py)

```python
# angular_base.py
from base64 import b64encode
from collections import UserList
import json
import warnings

from django.forms import forms
from django.http import QueryDict
~~from django.utils.html import format_html, format_html_join, escape, conditional_escape
from django.utils.encoding import force_text
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe, SafeText, SafeData
from django.core.exceptions import ValidationError, ImproperlyConfigured

from .fields import DefaultFieldMixin


class SafeTuple(SafeData, tuple):


class TupleErrorList(UserList, list):
    def __init__(self, initlist=None, error_class=None):
        super(TupleErrorList, self).__init__(initlist)

        if error_class is None:
            self.error_class = 'errorlist'
        else:
            self.error_class = 'errorlist {}'.format(error_class)

    def as_data(self):
        return ValidationError(self.data).error_list

    def get_json_data(self, escape_html=False):
        errors = []
        for error in self.as_data():
            message = list(error)[0]
            errors.append({
~~                'message': escape(message) if escape_html else message,
                'code': error.code or '',
            })
        return errors

    def as_json(self, escape_html=False):
        return json.dumps(self.get_json_data(escape_html))

    def extend(self, iterable):
        for item in iterable:
            if not isinstance(item, str):
                self.append(item)
        return None

    def as_ul(self):
        if not self:
            return SafeText()
        first = self[0]
        if isinstance(first, tuple):
            error_lists = {'$pristine': [], '$dirty': []}
            for e in self:
                if e[5] == '$message':
                    li_format = '<li ng-show="{0}.{1} && {0}.{3}" class="{2}" ng-bind="{0}.{3}"></li>'
                else:
                    li_format = '<li ng-show="{0}.{1}" class="{2}">{3}</li>'


## ... source file continues with no further escape examples...

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
~~from django.utils.html import escape
from django.utils.http import urlencode
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


## ... source file abbreviated to get to escape examples ...


        'as',
        Argument('varname', required=False, resolve=False)
    )

    valid_attributes = [
        "title",
        "slug",
        "meta_description",
        "page_title",
        "menu_title",
        "changed_date",
        "changed_by",
    ]

    def get_value(self, context, name, page_lookup):
        if not 'request' in context:
            return ''
        name = name.lower()
        request = context['request']
        lang = get_language_from_request(request)
        page = _get_page_by_untyped_arg(page_lookup, request, get_site_id(None))
        if page and name in self.valid_attributes:
            func = getattr(page, "get_%s" % name)
            ret_val = func(language=lang, fallback=True)
            if not isinstance(ret_val, datetime):
~~                ret_val = escape(ret_val)
            return ret_val
        return ''


class CMSToolbar(RenderBlock):
    name = 'cms_toolbar'

    options = Options(
        Argument('name', required=False),  # just here so sekizai thinks this is a RenderBlock
        parser_class=SekizaiParser,
    )

    def render_tag(self, context, name, nodelist):
        request = context.get('request')

        if not request:
            return nodelist.render(context)

        toolbar = get_toolbar_from_request(request)

        if toolbar and toolbar.show_toolbar:
            toolbar.init_toolbar(request)
            return toolbar.render_with_structure(context, nodelist)
        return nodelist.render(context)


## ... source file continues with no further escape examples...

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

[**django-debug-toolbar / debug_toolbar / views.py**](https://github.com/jazzband/django-debug-toolbar/blob/master/debug_toolbar/./views.py)

```python
# views.py
from django.http import JsonResponse
~~from django.utils.html import escape
from django.utils.translation import gettext as _

from debug_toolbar.decorators import require_show_toolbar
from debug_toolbar.toolbar import DebugToolbar


@require_show_toolbar
def render_panel(request):
    toolbar = DebugToolbar.fetch(request.GET["store_id"])
    if toolbar is None:
        content = _(
            "Data for this panel isn't available anymore. "
            "Please reload the page and retry."
        )
~~        content = "<p>%s</p>" % escape(content)
        scripts = []
    else:
        panel = toolbar.get_panel_by_id(request.GET["panel_id"])
        content = panel.content
        scripts = panel.scripts
    return JsonResponse({"content": content, "scripts": scripts})



## ... source file continues with no further escape examples...

```


## Example 4 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / admin / folderadmin.py**](https://github.com/divio/django-filer/blob/develop/filer/admin/folderadmin.py)

```python
# folderadmin.py
from __future__ import absolute_import, division, unicode_literals

import itertools
import os
import re
from collections import OrderedDict

from django import forms
from django.conf import settings as django_settings
from django.conf.urls import url
from django.contrib import messages
from django.contrib.admin import helpers
from django.contrib.admin.utils import capfirst, quote, unquote
from django.core.exceptions import PermissionDenied, ValidationError
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db import models, router
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils.encoding import force_text
~~from django.utils.html import escape
from django.utils.http import urlquote, urlunquote
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy, ungettext

from .. import settings
from ..models import (
    File, Folder, FolderPermission, FolderRoot, ImagesWithMissingData,
    UnsortedImages, tools,
)
from ..settings import FILER_IMAGE_MODEL, FILER_PAGINATE_BY
from ..thumbnail_processors import normalize_subject_location
from ..utils.compatibility import get_delete_permission
from ..utils.filer_easy_thumbnails import FilerActionThumbnailer
from ..utils.loader import load_model
from . import views
from .forms import CopyFilesAndFoldersForm, RenameFilesForm, ResizeImagesForm
from .patched.admin_utils import get_deleted_objects
from .permissions import PrimitivePermissionAwareModelAdmin
from .tools import (
    AdminContext, admin_url_params_encoded, check_files_edit_permissions,
    check_files_read_permissions, check_folder_edit_permissions,
    check_folder_read_permissions, popup_status, userperms_for_request,
)


## ... source file abbreviated to get to escape examples ...



        return render(
            request,
            "admin/filer/delete_selected_files_confirmation.html",
            context
        )

    delete_files_or_folders.short_description = ugettext_lazy(
        "Delete selected files and/or folders")

    def _format_callback(self, obj, user, admin_site, perms_needed):
        has_admin = obj.__class__ in admin_site._registry
        opts = obj._meta
        if has_admin:
            admin_url = reverse('%s:%s_%s_change'
                                % (admin_site.name,
                                   opts.app_label,
                                   opts.object_name.lower()),
                                None, (quote(obj._get_pk_val()),))
            p = get_delete_permission(opts)
            if not user.has_perm(p):
                perms_needed.add(opts.verbose_name)
            return mark_safe('%s: <a href="%s">%s</a>' %
                             (escape(capfirst(opts.verbose_name)),
                              admin_url,
~~                              escape(obj)))
        else:
            return '%s: %s' % (capfirst(opts.verbose_name), force_text(obj))

    def _check_copy_perms(self, request, files_queryset, folders_queryset):
        try:
            check_files_read_permissions(request, files_queryset)
            check_folder_read_permissions(request, folders_queryset)
        except PermissionDenied:
            return True
        return False

    def _check_move_perms(self, request, files_queryset, folders_queryset):
        try:
            check_files_read_permissions(request, files_queryset)
            check_folder_read_permissions(request, folders_queryset)
            check_files_edit_permissions(request, files_queryset)
            check_folder_edit_permissions(request, folders_queryset)
        except PermissionDenied:
            return True
        return False

    def _get_current_action_folder(self, request, files_queryset,
                                   folders_queryset):
        if files_queryset:


## ... source file continues with no further escape examples...

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

[**django-rest-framework / rest_framework / templatetags / rest_framework.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/templatetags/rest_framework.py)

```python
# rest_framework.py
import re
from collections import OrderedDict

from django import template
from django.template import loader
from django.urls import NoReverseMatch, reverse
from django.utils.encoding import force_str, iri_to_uri
~~from django.utils.html import escape, format_html, smart_urlquote
from django.utils.safestring import SafeData, mark_safe

from rest_framework.compat import apply_markdown, pygments_highlight
from rest_framework.renderers import HTMLFormRenderer
from rest_framework.utils.urls import replace_query_param

register = template.Library()

class_re = re.compile(r'(?<=class=["\'])(.*)(?=["\'])')


@register.tag(name='code')
def highlight_code(parser, token):
    code = token.split_contents()[-1]
    nodelist = parser.parse(('endcode',))
    parser.delete_first_token()
    return CodeNode(code, nodelist)


class CodeNode(template.Node):
    style = 'emacs'

    def __init__(self, lang, code):
        self.lang = lang


## ... source file abbreviated to get to escape examples ...


def optional_logout(request, user):
    try:
        logout_url = reverse('rest_framework:logout')
    except NoReverseMatch:
~~        snippet = format_html('<li class="navbar-text">{user}</li>', user=escape(user))
        return mark_safe(snippet)

    snippet = """<li class="dropdown">
        <a href="#" class="dropdown-toggle" data-toggle="dropdown">
            {user}
            <b class="caret"></b>
        </a>
        <ul class="dropdown-menu">
            <li><a href='{href}?next={next}'>Log out</a></li>
        </ul>
    </li>"""
~~    snippet = format_html(snippet, user=escape(user), href=logout_url, next=escape(request.path))

    return mark_safe(snippet)


@register.simple_tag
def add_query_param(request, key, val):
    iri = request.get_full_path()
    uri = iri_to_uri(iri)
~~    return escape(replace_query_param(uri, key, val))


@register.filter
def as_string(value):
    if value is None:
        return ''
    return '%s' % value


@register.filter
def as_list_of_strings(value):
    return [
        '' if (item is None) else ('%s' % item)
        for item in value
    ]


@register.filter
def add_class(value, css_class):
    html = str(value)
    match = class_re.search(html)
    if match:
        m = re.search(r'^%s$|^%s\s|\s%s\s|\s%s$' % (css_class, css_class,
                                                    css_class, css_class),
                      match.group(1))
        if not m:
            return mark_safe(class_re.sub(match.group(1) + " " + css_class,
                                          html))
    else:
        return mark_safe(html.replace('>', ' class="%s">' % css_class, 1))
    return value


@register.filter
def format_value(value):
    if getattr(value, 'is_hyperlink', False):
        name = str(value.obj)
~~        return mark_safe('<a href=%s>%s</a>' % (value, escape(name)))
    if value is None or isinstance(value, bool):
        return mark_safe('<code>%s</code>' % {True: 'true', False: 'false', None: 'null'}[value])
    elif isinstance(value, list):
        if any([isinstance(item, (list, dict)) for item in value]):
            template = loader.get_template('rest_framework/admin/list_value.html')
        else:
            template = loader.get_template('rest_framework/admin/simple_list_value.html')
        context = {'value': value}
        return template.render(context)
    elif isinstance(value, dict):
        template = loader.get_template('rest_framework/admin/dict_value.html')
        context = {'value': value}
        return template.render(context)
    elif isinstance(value, str):
        if (
            (value.startswith('http:') or value.startswith('https:')) and not
            re.search(r'\s', value)
        ):
~~            return mark_safe('<a href="{value}">{value}</a>'.format(value=escape(value)))
        elif '@' in value and not re.search(r'\s', value):
~~            return mark_safe('<a href="mailto:{value}">{value}</a>'.format(value=escape(value)))
        elif '\n' in value:
~~            return mark_safe('<pre>%s</pre>' % escape(value))
    return str(value)


@register.filter
def items(value):
    if value is None:
        return []
    return value.items()


@register.filter
def data(value):
    return value.data


@register.filter
def schema_links(section, sec_key=None):
    NESTED_FORMAT = '%s > %s'  # this format is used in docs/js/api.js:normalizeKeys
    links = section.links
    if section.data:
        data = section.data.items()
        for sub_section_key, sub_section in data:
            new_links = schema_links(sub_section, sec_key=sub_section_key)
            links.update(new_links)


## ... source file abbreviated to get to escape examples ...



TRAILING_PUNCTUATION = ['.', ',', ':', ';', '.)', '"', "']", "'}", "'"]
WRAPPING_PUNCTUATION = [('(', ')'), ('<', '>'), ('[', ']'), ('&lt;', '&gt;'),
                        ('"', '"'), ("'", "'")]
word_split_re = re.compile(r'(\s+)')
simple_url_re = re.compile(r'^https?://\[?\w', re.IGNORECASE)
simple_url_2_re = re.compile(r'^www\.|^(?!http)\w[^@]+\.(com|edu|gov|int|mil|net|org)$', re.IGNORECASE)
simple_email_re = re.compile(r'^\S+@\S+\.\S+$')


def smart_urlquote_wrapper(matched_url):
    try:
        return smart_urlquote(matched_url)
    except ValueError:
        return None


@register.filter(needs_autoescape=True)
def urlize_quoted_links(text, trim_url_limit=None, nofollow=True, autoescape=True):
    def trim_url(x, limit=trim_url_limit):
        return limit is not None and (len(x) > limit and ('%s...' % x[:max(0, limit - 3)])) or x

    safe_input = isinstance(text, SafeData)

    def conditional_escape(text):
~~        return escape(text) if autoescape and not safe_input else text

    words = word_split_re.split(force_str(text))
    for i, word in enumerate(words):
        if '.' in word or '@' in word or ':' in word:
            lead, middle, trail = '', word, ''
            for punctuation in TRAILING_PUNCTUATION:
                if middle.endswith(punctuation):
                    middle = middle[:-len(punctuation)]
                    trail = punctuation + trail
            for opening, closing in WRAPPING_PUNCTUATION:
                if middle.startswith(opening):
                    middle = middle[len(opening):]
                    lead = lead + opening
                if (
                    middle.endswith(closing) and
                    middle.count(closing) == middle.count(opening) + 1
                ):
                    middle = middle[:-len(closing)]
                    trail = closing + trail

            url = None
            nofollow_attr = ' rel="nofollow"' if nofollow else ''
            if simple_url_re.match(middle):
                url = smart_urlquote_wrapper(middle)
def get_pagination_html(pager):
    return pager.to_html()


@register.simple_tag
def render_form(serializer, template_pack=None):
    style = {'template_pack': template_pack} if template_pack else {}
    renderer = HTMLFormRenderer()
    return renderer.render(serializer.data, None, {'style': style})


@register.simple_tag
def render_field(field, style):
    renderer = style.get('renderer', HTMLFormRenderer())
    return renderer.render_field(field, style)


@register.simple_tag
def optional_login(request):
    try:
        login_url = reverse('rest_framework:login')
    except NoReverseMatch:
        return ''

    snippet = "<li><a href='{href}?next={next}'>Log in</a></li>"
~~    snippet = format_html(snippet, href=login_url, next=escape(request.path))

    return mark_safe(snippet)


@register.simple_tag
def optional_docs_login(request):
    try:
        login_url = reverse('rest_framework:login')
    except NoReverseMatch:
        return 'log in'

    snippet = "<a href='{href}?next={next}'>log in</a>"
~~    snippet = format_html(snippet, href=login_url, next=escape(request.path))

    return mark_safe(snippet)


@register.simple_tag


## ... source file continues with no further escape examples...

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
~~from django.utils.html import escape
from django.utils.http import urlencode

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


## ... source file abbreviated to get to escape examples ...




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


## ... source file continues with no further escape examples...

```


## Example 7 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / images / formats.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/images/formats.py)

```python
# formats.py
~~from django.utils.html import escape
from django.utils.translation import gettext_lazy as _

from wagtail.utils.apps import get_app_submodules

from .shortcuts import get_rendition_or_not_found


class Format:
    def __init__(self, name, label, classnames, filter_spec):
        self.name = name
        self.label = label
        self.classnames = classnames
        self.filter_spec = filter_spec

    def editor_attributes(self, image, alt_text):
        return {
            'data-embedtype': "image",
            'data-id': image.id,
            'data-format': self.name,
~~            'data-alt': escape(alt_text),
        }

    def image_to_editor_html(self, image, alt_text):
        return self.image_to_html(
            image, alt_text, self.editor_attributes(image, alt_text)
        )

    def image_to_html(self, image, alt_text, extra_attributes=None):
        if extra_attributes is None:
            extra_attributes = {}
        rendition = get_rendition_or_not_found(image, self.filter_spec)

~~        extra_attributes['alt'] = escape(alt_text)
        if self.classnames:
~~            extra_attributes['class'] = "%s" % escape(self.classnames)

        return rendition.img_tag(extra_attributes)


FORMATS = []
FORMATS_BY_NAME = {}


def register_image_format(format):
    if format.name in FORMATS_BY_NAME:
        raise KeyError("Image format '%s' is already registered" % format.name)
    FORMATS_BY_NAME[format.name] = format
    FORMATS.append(format)


def unregister_image_format(format_name):
    global FORMATS
    try:
        format_name = format_name.name
    except AttributeError:
        pass

    try:
        del FORMATS_BY_NAME[format_name]


## ... source file continues with no further escape examples...

```

