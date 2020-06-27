title: django.contrib.admin.options IncorrectLookupParameters code examples
category: page
slug: django-contrib-admin-options-incorrectlookupparameters-examples
sortorder: 500011023
toc: False
sidebartitle: django.contrib.admin.options IncorrectLookupParameters
meta: Python example code for the IncorrectLookupParameters class from the django.contrib.admin.options module of the Django project.


IncorrectLookupParameters is a class within the django.contrib.admin.options module of the Django project.


## Example 1 from django-jet
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
from django.utils.functional import Promise
~~from django.contrib.admin.options import IncorrectLookupParameters
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
    request = context['request']


## ... source file abbreviated to get to IncorrectLookupParameters examples ...


        if hasattr(model_admin, 'get_search_fields') else model_admin.search_fields
    list_select_related = model_admin.get_list_select_related(request) \
        if hasattr(model_admin, 'get_list_select_related') else model_admin.list_select_related

    actions = model_admin.get_actions(request)
    if actions:
        list_display = ['action_checkbox'] + list(list_display)

    ChangeList = model_admin.get_changelist(request)

    change_list_args = [
        request, model, list_display, list_display_links, list_filter,
        model_admin.date_hierarchy, search_fields, list_select_related,
        model_admin.list_per_page, model_admin.list_max_show_all,
        model_admin.list_editable, model_admin]

    try:
        sortable_by = model_admin.get_sortable_by(request)
        change_list_args.append(sortable_by)
    except AttributeError:
        pass

    try:
        cl = ChangeList(*change_list_args)
        queryset = cl.get_queryset(request)
~~    except IncorrectLookupParameters:
        pass

    return queryset


def get_possible_language_codes():
    language_code = translation.get_language()

    language_code = language_code.replace('_', '-').lower()
    language_codes = []

    split = language_code.split('-', 2)
    if len(split) == 2:
        language_code = '%s-%s' % (split[0].lower(), split[1].upper()) if split[0] != split[1] else split[0]

    language_codes.append(language_code)

    if len(split) == 2:
        language_codes.append(split[0].lower())

    return language_codes


def get_original_menu_items(context):


## ... source file continues with no further IncorrectLookupParameters examples...

```

