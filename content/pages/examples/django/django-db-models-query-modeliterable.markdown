title: django.db.models.query ModelIterable Example Code
category: page
slug: django-db-models-query-modeliterable-examples
sortorder: 500011240
toc: False
sidebartitle: django.db.models.query ModelIterable
meta: Python example code for the ModelIterable class from the django.db.models.query module of the Django project.


ModelIterable is a class within the django.db.models.query module of the Django project.


## Example 1 from django-model-utils
[django-model-utils](https://github.com/jazzband/django-model-utils)
([project documentation](https://django-model-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-model-utils/))
provides useful mixins and utilities for working with
[Django ORM](/django-orm.html) models in your projects.

The django-model-utils project is open sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/jazzband/django-model-utils/blob/master/LICENSE.txt).

[**django-model-utils / model_utils / managers.py**](https://github.com/jazzband/django-model-utils/blob/master/model_utils/./managers.py)

```python
# managers.py
import django
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection
from django.db import models
from django.db.models.constants import LOOKUP_SEP
from django.db.models.fields.related import OneToOneField, OneToOneRel
~~from django.db.models.query import ModelIterable
from django.db.models.query import QuerySet
from django.db.models.sql.datastructures import Join


~~class InheritanceIterable(ModelIterable):
    def __iter__(self):
        queryset = self.queryset
~~        iter = ModelIterable(queryset)
        if getattr(queryset, 'subclasses', False):
            extras = tuple(queryset.query.extra.keys())
            subclasses = sorted(queryset.subclasses, key=len, reverse=True)
            for obj in iter:
                sub_obj = None
                for s in subclasses:
                    sub_obj = queryset._get_sub_obj_recurse(obj, s)
                    if sub_obj:
                        break
                if not sub_obj:
                    sub_obj = obj

                if getattr(queryset, '_annotated', False):
                    for k in queryset._annotated:
                        setattr(sub_obj, k, getattr(obj, k))

                for k in extras:
                    setattr(sub_obj, k, getattr(obj, k))

                yield sub_obj
        else:
            yield from iter




## ... source file continues with no further ModelIterable examples...

```

