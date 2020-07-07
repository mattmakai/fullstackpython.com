title: django.db.migrations RunPython Example Code
category: page
slug: django-db-migrations-runpython-examples
sortorder: 500011171
toc: False
sidebartitle: django.db.migrations RunPython
meta: Python example code for the RunPython class from the django.db.migrations module of the Django project.


RunPython is a class within the django.db.migrations module of the Django project.


## Example 1 from django-migration-linter
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
from django.db import DEFAULT_DB_ALIAS, connections, ProgrammingError
~~from django.db.migrations import RunPython
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

    @staticmethod


## ... source file abbreviated to get to RunPython examples ...


            or (self.exclude_apps and app_label in self.exclude_apps)
            or any(isinstance(o, IgnoreMigration) for o in operations)
            or (
                self.ignore_name_contains
                and self.ignore_name_contains in migration_name
            )
            or (migration_name in self.ignore_name)
            or (
                self.only_applied_migrations
                and (app_label, migration_name)
                not in self.migration_loader.applied_migrations
            )
            or (
                self.only_unapplied_migrations
                and (app_label, migration_name)
                in self.migration_loader.applied_migrations
            )
        )

    def analyse_data_migration(self, migration):
        errors = []
        ignored = []
        warnings = []

        for operation in migration.operations:
~~            if isinstance(operation, RunPython):
                op_errors, op_ignored, op_warnings = self.lint_runpython(operation)
                if op_errors:
                    errors += op_errors
                if op_ignored:
                    ignored += op_ignored
                if op_warnings:
                    warnings += op_warnings

        return errors, ignored, warnings

    def lint_runpython(self, runpython):
        function_name = runpython.code.__name__
        error = []
        ignored = []
        warning = []

        if not runpython.reversible:
            issue = {
                "code": "REVERSIBLE_DATA_MIGRATION",
                "msg": "'{}': RunPython data migration is not reversible".format(
                    function_name
                ),
            }
            if issue["code"] in self.exclude_migration_tests:


## ... source file continues with no further RunPython examples...

```

