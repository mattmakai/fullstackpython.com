title: sqlalchemy.sql.elements Label Example Code
category: page
slug: sqlalchemy-sql-elements-label-examples
sortorder: 500031120
toc: False
sidebartitle: sqlalchemy.sql.elements Label
meta: Example code for understanding how to use the Label class from the sqlalchemy.sql.elements module of the SQLAlchemy project.


`Label` is a class within the `sqlalchemy.sql.elements` module of the SQLAlchemy project.

<a href="/sqlalchemy-sql-elements-columnelement-examples.html">ColumnElement</a>
is another callable from the `sqlalchemy.sql.elements` package with code examples.

## Example 1 from GINO
[GINO](https://github.com/fantix/gino)
([project documentation](https://python-gino.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/gino/))
is an [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
built on SQLAlchemy that is non-blocking and therefore designed to work properly
with asynchronously-run code, for example, an application written with
[asyncio](https://docs.python.org/3/library/asyncio.html).

GINO is open sourced under the [BSD License](https://github.com/python-gino/gino/blob/master/LICENSE).

[**GINO / src/gino / loader.py**](https://github.com/python-gino/gino/blob/master/src/gino/./loader.py)

```python
# loader.py
import types
import warnings

from sqlalchemy import select
from sqlalchemy.schema import Column
~~from sqlalchemy.sql.elements import Label

from .declarative import Model


class Loader:

    @classmethod
    def get(cls, value):
        from .crud import Alias

        if isinstance(value, Loader):
            rv = value
        elif isinstance(value, type) and issubclass(value, Model):
            rv = ModelLoader(value)
        elif isinstance(value, Alias):
            rv = AliasLoader(value)
        elif isinstance(value, Column):
            rv = ColumnLoader(value)
~~        elif isinstance(value, Label):
            rv = ColumnLoader(value.name)
        elif isinstance(value, tuple):
            rv = TupleLoader(value)
        elif callable(value):
            rv = CallableLoader(value)
        else:
            rv = ValueLoader(value)
        return rv

    @property
    def query(self):
        rv = select(self.get_columns())
        from_clause = self.get_from()
        if from_clause is not None:
            rv = rv.select_from(from_clause)
        return rv.execution_options(loader=self)

    def do_load(self, row, context):
        raise NotImplementedError

    def get_columns(self):
        return []

    def get_from(self):


## ... source file continues with no further Label examples...

```


## Example 2 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management that is
powered by [SQLAlchemy](/sqlalchemy.html) on the backend. The code
for this project is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / core / marshmallow.py**](https://github.com/indico/indico/blob/master/indico/core/marshmallow.py)

```python
# marshmallow.py

from __future__ import absolute_import, unicode_literals

from inspect import getmro

from flask_marshmallow import Marshmallow
from flask_marshmallow.sqla import SchemaOpts
from marshmallow import fields, post_dump, post_load, pre_load
from marshmallow_enum import EnumField
from marshmallow_sqlalchemy import ModelConverter
from marshmallow_sqlalchemy import ModelSchema as MSQLAModelSchema
from sqlalchemy.orm import ColumnProperty
~~from sqlalchemy.sql.elements import Label
from webargs.flaskparser import parser as webargs_flask_parser

from indico.core import signals
from indico.core.db.sqlalchemy import PyIntEnum, UTCDateTime
from indico.web.args import parser as indico_webargs_flask_parser


mm = Marshmallow()


def _is_column_property(prop):
    return hasattr(prop, 'columns') and isinstance(prop.columns[0], Label)


class IndicoModelConverter(ModelConverter):
    SQLA_TYPE_MAPPING = ModelConverter.SQLA_TYPE_MAPPING.copy()
    SQLA_TYPE_MAPPING.update({
        UTCDateTime: fields.DateTime,
        PyIntEnum: EnumField
    })

    def _get_field_kwargs_for_property(self, prop):
        kwargs = super(IndicoModelConverter, self)._get_field_kwargs_for_property(prop)
        if isinstance(prop, ColumnProperty) and hasattr(prop.columns[0].type, 'marshmallow_get_field_kwargs'):


## ... source file continues with no further Label examples...

```

