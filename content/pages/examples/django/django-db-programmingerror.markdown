title: django.db ProgrammingError Example Code
category: page
slug: django-db-programmingerror-examples
sortorder: 500011163
toc: False
sidebartitle: django.db ProgrammingError
meta: Python example code for the ProgrammingError class from the django.db module of the Django project.


ProgrammingError is a class within the django.db module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / appresolver.py**](https://github.com/divio/django-cms/blob/develop/cms/./appresolver.py)

```python
# appresolver.py
from collections import OrderedDict
from importlib import import_module

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
~~from django.db import OperationalError, ProgrammingError
from django.utils.translation import get_language, override
from django.urls import Resolver404, reverse

from six import string_types

from cms.apphook_pool import apphook_pool
from cms.models.pagemodel import Page
from cms.utils import get_current_site
from cms.utils.compat import DJANGO_1_11
from cms.utils.compat.dj import RegexPattern, URLPattern, URLResolver
from cms.utils.i18n import get_language_list
from cms.utils.moderator import use_draft


APP_RESOLVERS = []


def clear_app_resolvers():
    global APP_RESOLVERS
    APP_RESOLVERS = []


def applications_page_check(request, current_page=None, path=None):
    if current_page:


## ... source file abbreviated to get to ProgrammingError examples ...


            if not hasattr(mod, 'urlpatterns'):
                raise ImproperlyConfigured(
                    "URLConf `%s` has no urlpatterns attribute" % urlconf)
            yield getattr(mod, 'urlpatterns')
        elif isinstance(urlconf, (list, tuple)):
            yield urlconf
        else:
            yield [urlconf]


def get_patterns_for_title(path, title):
    app = apphook_pool.get_apphook(title.page.application_urls)
    url_patterns = []
    for pattern_list in get_app_urls(app.get_urls(title.page, title.language)):
        if path and not path.endswith('/'):
            path += '/'
        page_id = title.page.id
        url_patterns += recurse_patterns(path, pattern_list, page_id)
    return url_patterns


def get_app_patterns():
    try:
        site = get_current_site()
        return _get_app_patterns(site)
~~    except (OperationalError, ProgrammingError):
        return []


def _get_app_patterns(site):
    from cms.models import Title

    included = []

    title_qs = Title.objects.public().filter(page__node__site=site)

    hooked_applications = OrderedDict()

    titles = (title_qs.exclude(page__application_urls=None)
              .exclude(page__application_urls='')
              .order_by('-page__node__path').select_related())
    for title in titles:
        path = title.path
        mix_id = "%s:%s:%s" % (
            path + "/", title.page.application_urls, title.language)
        if mix_id in included:
            continue
        if not settings.APPEND_SLASH:
            path += '/'
        app = apphook_pool.get_apphook(title.page.application_urls)


## ... source file continues with no further ProgrammingError examples...

```


## Example 2 from django-migration-linter
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



## ... source file abbreviated to get to ProgrammingError examples ...


    def print_summary(self):
        print()
        print("*** Summary ***")
        print("Valid migrations: {}/{}".format(self.nb_valid, self.nb_total))
        print("Erroneous migrations: {}/{}".format(self.nb_erroneous, self.nb_total))
        print("Migrations with warnings: {}/{}".format(self.nb_warnings, self.nb_total))
        print("Ignored migrations: {}/{}".format(self.nb_ignored, self.nb_total))

    @property
    def has_errors(self):
        return self.nb_erroneous > 0

    def get_sql(self, app_label, migration_name):
        logger.info(
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
~~        except (ValueError, ProgrammingError):
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
        from django.db.migrations.loader import MIGRATIONS_MODULE_NAME

        return (
            re.search(r"/{0}/.*\.py".format(MIGRATIONS_MODULE_NAME), filename)
            and "__init__" not in filename
        )

    @classmethod
    def read_migrations_list(cls, migrations_file_path):
        if not migrations_file_path:
            return None


## ... source file continues with no further ProgrammingError examples...

```

