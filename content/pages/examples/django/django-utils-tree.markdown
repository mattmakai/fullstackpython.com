title: django.utils tree Example Code
category: page
slug: django-utils-tree-examples
sortorder: 500011423
toc: False
sidebartitle: django.utils tree
meta: Python example code for the tree callable from the django.utils module of the Django project.


tree is a callable within the django.utils module of the Django project.


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

[**django-haystack / haystack / backends / __init__.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/backends/__init__.py)

```python
# __init__.py
import copy
from copy import deepcopy
from time import time

from django.conf import settings
from django.db.models import Q
from django.db.models.base import ModelBase
~~from django.utils import tree
from django.utils.encoding import force_str

from haystack.constants import VALID_FILTERS, FILTER_SEPARATOR, DEFAULT_ALIAS
from haystack.exceptions import MoreLikeThisError, FacetingError
from haystack.models import SearchResult
from haystack.utils.loading import UnifiedIndex
from haystack.utils import get_model_ct

VALID_GAPS = ["year", "month", "day", "hour", "minute", "second"]

SPELLING_SUGGESTION_HAS_NOT_RUN = object()


def log_query(func):

    def wrapper(obj, query_string, *args, **kwargs):
        start = time()

        try:
            return func(obj, query_string, *args, **kwargs)
        finally:
            stop = time()

            if settings.DEBUG:


## ... source file abbreviated to get to tree examples ...


        if " " in query_string:
            query_string = "(%s)" % query_string

        return "NOT %s" % query_string

    def build_exact_query(self, query_string):
        return '"%s"' % query_string

    def add_filter(self, query_filter, use_or=False):
        if use_or:
            connector = SQ.OR
        else:
            connector = SQ.AND

        if (
            self.query_filter
            and query_filter.connector != connector
            and len(query_filter) > 1
        ):
            self.query_filter.start_subtree(connector)
            subtree = True
        else:
            subtree = False

        for child in query_filter.children:
~~            if isinstance(child, tree.Node):
                self.query_filter.start_subtree(connector)
                self.add_filter(child)
                self.query_filter.end_subtree()
            else:
                expression, value = child
                self.query_filter.add((expression, value), connector)

            connector = query_filter.connector

        if query_filter.negated:
            self.query_filter.negate()

        if subtree:
            self.query_filter.end_subtree()

    def add_order_by(self, field):
        self.order_by.append(field)

    def clear_order_by(self):
        self.order_by = []

    def add_model(self, model):
        if not isinstance(model, ModelBase):
            raise AttributeError(


## ... source file continues with no further tree examples...

```

