title: django.db.models PositiveSmallIntegerField Python Code Examples
category: page
slug: django-db-models-positivesmallintegerfield-examples
sortorder: 500012890
toc: False
sidebartitle: django.db.models PositiveSmallIntegerField
meta: Python code examples for the PositiveSmallIntegerField class used in the Django ORM, found within the django.db.models module of the Django project. 


[PositiveSmallIntegerField](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
([documentation](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.PositiveIntegerField))
is a [Django ORM](/django-orm.html) mapping from your Python code to an
integer-type column in your [relational database](/databases.html)
that is restricted to only positive values from 0 to 2147483647.

Note that `PositiveSmallIntegerField` is defined within the 
[django.db.models.fields](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
module but is typically referenced from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than including the `fields` module reference.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog / models.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog/models.py)

```python
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


## ... source file abbreviated here to get to example code ...


@python_2_unicode_compatible
class LogEntry(models.Model):
    """
    Represents an entry in the audit log. The content type is saved along with the textual and numeric (if available)
    primary key, as well as the textual representation of the object when it was saved. It holds the action performed
    and the fields that were changed in the transaction.

    If AuditlogMiddleware is used, the actor will be set automatically. Keep in mind that editing / re-saving LogEntry
    instances may set the actor to a wrong value - editing LogEntry instances is not recommended (and it should not be
    necessary).
    """

    class Action:
        """
        The actions that Auditlog distinguishes: creating, updating and deleting objects. Viewing objects is not logged.
        The values of the actions are numeric, a higher integer value means a more intrusive action. This may be useful
        in some cases when comparing actions because the ``__lt``, ``__lte``, ``__gt``, ``__gte`` lookup filters can be
        used in queries.

        The valid actions are :py:attr:`Action.CREATE`, :py:attr:`Action.UPDATE` and :py:attr:`Action.DELETE`.
        """
        CREATE = 0
        UPDATE = 1
        DELETE = 2

        choices = (
            (CREATE, _("create")),
            (UPDATE, _("update")),
            (DELETE, _("delete")),
        )

    content_type = models.ForeignKey(to='contenttypes.ContentType', on_delete=models.CASCADE, related_name='+', verbose_name=_("content type"))
    object_pk = models.CharField(db_index=True, max_length=255, verbose_name=_("object pk"))
    object_id = models.BigIntegerField(blank=True, db_index=True, null=True, verbose_name=_("object id"))
    object_repr = models.TextField(verbose_name=_("object representation"))
~~    action = models.PositiveSmallIntegerField(choices=Action.choices, verbose_name=_("action"))
    changes = models.TextField(blank=True, verbose_name=_("change message"))
    actor = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name='+', verbose_name=_("actor"))
    remote_addr = models.GenericIPAddressField(blank=True, null=True, verbose_name=_("remote address"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("timestamp"))
    additional_data = JSONField(blank=True, null=True, verbose_name=_("additional data"))

    objects = LogEntryManager()

    class Meta:
        get_latest_by = 'timestamp'
        ordering = ['-timestamp']
        verbose_name = _("log entry")
        verbose_name_plural = _("log entries")

~~    def __str__(self):
~~        if self.action == self.Action.CREATE:
~~            fstring = _("Created {repr:s}")
~~        elif self.action == self.Action.UPDATE:
~~            fstring = _("Updated {repr:s}")
~~        elif self.action == self.Action.DELETE:
~~            fstring = _("Deleted {repr:s}")
~~        else:
~~            fstring = _("Logged {repr:s}")

~~        return fstring.format(repr=self.object_repr)

    @property
    def changes_dict(self):
        """
        :return: The changes recorded in this log entry as a dictionary object.
        """
        try:
            return json.loads(self.changes)
        except ValueError:
            return {}


## ... source file continues with no further examples ...

```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / migrations / 0002_auto_20140816_1918.py**](https://github.com/divio/django-cms/blob/develop/cms/migrations/0002_auto_20140816_1918.py)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import cms.models.static_placeholder
import cms.models.fields
from django.conf import settings
from django.contrib.auth import get_user_model
~~from django.db import models, migrations
import django.utils.timezone

User = get_user_model()

user_model_label = '%s.%s' % (User._meta.app_label, User._meta.model_name)
user_ptr_name = '%s_ptr' % User._meta.object_name.lower()


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageUser',
            fields=[
                (user_ptr_name, models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, auto_created=True, parent_link=True, serialize=False, on_delete=models.CASCADE)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='created_users', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'User (page)',
                'verbose_name_plural': 'Users (page)',
            },
            bases=(user_model_label,),
        ),
        migrations.CreateModel(
            name='PageUserGroup',
            fields=[
                ('group_ptr', models.OneToOneField(primary_key=True, to='auth.Group', auto_created=True, parent_link=True, serialize=False, on_delete=models.CASCADE)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='created_usergroups', on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'User group (page)',
                'verbose_name_plural': 'User groups (page)',
            },
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Placeholder',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('slot', models.CharField(db_index=True, max_length=50, verbose_name='slot', editable=False)),
~~                ('default_width', models.PositiveSmallIntegerField(null=True, verbose_name='width', editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='page',
            name='placeholders',
            field=models.ManyToManyField(to='cms.Placeholder', editable=False),
            preserve_default=True,
        ),

## ... source file continues with no further examples ...

```


## Example 3 from django-floppyforms
[django-floppyforms](https://github.com/jazzband/django-floppyforms)
([project documentation](https://django-floppyforms.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-floppyforms/))
is a [Django](/django.html) code library for better control
over rendering HTML forms in your [templates](/template-engines.html).

The django-floppyforms code is provided as
[open source](https://github.com/jazzband/django-floppyforms/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-floppyforms / floppyforms / __future__ / models.py**](https://github.com/jazzband/django-floppyforms/blob/master/floppyforms/__future__/models.py)

```python
# flake8: noqa
import django
~~from django.db import models as db_models
from django.forms.models import (ModelForm as _ModelForm,
                                 ModelFormMetaclass as _ModelFormMetaclass,
                                 modelform_factory as _modelform_factory,
                                 modelformset_factory as _modelformset_factory,
                                 inlineformset_factory as _inlineformset_factory,
                                 model_to_dict, fields_for_model, BaseModelForm,
                                 BaseModelFormSet,
                                 BaseInlineFormSet)
if django.VERSION < (1, 9):
    from django.forms.models import save_instance
from django.utils import six

from floppyforms import fields
from floppyforms.forms import LayoutRenderer
from floppyforms.models import (ModelChoiceField, ModelMultipleChoiceField)
from floppyforms.widgets import Textarea


__all__ = (
    'ModelForm', 'BaseModelForm', 'model_to_dict', 'fields_for_model',
    'ModelChoiceField', 'ModelMultipleChoiceField',
    'BaseModelFormSet', 'modelformset_factory', 'BaseInlineFormSet',
    'inlineformset_factory',
)
if django.VERSION < (1, 9):
    __all__ += ('save_instance',)


if django.VERSION > (1, 7):
    from django.forms.models import ALL_FIELDS

    __all__ = __all__ + ('ALL_FIELDS',)


FORMFIELD_OVERRIDES = {
    db_models.BooleanField: {'form_class': fields.BooleanField},
    db_models.CharField: {'form_class': fields.CharField},
    db_models.CommaSeparatedIntegerField: {'form_class': fields.CharField},
    db_models.DateField: {'form_class': fields.DateField},
    db_models.DateTimeField: {'form_class': fields.DateTimeField},
    db_models.DecimalField: {'form_class': fields.DecimalField},
    db_models.EmailField: {'form_class': fields.EmailField},
    db_models.FilePathField: {'form_class': fields.FilePathField},
    db_models.FloatField: {'form_class': fields.FloatField},
    db_models.IntegerField: {'form_class': fields.IntegerField},
    db_models.BigIntegerField: {'form_class': fields.IntegerField},
    db_models.GenericIPAddressField: {'form_class': fields.GenericIPAddressField},
    db_models.NullBooleanField: {'form_class': fields.NullBooleanField},
    db_models.PositiveIntegerField: {'form_class': fields.IntegerField},
~~    db_models.PositiveSmallIntegerField: {'form_class': fields.IntegerField},
    db_models.SlugField: {'form_class': fields.SlugField},
    db_models.SmallIntegerField: {'form_class': fields.IntegerField},
    db_models.TextField: {'form_class': fields.CharField, 'widget': Textarea},
    db_models.TimeField: {'form_class': fields.TimeField},
    db_models.URLField: {'form_class': fields.URLField},
    # Binary field is never editable, so we don't need to convert it.

    db_models.FileField: {'form_class': fields.FileField},
    db_models.ImageField: {'form_class': fields.ImageField},

    db_models.ForeignKey: {'form_class': ModelChoiceField},
    db_models.ManyToManyField: {'form_class': ModelMultipleChoiceField},
    db_models.OneToOneField: {'form_class': ModelChoiceField},
}
if django.VERSION < (1, 9):
    FORMFIELD_OVERRIDES[db_models.IPAddressField] = {'form_class': fields.IPAddressField}

for value in FORMFIELD_OVERRIDES.values():
    value['choices_form_class'] = fields.TypedChoiceField


def formfield_callback(db_field, **kwargs):
    defaults = FORMFIELD_OVERRIDES.get(db_field.__class__, {}).copy()
    defaults.update(kwargs)
    return db_field.formfield(**defaults)


class ModelFormMetaclass(_ModelFormMetaclass):
    def __new__(mcs, name, bases, attrs):
        if not attrs.get('formfield_callback'):
            attrs['formfield_callback'] = formfield_callback
        return super(ModelFormMetaclass, mcs).__new__(mcs, name, bases, attrs)


class ModelForm(six.with_metaclass(ModelFormMetaclass, LayoutRenderer, _ModelForm)):
    pass


def modelform_factory(model, form=ModelForm, fields=None, exclude=None,
                      formfield_callback=formfield_callback, *args, **kwargs):
    return _modelform_factory(model, form, fields, exclude, formfield_callback,
                              *args, **kwargs)


def modelformset_factory(model, form=ModelForm,
                         formfield_callback=formfield_callback,
                         *args, **kwargs):
    return _modelformset_factory(model, form, formfield_callback,
                                 *args, **kwargs)


def inlineformset_factory(parent_model, model, form=ModelForm,
                          formset=BaseInlineFormSet, fk_name=None,
                          fields=None, exclude=None, extra=3, can_order=False,
                          can_delete=True, max_num=None,
                          formfield_callback=formfield_callback,
                          *args, **kwargs):
    return _inlineformset_factory(parent_model, model, form, formset, fk_name,
                                  fields, exclude, extra, can_order,
                                  can_delete, max_num, formfield_callback,
                                  *args, **kwargs)

```


