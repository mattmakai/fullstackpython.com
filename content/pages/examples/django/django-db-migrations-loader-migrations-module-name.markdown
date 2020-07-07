title: django.db.migrations.loader MIGRATIONS_MODULE_NAME Example Code
category: page
slug: django-db-migrations-loader-migrations-module-name-examples
sortorder: 500011175
toc: False
sidebartitle: django.db.migrations.loader MIGRATIONS_MODULE_NAME
meta: Python example code for the MIGRATIONS_MODULE_NAME constant from the django.db.migrations.loader module of the Django project.


MIGRATIONS_MODULE_NAME is a constant within the django.db.migrations.loader module of the Django project.


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


## ... source file abbreviated to get to MIGRATIONS_MODULE_NAME examples ...


            "Calling sqlmigrate command {} {}".format(app_label, migration_name)
        )
        dev_null = open(os.devnull, "w")
        try:
            sql_statement = call_command(
                "sqlmigrate",
                app_label,
                migration_name,
                database=self.database,
                stdout=dev_null,
            )
        except (ValueError, ProgrammingError):
            logger.warning(
                (
                    "Error while executing sqlmigrate on (%s, %s). "
                    "Continuing execution with empty SQL."
                ),
                app_label,
                migration_name,
            )
            sql_statement = ""
        return sql_statement.splitlines()

    @staticmethod
    def is_migration_file(filename):
~~        from django.db.migrations.loader import MIGRATIONS_MODULE_NAME

        return (
~~            re.search(r"/{0}/.*\.py".format(MIGRATIONS_MODULE_NAME), filename)
            and "__init__" not in filename
        )

    @classmethod
    def read_migrations_list(cls, migrations_file_path):
        if not migrations_file_path:
            return None

        migrations = []
        try:
            with open(migrations_file_path, "r") as file:
                for line in file:
                    if cls.is_migration_file(line):
                        app_label, name = split_migration_path(line)
                        migrations.append((app_label, name))
        except IOError:
            logger.exception("Migrations list path not found %s", migrations_file_path)
            raise Exception("Error while reading migrations list file")

        if not migrations:
            logger.info(
                "No valid migration paths found in the migrations file %s",
                migrations_file_path,
            )


## ... source file continues with no further MIGRATIONS_MODULE_NAME examples...

```

