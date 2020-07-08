title: django.forms Field Example Code
category: page
slug: django-forms-field-examples
sortorder: 500011264
toc: False
sidebartitle: django.forms Field
meta: Python example code for the Field class from the django.forms module of the Django project.


Field is a class within the django.forms module of the Django project.


## Example 1 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / forms.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/./forms.py)

```python
# forms.py
from django.db import DatabaseError
~~from django.forms import ModelForm, Field, ValidationError, BooleanField, CharField
from django.forms.widgets import CheckboxInput, Select

from explorer.app_settings import EXPLORER_DEFAULT_CONNECTION, EXPLORER_CONNECTIONS
from explorer.models import Query, MSG_FAILED_BLACKLIST


~~class SqlField(Field):

    def validate(self, value):

        query = Query(sql=value)

        passes_blacklist, failing_words = query.passes_blacklist()

        error = MSG_FAILED_BLACKLIST % ', '.join(failing_words) if not passes_blacklist else None

        if error:
            raise ValidationError(
                error,
                code="InvalidSql"
            )


class QueryForm(ModelForm):

    sql = SqlField()
    snapshot = BooleanField(widget=CheckboxInput, required=False)
    connection = CharField(widget=Select, required=False)

    def __init__(self, *args, **kwargs):
        super(QueryForm, self).__init__(*args, **kwargs)


## ... source file continues with no further Field examples...

```

