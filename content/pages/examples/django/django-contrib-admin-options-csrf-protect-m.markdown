title: django.contrib.admin.options csrf_protect_m code examples
category: page
slug: django-contrib-admin-options-csrf-protect-m-examples
sortorder: 500011025
toc: False
sidebartitle: django.contrib.admin.options csrf_protect_m
meta: Python example code for the csrf_protect_m function from the django.contrib.admin.options module of the Django project.


csrf_protect_m is a function within the django.contrib.admin.options module of the Django project.


## Example 1 from django-haystack
[django-haystack](https://github.com/django-haystack/django-haystack)
([project website](http://haystacksearch.org/) and
[PyPI page](https://pypi.org/project/django-haystack/))
is a search abstraction layer that separates the Python search code
in a [Django](/django.html) web application from the search engine
implementation that it runs on, such as
[Apache Solr](http://lucene.apache.org/solr/),
[Elasticsearch](https://www.elastic.co/)
or [Whoosh](https://whoosh.readthedocs.io/en/latest/intro.html).

The django-haystack project is open source under the
[BSD license](https://github.com/django-haystack/django-haystack/blob/master/LICENSE).

[**django-haystack / haystack / admin.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/./admin.py)

```python
# admin.py
~~from django.contrib.admin.options import ModelAdmin, csrf_protect_m
from django.contrib.admin.views.main import SEARCH_VAR, ChangeList
from django.core.exceptions import PermissionDenied
from django.core.paginator import InvalidPage, Paginator
from django.shortcuts import render
from django.utils.encoding import force_str
from django.utils.translation import ungettext

from haystack import connections
from haystack.constants import DEFAULT_ALIAS
from haystack.query import SearchQuerySet
from haystack.utils import get_model_ct_tuple


class SearchChangeList(ChangeList):
    def __init__(self, **kwargs):
        self.haystack_connection = kwargs.pop("haystack_connection", DEFAULT_ALIAS)
        super(SearchChangeList, self).__init__(**kwargs)

    def get_results(self, request):
        if SEARCH_VAR not in request.GET:
            return super(SearchChangeList, self).get_results(request)

        sqs = (
            SearchQuerySet(self.haystack_connection)


## ... source file abbreviated to get to csrf_protect_m examples ...


        result_count = paginator.count
        full_result_count = (
            SearchQuerySet(self.haystack_connection).models(self.model).all().count()
        )

        can_show_all = result_count <= self.list_max_show_all
        multi_page = result_count > self.list_per_page

        try:
            result_list = paginator.page(self.page_num + 1).object_list
            result_list = [result.object for result in result_list]
        except InvalidPage:
            result_list = ()

        self.result_count = result_count
        self.full_result_count = full_result_count
        self.result_list = result_list
        self.can_show_all = can_show_all
        self.multi_page = multi_page
        self.paginator = paginator


class SearchModelAdminMixin(object):
    haystack_connection = DEFAULT_ALIAS

~~    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        if not self.has_change_permission(request, None):
            raise PermissionDenied

        if SEARCH_VAR not in request.GET:
            return super(SearchModelAdminMixin, self).changelist_view(
                request, extra_context
            )

        indexed_models = (
            connections[self.haystack_connection]
            .get_unified_index()
            .get_indexed_models()
        )

        if self.model not in indexed_models:
            return super(SearchModelAdminMixin, self).changelist_view(
                request, extra_context
            )

        list_display = list(self.list_display)

        kwargs = {
            "haystack_connection": self.haystack_connection,


## ... source file continues with no further csrf_protect_m examples...

```

