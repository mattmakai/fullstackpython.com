title: django.views.generic.list MultipleObjectMixin Example Code
category: page
slug: django-views-generic-list-multipleobjectmixin-examples
sortorder: 500011540
toc: False
sidebartitle: django.views.generic.list MultipleObjectMixin
meta: Python example code for the MultipleObjectMixin class from the django.views.generic.list module of the Django project.


MultipleObjectMixin is a class within the django.views.generic.list module of the Django project.


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

[**django-haystack / haystack / generic_views.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/./generic_views.py)

```python
# generic_views.py
from django.conf import settings
from django.core.paginator import Paginator
from django.views.generic import FormView
from django.views.generic.edit import FormMixin
~~from django.views.generic.list import MultipleObjectMixin

from .forms import FacetedSearchForm, ModelSearchForm
from .query import SearchQuerySet

RESULTS_PER_PAGE = getattr(settings, "HAYSTACK_SEARCH_RESULTS_PER_PAGE", 20)


~~class SearchMixin(MultipleObjectMixin, FormMixin):

    template_name = "search/search.html"
    load_all = True
    form_class = ModelSearchForm
    context_object_name = None
    paginate_by = RESULTS_PER_PAGE
    paginate_orphans = 0
    paginator_class = Paginator
    page_kwarg = "page"
    form_name = "form"
    search_field = "q"
    object_list = None

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = SearchQuerySet()
        return self.queryset

    def get_form_kwargs(self):
        kwargs = {"initial": self.get_initial()}
        if self.request.method == "GET":
            kwargs.update({"data": self.request.GET})
        kwargs.update(
            {"searchqueryset": self.get_queryset(), "load_all": self.load_all}


## ... source file continues with no further MultipleObjectMixin examples...

```

