title: django.db.migrations.loader MigrationLoader Example Code
category: page
slug: django-db-migrations-loader-migrationloader-examples
sortorder: 500011176
toc: False
sidebartitle: django.db.migrations.loader MigrationLoader
meta: Python example code for the MigrationLoader class from the django.db.migrations.loader module of the Django project.


MigrationLoader is a class within the django.db.migrations.loader module of the Django project.


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


## ... source file abbreviated to get to MigrationLoader examples ...


        exclude_migration_tests=None,
        quiet=None,
        warnings_as_errors=False,
    ):
        self.django_path = path
        self.ignore_name_contains = ignore_name_contains
        self.ignore_name = ignore_name or tuple()
        self.include_apps = include_apps
        self.exclude_apps = exclude_apps
        self.exclude_migration_tests = exclude_migration_tests or []
        self.database = database or DEFAULT_DB_ALIAS
        self.cache_path = cache_path or DEFAULT_CACHE_PATH
        self.no_cache = no_cache
        self.only_applied_migrations = only_applied_migrations
        self.only_unapplied_migrations = only_unapplied_migrations
        self.quiet = quiet or []
        self.warnings_as_errors = warnings_as_errors

        self.reset_counters()

        if self.should_use_cache():
            self.old_cache = Cache(self.django_path, self.database, self.cache_path)
            self.new_cache = Cache(self.django_path, self.database, self.cache_path)
            self.old_cache.load()

~~        from django.db.migrations.loader import MigrationLoader

~~        self.migration_loader = MigrationLoader(
            connection=connections[self.database], load=True
        )

    def reset_counters(self):
        self.nb_valid = 0
        self.nb_ignored = 0
        self.nb_warnings = 0
        self.nb_erroneous = 0
        self.nb_total = 0

    def should_use_cache(self):
        return self.django_path and not self.no_cache

    def lint_all_migrations(self, git_commit_id=None, migrations_file_path=None):
        migrations_list = self.read_migrations_list(migrations_file_path)
        if git_commit_id:
            migrations = self._gather_migrations_git(git_commit_id, migrations_list)
        else:
            migrations = self._gather_all_migrations(migrations_list)

        sorted_migrations = sorted(
            migrations, key=lambda migration: (migration.app_label, migration.name)
        )
        for m in sorted_migrations:


## ... source file continues with no further MigrationLoader examples...

```

