title: django.db.migrations.operations.base Operation Example Code
category: page
slug: django-db-migrations-operations-base-operation-examples
sortorder: 500011177
toc: False
sidebartitle: django.db.migrations.operations.base Operation
meta: Python example code for the Operation class from the django.db.migrations.operations.base module of the Django project.


Operation is a class within the django.db.migrations.operations.base module of the Django project.


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

[**django-migration-linter / django_migration_linter / operations.py**](https://github.com/3YOURMIND/django-migration-linter/blob/master/django_migration_linter/./operations.py)

```python
# operations.py
~~from django.db.migrations.operations.base import Operation


~~class IgnoreMigration(Operation):

    reversible = True
    reduces_to_sql = False

    def state_forwards(self, app_label, state):
        pass

    def database_forwards(self, app_label, schema_editor, from_state, to_state):
        pass

    def database_backwards(self, app_label, schema_editor, from_state, to_state):
        pass

    def describe(self):
        return "The Django migration linter will ignore this migration"



## ... source file continues with no further Operation examples...

```

