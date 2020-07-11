title: django.core.exceptions FieldError Example Code
category: page
slug: django-core-exceptions-fielderror-examples
sortorder: 500011100
toc: False
sidebartitle: django.core.exceptions FieldError
meta: Python example code for the FieldError class from the django.core.exceptions module of the Django project.


FieldError is a class within the django.core.exceptions module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / api.py**](https://github.com/divio/django-cms/blob/develop/cms/./api.py)

```python
# api.py
import datetime

from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
~~from django.core.exceptions import FieldError
from django.core.exceptions import PermissionDenied
from django.core.exceptions import ValidationError
from django.db import transaction
from django.template.defaultfilters import slugify
from django.template.loader import get_template
from django.utils.translation import activate

from six import string_types

from cms import constants
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from cms.constants import TEMPLATE_INHERITANCE_MAGIC
from cms.models.pagemodel import Page
from cms.models.permissionmodels import (PageUser, PagePermission, GlobalPagePermission,
                                         ACCESS_PAGE_AND_DESCENDANTS)
from cms.models.placeholdermodel import Placeholder
from cms.models.pluginmodel import CMSPlugin
from cms.models.titlemodels import Title
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.utils import copy_plugins, get_current_site
from cms.utils.conf import get_cms_setting
from cms.utils.i18n import get_language_list


## ... source file abbreviated to get to FieldError examples ...



    if navigation_extenders:
        raw_menus = menu_pool.get_menus_by_attribute("cms_enabled", True)
        menus = [menu[0] for menu in raw_menus]
        assert navigation_extenders in menus

    accepted_limitations = (constants.VISIBILITY_ALL, constants.VISIBILITY_USERS, constants.VISIBILITY_ANONYMOUS)
    assert limit_visibility_in_menu in accepted_limitations

    assert position in ('last-child', 'first-child', 'left', 'right')
    target_node = parent.node if parent else None

    if apphook:
        application_urls = _verify_apphook(apphook, apphook_namespace)
    else:
        application_urls = None

    if created_by and isinstance(created_by, get_user_model()):
        _thread_locals.user = created_by
        created_by = getattr(created_by, get_user_model().USERNAME_FIELD)
    else:
        _thread_locals.user = None

    if reverse_id:
        if Page.objects.drafts().filter(reverse_id=reverse_id, node__site=site).exists():
~~            raise FieldError('A page with the reverse_id="%s" already exist.' % reverse_id)

    page = Page(
        created_by=created_by,
        changed_by=created_by,
        publication_date=publication_date,
        publication_end_date=publication_end_date,
        in_navigation=in_navigation,
        soft_root=soft_root,
        reverse_id=reverse_id,
        navigation_extenders=navigation_extenders,
        template=template,
        application_urls=application_urls,
        application_namespace=apphook_namespace,
        login_required=login_required,
        limit_visibility_in_menu=limit_visibility_in_menu,
        xframe_options=xframe_options,
    )
    page.set_tree_node(site=site, target=target_node, position=position)
    page.save()
    page.rescan_placeholders()

    create_title(
        language=language,
        title=title,


## ... source file continues with no further FieldError examples...

```


## Example 2 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / utils.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/./utils.py)

```python
# utils.py
import warnings
from collections import OrderedDict

from django.conf import settings
~~from django.core.exceptions import FieldDoesNotExist, FieldError
from django.db import models
from django.db.models.constants import LOOKUP_SEP
from django.db.models.expressions import Expression
from django.db.models.fields.related import ForeignObjectRel, RelatedField
from django.utils import timezone
from django.utils.encoding import force_str
from django.utils.text import capfirst
from django.utils.translation import gettext as _

from .exceptions import FieldLookupError


def deprecate(msg, level_modifier=0):
    warnings.warn(msg, MigrationNotice, stacklevel=3 + level_modifier)


class MigrationNotice(DeprecationWarning):
    url = 'https://django-filter.readthedocs.io/en/master/guide/migration.html'

    def __init__(self, message):
        super().__init__('%s See: %s' % (message, self.url))


class RenameAttributesBase(type):


## ... source file abbreviated to get to FieldError examples ...


        elif isinstance(field, ForeignObjectRel):
            opts = field.related_model._meta

    return fields


def resolve_field(model_field, lookup_expr):
    query = model_field.model._default_manager.all().query
    lhs = Expression(model_field)
    lookups = lookup_expr.split(LOOKUP_SEP)

    assert len(lookups) > 0

    try:
        while lookups:
            name = lookups[0]
            args = (lhs, name)
            if len(lookups) == 1:
                final_lookup = lhs.get_lookup(name)
                if not final_lookup:
                    lhs = query.try_transform(*args)
                    final_lookup = lhs.get_lookup('exact')
                return lhs.output_field, final_lookup.lookup_name
            lhs = query.try_transform(*args)
            lookups = lookups[1:]
~~    except FieldError as e:
        raise FieldLookupError(model_field, lookup_expr) from e


def handle_timezone(value, is_dst=None):
    if settings.USE_TZ and timezone.is_naive(value):
        return timezone.make_aware(value, timezone.get_current_timezone(), is_dst)
    elif not settings.USE_TZ and timezone.is_aware(value):
        return timezone.make_naive(value, timezone.utc)
    return value


def verbose_field_name(model, field_name):
    if field_name is None:
        return '[invalid name]'

    parts = get_field_parts(model, field_name)
    if not parts:
        return '[invalid name]'

    names = []
    for part in parts:
        if isinstance(part, ForeignObjectRel):
            if part.related_name:
                names.append(part.related_name.replace('_', ' '))


## ... source file continues with no further FieldError examples...

```


## Example 3 from django-model-utils
[django-model-utils](https://github.com/jazzband/django-model-utils)
([project documentation](https://django-model-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-model-utils/))
provides useful mixins and utilities for working with
[Django ORM](/django-orm.html) models in your projects.

The django-model-utils project is open sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/jazzband/django-model-utils/blob/master/LICENSE.txt).

[**django-model-utils / model_utils / tracker.py**](https://github.com/jazzband/django-model-utils/blob/master/model_utils/./tracker.py)

```python
# tracker.py
from copy import deepcopy
from functools import wraps

import django
~~from django.core.exceptions import FieldError
from django.db import models
from django.db.models.fields.files import FileDescriptor
from django.db.models.query_utils import DeferredAttribute


class DescriptorMixin:
    tracker_instance = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        was_deferred = False
        field_name = self._get_field_name()
        if field_name in instance._deferred_fields:
            instance._deferred_fields.remove(field_name)
            was_deferred = True
        value = super().__get__(instance, owner)
        if was_deferred:
            self.tracker_instance.saved_data[field_name] = deepcopy(value)
        return value

    def _get_field_name(self):
        return self.field_name



## ... source file abbreviated to get to FieldError examples ...


        else:
            self.saved_data.update(**self.current(fields=fields))

        for field, field_value in self.saved_data.items():
            self.saved_data[field] = deepcopy(field_value)

    def current(self, fields=None):
        if fields is None:
            deferred_fields = self.deferred_fields
            if deferred_fields:
                fields = [
                    field for field in self.fields
                    if field not in deferred_fields
                ]
            else:
                fields = self.fields

        return {f: self.get_field_value(f) for f in fields}

    def has_changed(self, field):
        if field in self.fields:
            if field in self.deferred_fields and field not in self.instance.__dict__:
                return False
            return self.previous(field) != self.get_field_value(field)
        else:
~~            raise FieldError('field "%s" not tracked' % field)

    def previous(self, field):

        if self.instance.pk and field in self.deferred_fields and field not in self.saved_data:

            if field not in self.instance.__dict__:
                self.get_field_value(field)

            else:
                current_value = self.get_field_value(field)
                self.instance.refresh_from_db(fields=[field])
                self.saved_data[field] = deepcopy(self.get_field_value(field))
                setattr(self.instance, self.field_map[field], current_value)

        return self.saved_data.get(field)

    def changed(self):
        return {
            field: self.previous(field)
            for field in self.fields
            if self.has_changed(field)
        }

    def init_deferred_fields(self):


## ... source file abbreviated to get to FieldError examples ...


                    field for field in update_fields if
                    field in self.fields
                )
            getattr(instance, self.attname).set_saved_fields(
                fields=fields
            )
            return ret

        setattr(model, method, inner)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.attname)


class ModelInstanceTracker(FieldInstanceTracker):

    def has_changed(self, field):
        if not self.instance.pk:
            return True
        elif field in self.saved_data:
            return self.previous(field) != self.get_field_value(field)
        else:
~~            raise FieldError('field "%s" not tracked' % field)

    def changed(self):
        if not self.instance.pk:
            return {}
        saved = self.saved_data.items()
        current = self.current()
        return {k: v for k, v in saved if v != current[k]}


class ModelTracker(FieldTracker):
    tracker_class = ModelInstanceTracker

    def get_field_map(self, cls):
        return {field: field for field in self.fields}



## ... source file continues with no further FieldError examples...

```

