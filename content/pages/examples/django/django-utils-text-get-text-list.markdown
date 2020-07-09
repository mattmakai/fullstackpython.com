title: django.utils.text get_text_list Example Code
category: page
slug: django-utils-text-get-text-list-examples
sortorder: 500011491
toc: False
sidebartitle: django.utils.text get_text_list
meta: Python example code for the get_text_list callable from the django.utils.text module of the Django project.


get_text_list is a callable within the django.utils.text module of the Django project.


## Example 1 from django-extensions
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
# __init__.py
import six
import operator
from functools import update_wrapper
from six.moves import reduce
from typing import Tuple, Dict, Callable  # NOQA

from django.apps import apps
from django.http import HttpResponse, HttpResponseNotFound
from django.conf import settings
from django.db import models
from django.db.models.query import QuerySet
from django.utils.encoding import smart_str
from django.utils.translation import gettext as _
~~from django.utils.text import get_text_list
from django.contrib import admin

from django_extensions.admin.widgets import ForeignKeySearchInput


class ForeignKeyAutocompleteAdminMixin:

    related_search_fields = {}  # type: Dict[str, Tuple[str]]
    related_string_functions = {}  # type: Dict[str, Callable]
    autocomplete_limit = getattr(settings, 'FOREIGNKEY_AUTOCOMPLETE_LIMIT', None)

    def get_urls(self):
        from django.urls import path

        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)
            return update_wrapper(wrapper, view)

        return [
            path('foreignkey_autocomplete/', wrap(self.foreignkey_autocomplete),
                name='%s_%s_autocomplete' % (self.model._meta.app_label, self.model._meta.model_name))
        ] + super().get_urls()



## ... source file abbreviated to get to get_text_list examples ...


                if additional_filter:
                    queryset = queryset.filter(additional_filter)

                if self.autocomplete_limit:
                    queryset = queryset[:self.autocomplete_limit]

                data = ''.join([six.u('%s|%s\n') % (to_string_function(f), f.pk) for f in queryset])
            elif object_pk:
                try:
                    obj = queryset.get(pk=object_pk)
                except Exception:  # FIXME: use stricter exception checking
                    pass
                else:
                    data = to_string_function(obj)
            return HttpResponse(data, content_type='text/plain')
        return HttpResponseNotFound()

    def get_related_filter(self, model, request):
        return None

    def get_help_text(self, field_name, model_name):
        searchable_fields = self.related_search_fields.get(field_name, None)
        if searchable_fields:
            help_kwargs = {
                'model_name': model_name,
~~                'field_list': get_text_list(searchable_fields, _('and')),
            }
            return _('Use the left field to do %(model_name)s lookups in the fields %(field_list)s.') % help_kwargs
        return ''

    def formfield_for_dbfield(self, db_field, **kwargs):
        if isinstance(db_field, models.ForeignKey) and db_field.name in self.related_search_fields:
            help_text = self.get_help_text(db_field.name, db_field.remote_field.model._meta.object_name)
            if kwargs.get('help_text'):
                help_text = six.u('%s %s' % (kwargs['help_text'], help_text))
            kwargs['widget'] = ForeignKeySearchInput(db_field.remote_field, self.related_search_fields[db_field.name])
            kwargs['help_text'] = help_text
        return super().formfield_for_dbfield(db_field, **kwargs)


class ForeignKeyAutocompleteAdmin(ForeignKeyAutocompleteAdminMixin, admin.ModelAdmin):
    pass


class ForeignKeyAutocompleteTabularInline(ForeignKeyAutocompleteAdminMixin, admin.TabularInline):
    pass


class ForeignKeyAutocompleteStackedInline(ForeignKeyAutocompleteAdminMixin, admin.StackedInline):
    pass


## ... source file continues with no further get_text_list examples...

```

