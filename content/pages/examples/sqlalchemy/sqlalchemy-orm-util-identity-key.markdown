title: sqlalchemy.orm.util identity_key Example Code
category: page
slug: sqlalchemy-orm-util-identity-key-examples
sortorder: 500031095
toc: False
sidebartitle: sqlalchemy.orm.util identity_key
meta: Python example code that shows how to use the identity_key callable from the sqlalchemy.orm.util module of the SQLAlchemy project.


`identity_key` is a callable within the `sqlalchemy.orm.util` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-util-aliasedclass-examples.html">AliasedClass</a>
and
<a href="/sqlalchemy-orm-util-aliasedinsp-examples.html">AliasedInsp</a>
are a couple of other callables within the `sqlalchemy.orm.util` package that also have code examples.

## Example 1 from WTForms-Alchemy
[wtforms-alchemy](git@github.com:kvesteri/wtforms-alchemy.git)
([documentation](https://wtforms-alchemy.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/WTForms-Alchemy/))
is a [WTForms](https://wtforms.readthedocs.io/en/2.2.1/) extension toolkit
for easier creation of [SQLAlchemy](/sqlalchemy.html) model based forms.
While this project primarily focuses on proper form handling, it also
has many good examples of how to use various parts of SQLAlchemy in
its code base. The project is provided as open source under the
[MIT license](https://github.com/kvesteri/wtforms-alchemy/blob/master/LICENSE).

[**WTForms-Alchemy / wtforms_alchemy / fields.py**](https://github.com/kvesteri/wtforms-alchemy/blob/master/wtforms_alchemy/./fields.py)

```python
# fields.py
from __future__ import unicode_literals

import operator
from itertools import groupby

import six
~~from sqlalchemy.orm.util import identity_key
from sqlalchemy_utils import Country, i18n, PhoneNumber
from sqlalchemy_utils.primitives import WeekDay, WeekDays
from wtforms import widgets
from wtforms.compat import string_types, text_type
from wtforms.fields import FieldList, FormField, SelectFieldBase
from wtforms.validators import ValidationError
from wtforms.widgets import CheckboxInput, ListWidget
from wtforms_components import SelectField, SelectMultipleField
from wtforms_components.fields.html5 import StringField
from wtforms_components.widgets import SelectWidget, TelInput

from .utils import find_entity

try:
    from wtforms.utils import unset_value as _unset_value
except ImportError:
    from wtforms.fields import _unset_value


class SkipOperation(Exception):
    pass


class ModelFormField(FormField):


## ... source file abbreviated to get to identity_key examples ...



    def _set_data(self, data):
        self._data = data
        self._formdata = None

    data = property(_get_data, _set_data)

    def iter_choices(self):
        for pk, obj in self._get_object_list():
            yield (pk, self.get_label(obj), obj in self.data)

    def process_formdata(self, valuelist):
        self._formdata = set(valuelist)

    def pre_validate(self, form):
        if self._invalid_formdata:
            raise ValidationError(self.gettext('Not a valid choice'))
        elif self.data:
            obj_list = list(x[1] for x in self._get_object_list())
            for v in self.data:
                if v not in obj_list:
                    raise ValidationError(self.gettext('Not a valid choice'))


def get_pk_from_identity(obj):
~~    cls, key = identity_key(instance=obj)[0:2]
    return ':'.join(text_type(x) for x in key)


class GroupedQuerySelectField(SelectField):
    widget = SelectWidget()

    def __init__(
        self,
        label=None,
        validators=None,
        query_factory=None,
        get_pk=None,
        get_label=None,
        get_group=None,
        allow_blank=False,
        blank_text='',
        blank_value='__None',
        **kwargs
    ):
        super(GroupedQuerySelectField, self).__init__(
            label,
            validators,
            coerce=lambda x: x,
            **kwargs


## ... source file continues with no further identity_key examples...

```

