title: sqlalchemy.dialects mysql Example Code
category: page
slug: sqlalchemy-dialects-mysql-examples
sortorder: 500031002
toc: False
sidebartitle: sqlalchemy.dialects mysql
meta: Python example code that shows how to use the mysql callable from the sqlalchemy.dialects module of the SQLAlchemy project.


`mysql` is a callable within the `sqlalchemy.dialects` module of the SQLAlchemy project.

<a href="/sqlalchemy-dialects-mssql-examples.html">mssql</a>,
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
    return functools.partial(
        fields.List, converter._get_field_class_for_data_type(data_type.item_type)
    )


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
~~        mysql.BIT: fields.Integer,
~~        mysql.YEAR: fields.Integer,
~~        mysql.SET: fields.List,
~~        mysql.ENUM: fields.Field,
~~        mysql.INTEGER: fields.Integer,
~~        mysql.DATETIME: fields.DateTime,
        mssql.BIT: fields.Integer,
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


## ... source file continues with no further mysql examples...

```


## Example 2 from sqlalchemy-datatables
[sqlalchemy-datatables](https://github.com/Pegase745/sqlalchemy-datatables)
([PyPI package information](https://pypi.org/project/sqlalchemy-datatables/))
is a helper library that makes it easier to use [SQLAlchemy](/sqlalchemy.html)
with the jQuery [JavaScript](/javascript.html)
[DataTables](https://datatables.net/) plugin. This library is designed to
be [web framework](/web-frameworks.html) agnostic and provides code examples
for both [Flask](/flask.html) and [Pyramid](/pyramid.html).

The project is built and maintained by
[Michel Nemnom (Pegase745)](https://github.com/Pegase745) and is open
sourced under the
[MIT license](https://github.com/Pegase745/sqlalchemy-datatables/blob/master/LICENSE).

[**sqlalchemy-datatables / datatables / datatables.py**](https://github.com/Pegase745/sqlalchemy-datatables/blob/master/./datatables/datatables.py)

```python
# datatables.py
from __future__ import absolute_import

import math

from sqlalchemy import Text, func, or_
~~from sqlalchemy.dialects import mysql, postgresql, sqlite

from datatables.clean_regex import clean_regex
from datatables.search_methods import SEARCH_METHODS


class DataTables:

    def __init__(self, request, query, columns, allow_regex_searches=False):
        self.params = dict(request)
        if 'sEcho' in self.params:
            raise ValueError(
                'Legacy datatables not supported, upgrade to >=1.10')
        self.query = query
        self.columns = columns
        self.results = None
        self.allow_regex_searches = allow_regex_searches

        self.cardinality_filtered = 0

        self.cardinality = 0

        self.yadcf_params = []
        self.filter_expressions = []
        self.error = None


## ... source file abbreviated to get to mysql examples ...


            direction = self.params.get('order[{:d}][dir]'.format(i))
            sort_expr = column.sqla_expr
            if direction == 'asc':
                sort_expr = sort_expr.asc()
            elif direction == 'desc':
                sort_expr = sort_expr.desc()
            else:
                raise ValueError(
                    'Invalid order direction: {}'.format(direction))
            if column.nulls_order:
                if column.nulls_order == 'nullsfirst':
                    sort_expr = sort_expr.nullsfirst()
                elif column.nulls_order == 'nullslast':
                    sort_expr = sort_expr.nullslast()
                else:
                    raise ValueError(
                        'Invalid order direction: {}'.format(direction))

            sort_expressions.append(sort_expr)
            i += 1
        self.sort_expressions = sort_expressions

    def _get_regex_operator(self):
        if isinstance(self.query.session.bind.dialect, postgresql.dialect):
            return '-'
~~        elif isinstance(self.query.session.bind.dialect, mysql.dialect):
            return 'REGEXP'
        elif isinstance(self.query.session.bind.dialect, sqlite.dialect):
            return 'REGEXP'
        else:
            raise NotImplementedError(
                'Regex searches are not implemented for this dialect')



## ... source file continues with no further mysql examples...

```

