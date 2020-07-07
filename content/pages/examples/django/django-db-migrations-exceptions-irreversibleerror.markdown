title: django.db.migrations.exceptions IrreversibleError Example Code
category: page
slug: django-db-migrations-exceptions-irreversibleerror-examples
sortorder: 500011173
toc: False
sidebartitle: django.db.migrations.exceptions IrreversibleError
meta: Python example code for the IrreversibleError class from the django.db.migrations.exceptions module of the Django project.


IrreversibleError is a class within the django.db.migrations.exceptions module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / migrations / __init__.py**](https://github.com/divio/django-cms/blob/develop/cms/migrations/__init__.py)

```python
# __init__.py
from django.db import migrations

try:
    IrreversibleError = migrations.Migration.IrreversibleError
except AttributeError:
~~    from django.db.migrations.exceptions import IrreversibleError


class IrreversibleMigration(migrations.Migration):

    def unapply(self, project_state, schema_editor, collect_sql=False):
~~        raise IrreversibleError('Migration %s is not reversible' % self.name)



## ... source file continues with no further IrreversibleError examples...

```

