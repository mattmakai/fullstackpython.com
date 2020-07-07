title: django.db DEFAULT_DB_ALIAS Example Code
category: page
slug: django-db-default-db-alias-examples
sortorder: 500011158
toc: False
sidebartitle: django.db DEFAULT_DB_ALIAS
meta: Python example code for the DEFAULT_DB_ALIAS constant from the django.db module of the Django project.


DEFAULT_DB_ALIAS is a constant within the django.db module of the Django project.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog / models.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/models.py)

```python
# models.py
from __future__ import unicode_literals

import json
import ast

from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import FieldDoesNotExist
~~from django.db import models, DEFAULT_DB_ALIAS
from django.db.models import QuerySet, Q
from django.utils import formats, timezone
from django.utils.encoding import python_2_unicode_compatible, smart_text
from django.utils.six import iteritems, integer_types
from django.utils.translation import ugettext_lazy as _

from jsonfield.fields import JSONField
from dateutil import parser
from dateutil.tz import gettz


class LogEntryManager(models.Manager):

    def log_create(self, instance, **kwargs):
        changes = kwargs.get('changes', None)
        pk = self._get_pk_value(instance)

        if changes is not None:
            kwargs.setdefault('content_type', ContentType.objects.get_for_model(instance))
            kwargs.setdefault('object_pk', pk)
            kwargs.setdefault('object_repr', smart_text(instance))

            if isinstance(pk, integer_types):
                kwargs.setdefault('object_id', pk)


## ... source file continues with no further DEFAULT_DB_ALIAS examples...

```


## Example 2 from django-import-export
[django-import-export](https://github.com/django-import-export/django-import-export)
([documentation](https://django-import-export.readthedocs.io/en/latest/)
and [PyPI page](https://pypi.org/project/django-import-export/))
is a [Django](/django.html) code library for importing and exporting data
from the Django Admin. The tool supports many export and import formats
such as CSV, JSON and YAML. django-import-export is open source under the
[BSD 2-Clause "Simplified" License](https://github.com/django-import-export/django-import-export/blob/master/LICENSE).

[**django-import-export / import_export / resources.py**](https://github.com/django-import-export/django-import-export/blob/master/import_export/./resources.py)

```python
# resources.py
import functools
import logging
import tablib
import traceback
from collections import OrderedDict
from copy import deepcopy

from diff_match_patch import diff_match_patch

import django
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.core.management.color import no_style
from django.core.paginator import Paginator
~~from django.db import DEFAULT_DB_ALIAS, connections
from django.db.models.fields.related import ForeignObjectRel
from django.db.models.query import QuerySet
from django.db.transaction import (
    TransactionManagementError,
    atomic,
    savepoint,
    savepoint_commit,
    savepoint_rollback
)
from django.utils.encoding import force_str
from django.utils.safestring import mark_safe

from . import widgets
from .fields import Field
from .instance_loaders import ModelInstanceLoader
from .results import Error, Result, RowResult
from .utils import atomic_if_using_transaction

if django.VERSION[0] >= 3:
    from django.core.exceptions import FieldDoesNotExist
else:
    from django.db.models.fields import FieldDoesNotExist




## ... source file continues with no further DEFAULT_DB_ALIAS examples...

```


## Example 3 from django-migration-linter
[django-migration-linter](https://github.com/3YOURMIND/django-migration-linter)
([PyPI package information](https://pypi.org/project/django-migration-linter/))
checks for backwards-incompatible changes in [Django ORM](/django-orm.html)
schema migrations and warns you about them. The purpose of the project is
to save time in older and larger projects by detecting field migrations
that will be a problem so you do not run into issues later, and make it
easier to enable continuous [deployment](/deployment.html) configurations
with database changes. There is a
[blog post on keeping Django database migrations backward compatible](https://medium.com/3yourmind/keeping-django-database-migrations-backward-compatible-727820260dbb)
that goes into further detail on the tool.

The django-migration-linter project is open sourced under the
[Apache 2.0 license](https://github.com/3YOURMIND/django-migration-linter/blob/master/LICENSE).

[**django-migration-linter / django_migration_linter / migration_linter.py**](https://github.com/3YOURMIND/django-migration-linter/blob/master/django_migration_linter/./migration_linter.py)

```python
# migration_linter.py
from __future__ import print_function

import hashlib
import inspect
import logging
import os
import re
from subprocess import Popen, PIPE

from django.conf import settings
from django.core.management import call_command
~~from django.db import DEFAULT_DB_ALIAS, connections, ProgrammingError
from django.db.migrations import RunPython
from enum import Enum, unique
from six import PY2

from .cache import Cache
from .constants import (
    DEFAULT_CACHE_PATH,
    EXPECTED_DATA_MIGRATION_ARGS,
    DJANGO_APPS_WITH_MIGRATIONS,
)
from .utils import clean_bytes_to_str, get_migration_abspath, split_migration_path
from .operations import IgnoreMigration
from .sql_analyser import analyse_sql_statements

logger = logging.getLogger(__name__)


@unique
class MessageType(Enum):
    OK = "ok"
    IGNORE = "ignore"
    WARNING = "warning"
    ERROR = "error"



## ... source file continues with no further DEFAULT_DB_ALIAS examples...

```

