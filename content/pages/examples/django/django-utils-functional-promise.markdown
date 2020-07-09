title: django.utils.functional Promise Example Code
category: page
slug: django-utils-functional-promise-examples
sortorder: 500011455
toc: False
sidebartitle: django.utils.functional Promise
meta: Python example code for the Promise class from the django.utils.functional module of the Django project.


Promise is a class within the django.utils.functional module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / toolbar / items.py**](https://github.com/divio/django-cms/blob/develop/cms/toolbar/items.py)

```python
# items.py
import json
from abc import ABCMeta
from collections import defaultdict

from django.template.loader import render_to_string
from django.utils.encoding import force_text
~~from django.utils.functional import Promise

from six import with_metaclass

from cms.constants import RIGHT, LEFT, REFRESH_PAGE, URL_CHANGE


class ItemSearchResult(object):
    def __init__(self, item, index):
        self.item = item
        self.index = index

    def __add__(self, other):
        return ItemSearchResult(self.item, self.index + other)

    def __sub__(self, other):
        return ItemSearchResult(self.item, self.index - other)

    def __int__(self):
        return self.index


def may_be_lazy(thing):
~~    if isinstance(thing, Promise):
        return thing._proxy____args[0]
    else:
        return thing


class ToolbarAPIMixin(with_metaclass(ABCMeta)):
    REFRESH_PAGE = REFRESH_PAGE
    URL_CHANGE = URL_CHANGE
    LEFT = LEFT
    RIGHT = RIGHT

    def __init__(self):
        self.items = []
        self.menus = {}
        self._memo = defaultdict(list)

    def _memoize(self, item):
        self._memo[item.__class__].append(item)

    def _unmemoize(self, item):
        self._memo[item.__class__].remove(item)

    def _item_position(self, item):
        return self.items.index(item)


## ... source file continues with no further Promise examples...

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
    from django.urls import reverse, resolve, NoReverseMatch

from django.contrib.admin import AdminSite
from django.utils.encoding import smart_text
from django.utils.text import capfirst
from django.contrib import messages
from django.utils.encoding import force_text
~~from django.utils.functional import Promise
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
        kwargs.setdefault('content_type', 'application/json')
        data = json.dumps(data, cls=encoder)
        super(JsonResponse, self).__init__(content=data, **kwargs)


def get_app_list(context, order=True):
    admin_site = get_admin_site(context)


## ... source file abbreviated to get to Promise examples ...


def get_admin_site(context):
    try:
        current_resolver = resolve(context.get('request').path)
        index_resolver = resolve(reverse('%s:index' % current_resolver.namespaces[0]))

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
~~        elif isinstance(obj, Promise):
            return force_text(obj)
        return self.encode(obj)


def get_model_instance_label(instance):
    if getattr(instance, "related_label", None):
        return instance.related_label()
    return smart_text(instance)


class SuccessMessageMixin(object):
    success_message = ''

    def form_valid(self, form):
        response = super(SuccessMessageMixin, self).form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data




## ... source file continues with no further Promise examples...

```


## Example 3 from django-jsonfield
[django-jsonfield](https://github.com/dmkoch/django-jsonfield)
([jsonfield on PyPi](https://pypi.org/project/jsonfield/)) is a
[Django](/django.html) code library that makes it easier to store validated
JSON in a [Django object-relational mapper (ORM)](/django-orm.html) database
model.

The django-jsonfield project is open source under the
[MIT license](https://github.com/dmkoch/django-jsonfield/blob/master/LICENSE).

[**django-jsonfield / src/jsonfield / encoder.py**](https://github.com/dmkoch/django-jsonfield/blob/master/src/jsonfield/./encoder.py)

```python
# encoder.py
import datetime
import decimal
import json
import uuid

from django.db.models.query import QuerySet
from django.utils import timezone
from django.utils.encoding import force_str
~~from django.utils.functional import Promise


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):  # noqa: C901
~~        if isinstance(obj, Promise):
            return force_str(obj)
        elif isinstance(obj, datetime.datetime):
            representation = obj.isoformat()
            if representation.endswith('+00:00'):
                representation = representation[:-6] + 'Z'
            return representation
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.time):
            if timezone and timezone.is_aware(obj):
                raise ValueError("JSON can't represent timezone-aware times.")
            representation = obj.isoformat()
            return representation
        elif isinstance(obj, datetime.timedelta):
            return str(obj.total_seconds())
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        elif isinstance(obj, QuerySet):
            return tuple(obj)
        elif isinstance(obj, bytes):
            return obj.decode()
        elif hasattr(obj, 'tolist'):


## ... source file continues with no further Promise examples...

```


## Example 4 from django-rest-framework
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

[**django-rest-framework / rest_framework / utils / encoders.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/utils/encoders.py)

```python
# encoders.py
import datetime
import decimal
import json  # noqa
import uuid

from django.db.models.query import QuerySet
from django.utils import timezone
from django.utils.encoding import force_str
~~from django.utils.functional import Promise

from rest_framework.compat import coreapi


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
~~        if isinstance(obj, Promise):
            return force_str(obj)
        elif isinstance(obj, datetime.datetime):
            representation = obj.isoformat()
            if representation.endswith('+00:00'):
                representation = representation[:-6] + 'Z'
            return representation
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.time):
            if timezone and timezone.is_aware(obj):
                raise ValueError("JSON can't represent timezone-aware times.")
            representation = obj.isoformat()
            return representation
        elif isinstance(obj, datetime.timedelta):
            return str(obj.total_seconds())
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        elif isinstance(obj, QuerySet):
            return tuple(obj)
        elif isinstance(obj, bytes):
            return obj.decode()
        elif hasattr(obj, 'tolist'):


## ... source file continues with no further Promise examples...

```

