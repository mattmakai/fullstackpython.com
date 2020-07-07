title: django.db.migrations.state ProjectState Example Code
category: page
slug: django-db-migrations-state-projectstate-examples
sortorder: 500011178
toc: False
sidebartitle: django.db.migrations.state ProjectState
meta: Python example code for the ProjectState class from the django.db.migrations.state module of the Django project.


ProjectState is a class within the django.db.migrations.state module of the Django project.


## Example 1 from django-axes
[django-axes](https://github.com/jazzband/django-axes/)
([project documentation](https://django-axes.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-axes/)
is a code library for [Django](/django.html) projects to track failed
login attempts against a web application. The goal of the project is
to make it easier for you to stop people and scripts from hacking your
Django-powered website.

The code for django-axes is
[open source under the MIT license](https://github.com/jazzband/django-axes/blob/master/LICENSE)
and maintained by the group of developers known as
[Jazzband](https://jazzband.co/).

[**django-axes / axes / tests / test_models.py**](https://github.com/jazzband/django-axes/blob/master/axes/tests/test_models.py)

```python
# test_models.py
from django.apps.registry import apps
from django.db import connection
from django.db.migrations.autodetector import MigrationAutodetector
from django.db.migrations.executor import MigrationExecutor
~~from django.db.migrations.state import ProjectState

from axes.models import AccessAttempt, AccessLog
from axes.tests.base import AxesTestCase


class ModelsTestCase(AxesTestCase):
    def setUp(self):
        self.failures_since_start = 42

        self.access_attempt = AccessAttempt(
            failures_since_start=self.failures_since_start
        )
        self.access_log = AccessLog()

    def test_access_attempt_str(self):
        self.assertIn("Access", str(self.access_attempt))

    def test_access_log_str(self):
        self.assertIn("Access", str(self.access_log))


class MigrationsTestCase(AxesTestCase):
    def test_missing_migrations(self):
        executor = MigrationExecutor(connection)
        autodetector = MigrationAutodetector(
~~            executor.loader.project_state(), ProjectState.from_apps(apps)
        )

        changes = autodetector.changes(graph=executor.loader.graph)

        self.assertEqual({}, changes)



## ... source file continues with no further ProjectState examples...

```

