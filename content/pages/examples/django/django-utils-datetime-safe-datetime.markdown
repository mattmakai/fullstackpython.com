title: django.utils.datetime_safe datetime Example Code
category: page
slug: django-utils-datetime-safe-datetime-examples
sortorder: 500011435
toc: False
sidebartitle: django.utils.datetime_safe datetime
meta: Python example code for the datetime callable from the django.utils.datetime_safe module of the Django project.


datetime is a callable within the django.utils.datetime_safe module of the Django project.


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

[**django-haystack / haystack / backends / whoosh_backend.py**](https://github.com/django-haystack/django-haystack/blob/master/haystack/backends/whoosh_backend.py)

```python
# whoosh_backend.py
import json
import os
import re
import shutil
import threading
import warnings

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
~~from django.utils.datetime_safe import datetime
from django.utils.encoding import force_str

from haystack.backends import (
    BaseEngine,
    BaseSearchBackend,
    BaseSearchQuery,
    EmptyResults,
    log_query,
)
from haystack.constants import (
    DJANGO_CT,
    DJANGO_ID,
    FUZZY_WHOOSH_MAX_EDITS,
    FUZZY_WHOOSH_MIN_PREFIX,
    ID,
)
from haystack.exceptions import MissingDependency, SearchBackendError, SkipDocument
from haystack.inputs import Clean, Exact, PythonData, Raw
from haystack.models import SearchResult
from haystack.utils import get_identifier, get_model_ct
from haystack.utils import log as logging
from haystack.utils.app_loading import haystack_get_model

try:


## ... source file abbreviated to get to datetime examples ...



        if not query_string:
            return spelling_suggestion

        for rev_word in self.RESERVED_WORDS:
            cleaned_query = cleaned_query.replace(rev_word, "")

        for rev_char in self.RESERVED_CHARACTERS:
            cleaned_query = cleaned_query.replace(rev_char, "")

        query_words = cleaned_query.split()
        suggested_words = []

        for word in query_words:
            suggestions = corrector.suggest(word, limit=1)

            if len(suggestions) > 0:
                suggested_words.append(suggestions[0])

        spelling_suggestion = " ".join(suggested_words)
        return spelling_suggestion

    def _from_python(self, value):
        if hasattr(value, "strftime"):
            if not hasattr(value, "hour"):
~~                value = datetime(value.year, value.month, value.day, 0, 0, 0)
        elif isinstance(value, bool):
            if value:
                value = "true"
            else:
                value = "false"
        elif isinstance(value, (list, tuple)):
            value = ",".join([force_str(v) for v in value])
        elif isinstance(value, (int, float)):
            pass
        else:
            value = force_str(value)
        return value

    def _to_python(self, value):
        if value == "true":
            return True
        elif value == "false":
            return False

        if value and isinstance(value, str):
            possible_datetime = DATETIME_REGEX.search(value)

            if possible_datetime:
                date_values = possible_datetime.groupdict()

                for dk, dv in date_values.items():
                    date_values[dk] = int(dv)

~~                return datetime(
                    date_values["year"],
                    date_values["month"],
                    date_values["day"],
                    date_values["hour"],
                    date_values["minute"],
                    date_values["second"],
                )

        try:
            converted_value = json.loads(value)

            if isinstance(
                converted_value,
                (list, tuple, set, dict, int, float, complex),
            ):
                return converted_value
        except:
            pass

        return value


class WhooshSearchQuery(BaseSearchQuery):
    def _convert_datetime(self, date):


## ... source file continues with no further datetime examples...

```

