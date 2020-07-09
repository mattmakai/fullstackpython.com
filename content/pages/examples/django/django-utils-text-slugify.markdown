title: django.utils.text slugify Example Code
category: page
slug: django-utils-text-slugify-examples
sortorder: 500011493
toc: False
sidebartitle: django.utils.text slugify
meta: Python example code for the slugify callable from the django.utils.text module of the Django project.


slugify is a callable within the django.utils.text module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / forms / wizards.py**](https://github.com/divio/django-cms/blob/develop/cms/forms/wizards.py)

```python
# wizards.py

from __future__ import unicode_literals

from django import forms
from django.core.exceptions import ValidationError
from django.db import transaction
~~from django.utils.text import slugify
from django.utils.translation import (
    ugettext,
    ugettext_lazy as _,
)

from cms.admin.forms import AddPageForm
from cms.plugin_pool import plugin_pool
from cms.utils import get_current_site, permissions
from cms.utils.page import get_available_slug
from cms.utils.page_permissions import (
    user_can_add_page,
    user_can_add_subpage,
)
from cms.utils.conf import get_cms_setting
from cms.utils.urlutils import static_with_version

try:
    from djangocms_text_ckeditor.widgets import TextEditorWidget
    text_widget = TextEditorWidget
except ImportError:
    text_widget = forms.Textarea


class SlugWidget(forms.widgets.TextInput):


## ... source file abbreviated to get to slugify examples ...


        super(CreateCMSPageForm, self).__init__(*args, **kwargs)
        self.fields['title'].help_text = _(u"Provide a title for the new page.")
        self.fields['slug'].required = False
        self.fields['slug'].widget = SlugWidget()
        self.fields['slug'].help_text = _(u"Leave empty for automatic slug, or override as required.")

    @staticmethod
    def get_placeholder(page, slot=None):
        placeholders = page.get_placeholders()

        if slot:
            placeholders = placeholders.filter(slot=slot)

        for ph in placeholders:
            if not ph.is_static and ph.is_editable:
                return ph

        return None

    def clean(self):
        data = self.cleaned_data

        if self._errors:
            return data

~~        slug = data.get('slug') or slugify(data['title'])

        parent_node = data.get('parent_node')

        if parent_node:
            base = parent_node.item.get_path(self._language)
            path = u'%s/%s' % (base, slug) if base else slug
        else:
            base = ''
            path = slug

        data['slug'] = get_available_slug(self._site, path, self._language, suffix=None)
        data['path'] = '%s/%s' % (base, data['slug']) if base else data['slug']

        if not data['slug']:
            raise forms.ValidationError("Please provide a valid slug.")
        return data

    def clean_parent_node(self):
        if self.page and self.sub_page_form:
            parent_page = self.page
        elif self.page and self.page.parent_page:
            parent_page = self.page.parent_page
        else:
            parent_page = None


## ... source file continues with no further slugify examples...

```


## Example 2 from django-jet
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
    from django.urls import reverse, resolve, NoReverseMatch

from django.contrib.admin import AdminSite
from django.utils.encoding import smart_text
from django.utils.text import capfirst
from django.contrib import messages
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.contrib.admin.options import IncorrectLookupParameters
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
~~from django.utils.text import slugify

try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict  # Python 2.6


class JsonResponse(HttpResponse):

    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, **kwargs):
        if safe and not isinstance(data, dict):
            raise TypeError('In order to allow non-dict objects to be '
                'serialized set the safe parameter to False')
        kwargs.setdefault('content_type', 'application/json')
        data = json.dumps(data, cls=encoder)
        super(JsonResponse, self).__init__(content=data, **kwargs)


def get_app_list(context, order=True):
    admin_site = get_admin_site(context)
    request = context['request']

    app_dict = {}
    for model, model_admin in admin_site._registry.items():


## ... source file abbreviated to get to slugify examples ...


                    ))

                    if name in models:
                        item = models[name].copy()

            if 'label' in data:
                item['label'] = data['label']

            if 'url' in data:
                item['url'] = get_menu_item_url(data['url'], original_app_list)

            if 'url_blank' in data:
                item['url_blank'] = data['url_blank']

            if 'permissions' in data:
                item['has_perms'] = item.get('has_perms', True) and context['user'].has_perms(data['permissions'])

            return item

        def get_menu_item_app(data):
            app_label = data.get('app_label')

            if not app_label:
                if 'label' not in data:
                    raise Exception('Custom menu items should at least have \'label\' or \'app_label\' key')
~~                app_label = 'custom_%s' % slugify(data['label'], allow_unicode=True)

            if app_label in original_app_list:
                item = original_app_list[app_label].copy()
            else:
                item = {'app_label': app_label, 'has_perms': True}

            if 'label' in data:
                item['label'] = data['label']

            if 'items' in data:
                item['items'] = list(map(lambda x: get_menu_item_app_model(app_label, x), data['items']))

            if 'url' in data:
                item['url'] = get_menu_item_url(data['url'], original_app_list)

            if 'url_blank' in data:
                item['url_blank'] = data['url_blank']

            if 'permissions' in data:
                item['has_perms'] = item.get('has_perms', True) and context['user'].has_perms(data['permissions'])

            item['pinned'] = item['app_label'] in pinned_apps

            return item


## ... source file continues with no further slugify examples...

```


## Example 3 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / exporters.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/./exporters.py)

```python
# exporters.py
from django.db import DatabaseError
from django.core.serializers.json import DjangoJSONEncoder
import json
import uuid
import string
import sys
from datetime import datetime
PY3 = sys.version_info[0] == 3
if PY3:
    import csv
else:
    import unicodecsv as csv

from django.utils.module_loading import import_string
~~from django.utils.text import slugify
from explorer import app_settings
from six import StringIO, BytesIO


def get_exporter_class(format):
    class_str = dict(getattr(app_settings, 'EXPLORER_DATA_EXPORTERS'))[format]
    return import_string(class_str)


class BaseExporter(object):

    name = ''
    content_type = ''
    file_extension = ''

    def __init__(self, query):
        self.query = query

    def get_output(self, **kwargs):
        value = self.get_file_output(**kwargs).getvalue()
        if PY3:
            return value
        else:
            return str(value)


## ... source file abbreviated to get to slugify examples ...



        row = 0
        col = 0
        header_style = wb.add_format({'bold': True})
        for header in res.header_strings:
            ws.write(row, col, header, header_style)
            col += 1

        row = 1
        col = 0
        for data_row in res.data:
            for data in data_row:
                if isinstance(data, datetime) or isinstance(data, uuid.UUID):
                    data = str(data)
                if isinstance(data, dict) or isinstance(data, list):
                    data = json.dumps(data)
                ws.write(row, col, data)
                col += 1
            row += 1
            col = 0

        wb.close()
        return output

    def _format_title(self):
~~        title = slugify(self.query.title)
        return title[:31]



## ... source file continues with no further slugify examples...

```


## Example 4 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / models.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/./models.py)

```python
# models.py
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import IntegrityError, models, router, transaction
~~from django.utils.text import slugify
from django.utils.translation import gettext, gettext_lazy as _

try:
    from unidecode import unidecode
except ImportError:

    def unidecode(tag):
        return tag


class TagBase(models.Model):
    name = models.CharField(verbose_name=_("name"), unique=True, max_length=100)
    slug = models.SlugField(verbose_name=_("slug"), unique=True, max_length=100)

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.name.lower() > other.name.lower()

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

    class Meta:


## ... source file abbreviated to get to slugify examples ...


            using = kwargs.get("using") or router.db_for_write(
                type(self), instance=self
            )
            kwargs["using"] = using
            try:
                with transaction.atomic(using=using):
                    res = super().save(*args, **kwargs)
                return res
            except IntegrityError:
                pass
            slugs = set(
                type(self)
                ._default_manager.filter(slug__startswith=self.slug)
                .values_list("slug", flat=True)
            )
            i = 1
            while True:
                slug = self.slugify(self.name, i)
                if slug not in slugs:
                    self.slug = slug
                    return super().save(*args, **kwargs)
                i += 1
        else:
            return super().save(*args, **kwargs)

~~    def slugify(self, tag, i=None):
~~        slug = slugify(unidecode(tag))
        if i is not None:
            slug += "_%d" % i
        return slug


class Tag(TagBase):
    class Meta:
        verbose_name = _("tag")
        verbose_name_plural = _("tags")
        app_label = "taggit"


class ItemBase(models.Model):
    def __str__(self):
        return gettext("%(object)s tagged with %(tag)s") % {
            "object": self.content_object,
            "tag": self.tag,
        }

    class Meta:
        abstract = True

    @classmethod
    def tag_model(cls):


## ... source file continues with no further slugify examples...

```


## Example 5 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/models.py)

```python
# models.py
import json
import logging
from collections import defaultdict
from io import StringIO
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core import checks
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.handlers.base import BaseHandler
from django.core.handlers.wsgi import WSGIRequest
from django.db import models, transaction
from django.db.models import Case, Q, Value, When
from django.db.models.functions import Concat, Lower, Substr
from django.http import Http404
from django.http.request import split_domain_port
from django.template.response import TemplateResponse
from django.urls import NoReverseMatch, reverse
from django.utils import timezone
from django.utils.cache import patch_cache_control
from django.utils.functional import cached_property
~~from django.utils.text import capfirst, slugify
from django.utils.translation import gettext_lazy as _
from modelcluster.models import (
    ClusterableModel, get_all_child_m2m_relations, get_all_child_relations)
from treebeard.mp_tree import MP_Node

from wagtail.core.query import PageQuerySet, TreeQuerySet
from wagtail.core.signals import page_published, page_unpublished, post_page_move, pre_page_move
from wagtail.core.sites import get_site_for_hostname
from wagtail.core.url_routing import RouteResult
from wagtail.core.utils import WAGTAIL_APPEND_SLASH, camelcase_to_underscore, resolve_model_string
from wagtail.search import index


logger = logging.getLogger('wagtail.core')

PAGE_TEMPLATE_VAR = 'page'


class SiteManager(models.Manager):
    def get_queryset(self):
        return super(SiteManager, self).get_queryset().order_by(Lower("hostname"))

    def get_by_natural_key(self, hostname, port):
        return self.get(hostname=hostname, port=port)


## ... source file abbreviated to get to slugify examples ...


    def _slug_is_available(slug, parent_page, page=None):
        if parent_page is None:
            return True

        siblings = parent_page.get_children()
        if page:
            siblings = siblings.not_page(page)

        return not siblings.filter(slug=slug).exists()

    def _get_autogenerated_slug(self, base_slug):
        candidate_slug = base_slug
        suffix = 1
        parent_page = self.get_parent()

        while not Page._slug_is_available(candidate_slug, parent_page, self):
            suffix += 1
            candidate_slug = "%s-%d" % (base_slug, suffix)

        return candidate_slug

    def full_clean(self, *args, **kwargs):

        if not self.slug:
            allow_unicode = getattr(settings, 'WAGTAIL_ALLOW_UNICODE_SLUGS', True)
~~            base_slug = slugify(self.title, allow_unicode=allow_unicode)

            if base_slug:
                self.slug = self._get_autogenerated_slug(base_slug)

        if not self.draft_title:
            self.draft_title = self.title

        super().full_clean(*args, **kwargs)

    def clean(self):
        super().clean()
        if not Page._slug_is_available(self.slug, self.get_parent(), self):
            raise ValidationError({'slug': _("This slug is already in use")})

    @transaction.atomic
    def save(self, clean=True, **kwargs):
        if clean:
            self.full_clean()

        update_descendant_url_paths = False
        is_new = self.id is None

        if is_new:
            self.set_url_path(self.get_parent())


## ... source file continues with no further slugify examples...

```

