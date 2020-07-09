title: django.utils.deprecation RenameMethodsBase Example Code
category: page
slug: django-utils-deprecation-renamemethodsbase-examples
sortorder: 500011438
toc: False
sidebartitle: django.utils.deprecation RenameMethodsBase
meta: Python example code for the RenameMethodsBase class from the django.utils.deprecation module of the Django project.


RenameMethodsBase is a class within the django.utils.deprecation module of the Django project.


## Example 1 from django-filter
[django-filter](https://github.com/carltongibson/django-filter)
([project documentation](https://django-filter.readthedocs.io/en/master/)
and
[PyPI page](https://pypi.org/project/django-filter/2.2.0/))
makes it easier to filter down querysets from the
[Django ORM](/django-orm.html) by providing common bits of boilerplate
code. django-filter is provided as
[open source](https://github.com/carltongibson/django-filter/blob/master/LICENSE).

[**django-filter / django_filters / rest_framework / backends.py**](https://github.com/carltongibson/django-filter/blob/master/django_filters/rest_framework/backends.py)

```python
# backends.py
import warnings

from django.template import loader
~~from django.utils.deprecation import RenameMethodsBase

from .. import compat, utils
from . import filters, filterset


~~class RenameAttributes(utils.RenameAttributesBase, RenameMethodsBase):
    renamed_attributes = (
        ('default_filter_set', 'filterset_base', utils.MigrationNotice),
    )
    renamed_methods = (
        ('get_filter_class', 'get_filterset_class', utils.MigrationNotice),
    )


class DjangoFilterBackend(metaclass=RenameAttributes):
    filterset_base = filterset.FilterSet
    raise_exception = True

    @property
    def template(self):
        if compat.is_crispy():
            return 'django_filters/rest_framework/crispy_form.html'
        return 'django_filters/rest_framework/form.html'

    def get_filterset(self, request, queryset, view):
        filterset_class = self.get_filterset_class(view, queryset)
        if filterset_class is None:
            return None

        kwargs = self.get_filterset_kwargs(request, queryset, view)


## ... source file continues with no further RenameMethodsBase examples...

```

