title: django.contrib.admin.options ModelAdmin code examples
category: page
slug: django-contrib-admin-options-modeladmin-examples
sortorder: 500011024
toc: False
sidebartitle: django.contrib.admin.options ModelAdmin
meta: Python example code for the ModelAdmin class from the django.contrib.admin.options module of the Django project.


ModelAdmin is a class within the django.contrib.admin.options module of the Django project.


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


## ... source file abbreviated to get to ModelAdmin examples ...


            "cl": changelist,
            "media": media,
            "has_add_permission": self.has_add_permission(request),
            "opts": changelist.opts,
            "app_label": self.model._meta.app_label,
            "action_form": action_form,
            "actions_on_top": self.actions_on_top,
            "actions_on_bottom": self.actions_on_bottom,
            "actions_selection_counter": getattr(self, "actions_selection_counter", 0),
        }
        context.update(extra_context or {})
        request.current_app = self.admin_site.name
        app_name, model_name = get_model_ct_tuple(self.model)
        return render(
            request,
            self.change_list_template
            or [
                "admin/%s/%s/change_list.html" % (app_name, model_name),
                "admin/%s/change_list.html" % app_name,
                "admin/change_list.html",
            ],
            context,
        )


~~class SearchModelAdmin(SearchModelAdminMixin, ModelAdmin):
    pass



## ... source file continues with no further ModelAdmin examples...

```

