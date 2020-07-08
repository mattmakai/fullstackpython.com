title: django.db.models.query_utils DeferredAttribute Example Code
category: page
slug: django-db-models-query-utils-deferredattribute-examples
sortorder: 500011245
toc: False
sidebartitle: django.db.models.query_utils DeferredAttribute
meta: Python example code for the DeferredAttribute class from the django.db.models.query_utils module of the Django project.


DeferredAttribute is a class within the django.db.models.query_utils module of the Django project.


## Example 1 from django-model-utils
[django-model-utils](https://github.com/jazzband/django-model-utils)
([project documentation](https://django-model-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-model-utils/))
provides useful mixins and utilities for working with
[Django ORM](/django-orm.html) models in your projects.

The django-model-utils project is open sourced under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/jazzband/django-model-utils/blob/master/LICENSE.txt).

[**django-model-utils / model_utils / tracker.py**](https://github.com/jazzband/django-model-utils/blob/master/model_utils/./tracker.py)

```python
# tracker.py
from copy import deepcopy
from functools import wraps

import django
from django.core.exceptions import FieldError
from django.db import models
from django.db.models.fields.files import FileDescriptor
~~from django.db.models.query_utils import DeferredAttribute


class DescriptorMixin:
    tracker_instance = None

    def __get__(self, instance, owner):
        if instance is None:
            return self
        was_deferred = False
        field_name = self._get_field_name()
        if field_name in instance._deferred_fields:
            instance._deferred_fields.remove(field_name)
            was_deferred = True
        value = super().__get__(instance, owner)
        if was_deferred:
            self.tracker_instance.saved_data[field_name] = deepcopy(value)
        return value

    def _get_field_name(self):
        return self.field_name


class DescriptorWrapper:



## ... source file abbreviated to get to DeferredAttribute examples ...


        if self.instance.pk and field in self.deferred_fields and field not in self.saved_data:

            if field not in self.instance.__dict__:
                self.get_field_value(field)

            else:
                current_value = self.get_field_value(field)
                self.instance.refresh_from_db(fields=[field])
                self.saved_data[field] = deepcopy(self.get_field_value(field))
                setattr(self.instance, self.field_map[field], current_value)

        return self.saved_data.get(field)

    def changed(self):
        return {
            field: self.previous(field)
            for field in self.fields
            if self.has_changed(field)
        }

    def init_deferred_fields(self):
        self.instance._deferred_fields = set()
        if hasattr(self.instance, '_deferred') and not self.instance._deferred:
            return

~~        class DeferredAttributeTracker(DescriptorMixin, DeferredAttribute):
            tracker_instance = self

        class FileDescriptorTracker(DescriptorMixin, FileDescriptor):
            tracker_instance = self

            def _get_field_name(self):
                return self.field.name

        self.instance._deferred_fields = self.instance.get_deferred_fields()
        for field in self.instance._deferred_fields:
            field_obj = self.instance.__class__.__dict__.get(field)
            if isinstance(field_obj, FileDescriptor):
                field_tracker = FileDescriptorTracker(field_obj.field)
                setattr(self.instance.__class__, field, field_tracker)
            else:
                field_tracker = DeferredAttributeTracker(field)
                setattr(self.instance.__class__, field, field_tracker)


class FieldTracker:

    tracker_class = FieldInstanceTracker

    def __init__(self, fields=None):


## ... source file continues with no further DeferredAttribute examples...

```

