title: django.views.generic.list ListView Example Code
category: page
slug: django-views-generic-list-listview-examples
sortorder: 500011539
toc: False
sidebartitle: django.views.generic.list ListView
meta: Python example code for the ListView class from the django.views.generic.list module of the Django project.


ListView is a class within the django.views.generic.list module of the Django project.


## Example 1 from django-tables2
[django-tables2](https://github.com/jieter/django-tables2)
([projection documentation](https://django-tables2.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-tables2/))
is a code library for [Django](/django.html) that simplifies creating and
displaying tables in [Django templates](/django-templates.html),
especially with more advanced features such as pagination and sorting.
The project and its code are
[available as open source](https://github.com/jieter/django-tables2/blob/master/LICENSE).

[**django-tables2 / django_tables2 / views.py**](https://github.com/jieter/django-tables2/blob/master/django_tables2/./views.py)

```python
# views.py
from itertools import count

from django.core.exceptions import ImproperlyConfigured
~~from django.views.generic.list import ListView

from . import tables
from .config import RequestConfig


class TableMixinBase:

    context_table_name = "table"
    table_pagination = None

    def get_context_table_name(self, table):
        return self.context_table_name

    def get_table_pagination(self, table):
        paginate = self.table_pagination
        if paginate is False:
            return False

        paginate = {}
        if getattr(self, "paginate_by", None) is not None:
            paginate["per_page"] = self.paginate_by
        if hasattr(self, "paginator_class"):
            paginate["paginator_class"] = self.paginator_class
        if getattr(self, "paginate_orphans", 0) != 0:


## ... source file abbreviated to get to ListView examples ...


        )

    def get_table_data(self):
        if self.table_data is not None:
            return self.table_data
        elif hasattr(self, "object_list"):
            return self.object_list
        elif hasattr(self, "get_queryset"):
            return self.get_queryset()

        klass = type(self).__name__
        raise ImproperlyConfigured(
            "Table data was not specified. Define {}.table_data".format(klass)
        )

    def get_table_kwargs(self):
        return {}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        table = self.get_table(**self.get_table_kwargs())
        context[self.get_context_table_name(table)] = table
        return context


~~class SingleTableView(SingleTableMixin, ListView):


class MultiTableMixin(TableMixinBase):

    tables = None
    tables_data = None

    table_prefix = "table_{}-"

    context_table_name = "tables"

    def get_tables(self):
        if self.tables is None:
            klass = type(self).__name__
            raise ImproperlyConfigured("No tables were specified. Define {}.tables".format(klass))
        data = self.get_tables_data()

        if data is None:
            return self.tables

        if len(data) != len(self.tables):
            klass = type(self).__name__
            raise ImproperlyConfigured("len({}.tables_data) != len({}.tables)".format(klass, klass))
        return list(Table(data[i]) for i, Table in enumerate(self.tables))


## ... source file continues with no further ListView examples...

```


## Example 2 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / views.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/views.py)

```python
# views.py
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
~~from django.views.generic.list import ListView

from taggit.models import Tag, TaggedItem


def tagged_object_list(request, slug, queryset, **kwargs):
    if callable(queryset):
        queryset = queryset()
    kwargs["slug"] = slug
    tag_list_view = type(
        "TagListView",
        (TagListMixin, ListView),
        {"model": queryset.model, "queryset": queryset},
    )
    return tag_list_view.as_view()(request, **kwargs)


class TagListMixin:
    tag_suffix = "_tag"

    def dispatch(self, request, *args, **kwargs):
        slug = kwargs.pop("slug")
        self.tag = get_object_or_404(Tag, slug=slug)
        return super().dispatch(request, *args, **kwargs)



## ... source file continues with no further ListView examples...

```

