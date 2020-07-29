title: sqlalchemy.dialects mssql Example Code
category: page
slug: sqlalchemy-dialects-mssql-examples
sortorder: 500031001
toc: False
sidebartitle: sqlalchemy.dialects mssql
meta: Python example code that shows how to use the mssql callable from the sqlalchemy.dialects module of the SQLAlchemy project.


`mssql` is a callable within the `sqlalchemy.dialects` module of the SQLAlchemy project.

<a href="/sqlalchemy-dialects-mysql-examples.html">mysql</a>,
<a href="/sqlalchemy-dialects-oracle-examples.html">oracle</a>,
<a href="/sqlalchemy-dialects-postgresql-examples.html">postgresql</a>,
and <a href="/sqlalchemy-dialects-sqlite-examples.html">sqlite</a>
are several other callables with code examples from the same `sqlalchemy.dialects` package.

## Example 1 from marshmallow-sqlalchemy
[marshmallow-sqlalchemy](https://github.com/marshmallow-code/marshmallow-sqlalchemy)
([project documentation](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/))
is a code library that makes it easier to use
[SQLAlchemy](/sqlalchemy.html) with the
[Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
data serialization tool.

The marshmallow-sqlalchemy project is provided as open source under the
[MIT license](https://github.com/marshmallow-code/marshmallow-sqlalchemy/blob/dev/LICENSE).

[**marshmallow-sqlalchemy / src/marshmallow_sqlalchemy / convert.py**](https://github.com/marshmallow-code/marshmallow-sqlalchemy/blob/dev/src/marshmallow_sqlalchemy/./convert.py)

```python
# convert.py
import inspect
import functools
import warnings

import uuid
import marshmallow as ma
from marshmallow import validate, fields
~~from sqlalchemy.dialects import postgresql, mysql, mssql
from sqlalchemy.orm import SynonymProperty
import sqlalchemy as sa

from .exceptions import ModelConversionError
from .fields import Related, RelatedList


def _is_field(value):
    return isinstance(value, type) and issubclass(value, fields.Field)


def _has_default(column):
    return (
        column.default is not None
        or column.server_default is not None
        or _is_auto_increment(column)
    )


def _is_auto_increment(column):
    return column.table is not None and column is column.table._autoincrement_column


def _postgres_array_factory(converter, data_type):


## ... source file abbreviated to get to mssql examples ...



class ModelConverter:

    SQLA_TYPE_MAPPING = {
        sa.Enum: fields.Field,
        sa.JSON: fields.Raw,
        postgresql.BIT: fields.Integer,
        postgresql.OID: fields.Integer,
        postgresql.UUID: fields.UUID,
        postgresql.MACADDR: fields.String,
        postgresql.INET: fields.String,
        postgresql.CIDR: fields.String,
        postgresql.JSON: fields.Raw,
        postgresql.JSONB: fields.Raw,
        postgresql.HSTORE: fields.Raw,
        postgresql.ARRAY: _postgres_array_factory,
        postgresql.MONEY: fields.Decimal,
        postgresql.DATE: fields.Date,
        postgresql.TIME: fields.Time,
        mysql.BIT: fields.Integer,
        mysql.YEAR: fields.Integer,
        mysql.SET: fields.List,
        mysql.ENUM: fields.Field,
        mysql.INTEGER: fields.Integer,
        mysql.DATETIME: fields.DateTime,
~~        mssql.BIT: fields.Integer,
    }
    DIRECTION_MAPPING = {"MANYTOONE": False, "MANYTOMANY": True, "ONETOMANY": True}

    def __init__(self, schema_cls=None):
        self.schema_cls = schema_cls

    @property
    def type_mapping(self):
        if self.schema_cls:
            return self.schema_cls.TYPE_MAPPING
        else:
            return ma.Schema.TYPE_MAPPING

    def fields_for_model(
        self,
        model,
        *,
        include_fk=False,
        include_relationships=False,
        fields=None,
        exclude=None,
        base_fields=None,
        dict_cls=dict,
    ):


## ... source file continues with no further mssql examples...

```

