title: django.urls.exceptions NoReverseMatch Python Code Examples
category: page
slug: django-urls-exceptions-noreversematch-examples
sortorder: 500013640
toc: False
sidebartitle: django.urls.exceptions NoReverseMatch
meta: Python example code for the NoReverseMatch exception class from the django.urls.exceptions module.


[NoReverseMatch](https://docs.djangoproject.com/en/stable/ref/exceptions/#noreversematch)
([source code](https://github.com/django/django/blob/master/django/urls/exceptions.py))
is a [Django](/django.html) exception that is raised when a URL
cannot be matched against any string or regular express in your URL 
configuration. 

A URL matching problem is often caused by missing arguments or 
supplying too many arguments. For example, let's say you have a blog
project with URLs like "myblog.com/2019/10/title-slug", where `2019`
is the year, `10` is the month and `title-slug` is the article's title
as a [slug](https://stackoverflow.com/questions/427102/what-is-a-slug-in-django). 
A miss could happen if you have a URL configuration that is trying to 
find a blog post with the year and the month in the path, but your 
application only specifies the year without the month.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular) 
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use 
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is 
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / core / urlresolvers.py**](https://github.com/jrief/django-angular/blob/master/djng/core/urlresolvers.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from inspect import isclass

from django.utils import six
~~from django.urls import (get_resolver, get_urlconf, resolve, 
~~                         reverse, NoReverseMatch)
from django.core.exceptions import ImproperlyConfigured

try:
    from django.utils.module_loading import import_string
except ImportError:
    from django.utils.module_loading \
        import import_by_path as import_string

from djng.views.mixins import JSONResponseMixin


def _get_remote_methods_for(view_object, url):
    # view_object can be a view class or instance
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
    """
    Returns a dictionary to be used for calling 
    ``djangoCall.configure()``, which itself extends the
    Angular API to the client, offering him to call remote methods.
    """
    if not resolver:
        resolver = get_resolver(get_urlconf())
    result = {}
    for name in resolver.reverse_dict.keys():
        if not isinstance(name, six.string_types):
            continue
~~        try:
~~            url = reverse(ns_prefix + name)
~~            resmgr = resolve(url)
~~            ViewClass = import_string('{0}.{1}'.format(\
~~                resmgr.func.__module__, resmgr.func.__name__))
~~            if isclass(ViewClass) and issubclass(ViewClass, 
~~                                                 JSONResponseMixin):
~~                result[name] = _get_remote_methods_for(ViewClass, 
~~                                                       url)
~~        except (NoReverseMatch, ImproperlyConfigured):
~~            pass
    for namespace, ns_pattern in resolver.namespace_dict.items():
        sub_res = get_all_remote_methods(ns_pattern[1], 
                                         ns_prefix + namespace + ':')
        if sub_res:
            result[namespace] = sub_res
    return result


def get_current_remote_methods(view):
    if isinstance(view, JSONResponseMixin):
        return _get_remote_methods_for(view, 
                                       view.request.path_info)
```


## Example 2 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog / mixins.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/mixins.py)

```python
import json

from django.conf import settings
try:
    from django.core import urlresolvers
except ImportError:
    from django import urls as urlresolvers
~~try:
~~    from django.urls.exceptions import NoReverseMatch
~~except ImportError:
~~    from django.core.urlresolvers import NoReverseMatch
from django.utils.html import format_html
from django.utils.safestring import mark_safe

MAX = 75


class LogEntryAdminMixin(object):

    def created(self, obj):
        return obj.timestamp.strftime('%Y-%m-%d %H:%M:%S')
    created.short_description = 'Created'

    def user_url(self, obj):
        if obj.actor:
            app_label, model = settings.AUTH_USER_MODEL.split('.')
            viewname = 'admin:%s_%s_change' % (app_label, model.lower())
~~            try:
~~                link = urlresolvers.reverse(viewname, args=[obj.actor.id])
~~            except NoReverseMatch:
~~                return u'%s' % (obj.actor)
            return format_html(u'<a href="{}">{}</a>', link, obj.actor)

        return 'system'
    user_url.short_description = 'User'

    def resource_url(self, obj):
        app_label, model = obj.content_type.app_label, obj.content_type.model
        viewname = 'admin:%s_%s_change' % (app_label, model)
~~        try:
~~            args = [obj.object_pk] if obj.object_id is None else [obj.object_id]
~~            link = urlresolvers.reverse(viewname, args=args)
~~        except NoReverseMatch:
~~            return obj.object_repr
~~        else:
~~            return format_html(u'<a href="{}">{}</a>', link, obj.object_repr)
    resource_url.short_description = 'Resource'

    def msg_short(self, obj):
        if obj.action == 2:
            return ''  # delete
        changes = json.loads(obj.changes)
        s = '' if len(changes) == 1 else 's'
        fields = ', '.join(changes.keys())
        if len(fields) > MAX:
            i = fields.rfind(' ', 0, MAX)
            fields = fields[:i] + ' ..'
        return '%d change%s: %s' % (len(changes), s, fields)
    msg_short.short_description = 'Changes'

    def msg(self, obj):
        if obj.action == 2:
            return ''  # delete
        changes = json.loads(obj.changes)
        msg = '<table><tr><th>#</th><th>Field</th><th>From</th><th>To</th></tr>'
        for i, field in enumerate(sorted(changes), 1):
            value = [i, field] + (['***', '***'] if field == 'password' else changes[field])
            msg += format_html('<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>', *value)

        msg += '</table>'
        return mark_safe(msg)
    msg.short_description = 'Changes'

```


## Example 3 from django-filer
[django-filer](https://github.com/divio/django-filer)
([project documentation](https://django-filer.readthedocs.io/en/latest/))
is a file management library for uploading and organizing files and images
in Django's admin interface. The project's code is available under the
[BSD 3-Clause "New" or "Revised" open source license](https://github.com/divio/django-filer/blob/develop/LICENSE.txt).

[**django-filer / filer / models / filemodels.py**](https://github.com/divio/django-filer/blob/develop/filer/models/filemodels.py)

```python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import hashlib
import os
from datetime import datetime

from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models
~~from django.urls import NoReverseMatch, reverse
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .. import settings as filer_settings
from ..fields.multistorage_file import MultiStorageFileField
from . import mixins
from .foldermodels import Folder


try:
    from polymorphic.models import PolymorphicModel
    from polymorphic.managers import PolymorphicManager
except ImportError:
    # django-polymorphic < 0.8
    from polymorphic import PolymorphicModel, PolymorphicManager


class FileManager(PolymorphicManager):
    def find_all_duplicates(self):
        r = {}
        for file_obj in self.all():
            if file_obj.sha1:
                q = self.filter(sha1=file_obj.sha1)
                if len(q) > 1:
                    r[file_obj.sha1] = q
        return r

    def find_duplicates(self, file_obj):
        return [i for i in self.exclude(pk=file_obj.pk).filter(sha1=file_obj.sha1)]


def is_public_default():
    # not using this setting directly as `is_public` default value
    # so that Django doesn't generate new migrations upon setting change
    return filer_settings.FILER_IS_PUBLIC_DEFAULT


@python_2_unicode_compatible
class File(PolymorphicModel, mixins.IconsMixin):
    file_type = 'File'
    _icon = "file"
    _file_data_changed_hint = None

    folder = models.ForeignKey(
        Folder,
        verbose_name=_('folder'),
        related_name='all_files',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
    file = MultiStorageFileField(_('file'), null=True, blank=True, max_length=255)
    _file_size = models.BigIntegerField(_('file size'), null=True, blank=True)

    sha1 = models.CharField(_('sha1'), max_length=40, blank=True, default='')

    has_all_mandatory_data = models.BooleanField(_('has all mandatory data'), default=False, editable=False)


## ... source file abbreviated to get to the examples ...


    @property
    def canonical_url(self):
        url = ''
~~        if self.file and self.is_public:
~~            try:
~~                url = reverse('canonical', kwargs={
~~                    'uploaded_at': self.canonical_time,
~~                    'file_id': self.id
~~                })
~~            except NoReverseMatch:
~~                pass  # No canonical url, return empty string
        return url

## ... source file continues with no further relevant examples ...
```
