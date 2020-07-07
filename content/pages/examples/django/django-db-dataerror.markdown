title: django.db DataError Example Code
category: page
slug: django-db-dataerror-examples
sortorder: 500011159
toc: False
sidebartitle: django.db DataError
meta: Python example code for the DataError class from the django.db module of the Django project.


DataError is a class within the django.db module of the Django project.


## Example 1 from django-rest-framework
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

[**django-rest-framework / rest_framework / validators.py**](https://github.com/encode/django-rest-framework/blob/master/rest_framework/./validators.py)

```python
# validators.py
~~from django.db import DataError
from django.utils.translation import gettext_lazy as _

from rest_framework.exceptions import ValidationError
from rest_framework.utils.representation import smart_repr


def qs_exists(queryset):
    try:
        return queryset.exists()
~~    except (TypeError, ValueError, DataError):
        return False


def qs_filter(queryset, **kwargs):
    try:
        return queryset.filter(**kwargs)
~~    except (TypeError, ValueError, DataError):
        return queryset.none()


class UniqueValidator:
    message = _('This field must be unique.')
    requires_context = True

    def __init__(self, queryset, message=None, lookup='exact'):
        self.queryset = queryset
        self.message = message or self.message
        self.lookup = lookup

    def filter_queryset(self, value, queryset, field_name):
        filter_kwargs = {'%s__%s' % (field_name, self.lookup): value}
        return qs_filter(queryset, **filter_kwargs)

    def exclude_current_instance(self, queryset, instance):
        if instance is not None:
            return queryset.exclude(pk=instance.pk)
        return queryset

    def __call__(self, value, serializer_field):
        field_name = serializer_field.source_attrs[-1]
        instance = getattr(serializer_field.parent, 'instance', None)


## ... source file continues with no further DataError examples...

```

