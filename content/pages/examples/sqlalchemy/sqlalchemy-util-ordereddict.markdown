title: sqlalchemy.util OrderedDict Example Code
category: page
slug: sqlalchemy-util-ordereddict-examples
sortorder: 500031149
toc: False
sidebartitle: sqlalchemy.util OrderedDict
meta: Example code for understanding how to use the OrderedDict class from the sqlalchemy.util module of the SQLAlchemy project.


`OrderedDict` is a class within the `sqlalchemy.util` module of the SQLAlchemy project.

<a href="/sqlalchemy-util-orderedset-examples.html">OrderedSet</a>,
<a href="/sqlalchemy-util-set-creation-order-examples.html">set_creation_order</a>,
<a href="/sqlalchemy-util-symbol-examples.html">symbol</a>,
and <a href="/sqlalchemy-util-topological-examples.html">topological</a>
are several other callables with code examples from the same `sqlalchemy.util` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / operations / batch.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/operations/batch.py)

```python
# batch.py
from sqlalchemy import CheckConstraint
from sqlalchemy import Column
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy import Index
from sqlalchemy import MetaData
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import schema as sql_schema
from sqlalchemy import select
from sqlalchemy import Table
from sqlalchemy import types as sqltypes
from sqlalchemy.events import SchemaEventTarget
~~from sqlalchemy.util import OrderedDict
from sqlalchemy.util import topological

from ..util import exc
from ..util.sqla_compat import _columns_for_constraint
from ..util.sqla_compat import _fk_is_self_referential
from ..util.sqla_compat import _is_type_bound
from ..util.sqla_compat import _remove_column_from_collection


class BatchOperationsImpl(object):
    def __init__(
        self,
        operations,
        table_name,
        schema,
        recreate,
        copy_from,
        table_args,
        table_kwargs,
        reflect_args,
        reflect_kwargs,
        naming_convention,
        partial_reordering,
    ):


## ... source file abbreviated to get to OrderedDict examples ...



    def drop_table(self, table):
        raise NotImplementedError("Can't drop table in batch mode")


class ApplyBatchImpl(object):
    def __init__(
        self,
        impl,
        table,
        table_args,
        table_kwargs,
        reflected,
        partial_reordering=(),
    ):
        self.impl = impl
        self.table = table  # this is a Table object
        self.table_args = table_args
        self.table_kwargs = table_kwargs
        self.temp_table_name = self._calc_temp_name(table.name)
        self.new_table = None

        self.partial_reordering = partial_reordering  # tuple of tuples
        self.add_col_ordering = ()  # tuple of tuples

~~        self.column_transfers = OrderedDict(
            (c.name, {"expr": c}) for c in self.table.c
        )
        self.existing_ordering = list(self.column_transfers)

        self.reflected = reflected
        self._grab_table_elements()

    @classmethod
    def _calc_temp_name(cls, tablename):
        return ("_alembic_tmp_%s" % tablename)[0:50]

    def _grab_table_elements(self):
        schema = self.table.schema
~~        self.columns = OrderedDict()
        for c in self.table.c:
            c_copy = c.copy(schema=schema)
            c_copy.unique = c_copy.index = False
            if isinstance(c.type, SchemaEventTarget):
                assert c_copy.type is not c.type
            self.columns[c.name] = c_copy
        self.named_constraints = {}
        self.unnamed_constraints = []
        self.indexes = {}
        self.new_indexes = {}
        for const in self.table.constraints:
            if _is_type_bound(const):
                continue
            elif self.reflected and isinstance(const, CheckConstraint):
                pass
            elif const.name:
                self.named_constraints[const.name] = const
            else:
                self.unnamed_constraints.append(const)

        for idx in self.table.indexes:
            self.indexes[idx.name] = idx

        for k in self.table.kwargs:
            self.table_kwargs.setdefault(k, self.table.kwargs[k])

    def _adjust_self_columns_for_partial_reordering(self):
        pairs = set()

        col_by_idx = list(self.columns)

        if self.partial_reordering:
            for tuple_ in self.partial_reordering:
                for index, elem in enumerate(tuple_):
                    if index > 0:
                        pairs.add((tuple_[index - 1], elem))
        else:
            for index, elem in enumerate(self.existing_ordering):
                if index > 0:
                    pairs.add((col_by_idx[index - 1], elem))

        pairs.update(self.add_col_ordering)

        pairs = [p for p in pairs if p[0] != p[1]]

        sorted_ = list(
            topological.sort(pairs, col_by_idx, deterministic_order=True)
        )
~~        self.columns = OrderedDict((k, self.columns[k]) for k in sorted_)
~~        self.column_transfers = OrderedDict(
            (k, self.column_transfers[k]) for k in sorted_
        )

    def _transfer_elements_to_new_table(self):
        assert self.new_table is None, "Can only create new table once"

        m = MetaData()
        schema = self.table.schema

        if self.partial_reordering or self.add_col_ordering:
            self._adjust_self_columns_for_partial_reordering()

        self.new_table = new_table = Table(
            self.temp_table_name,
            m,
            *(list(self.columns.values()) + list(self.table_args)),
            schema=schema,
            **self.table_kwargs
        )

        for const in (
            list(self.named_constraints.values()) + self.unnamed_constraints
        ):



## ... source file continues with no further OrderedDict examples...

```


## Example 2 from sqlacodegen
[sqlacodegen](https://github.com/agronholm/sqlacodegen)
([PyPI package information](https://pypi.org/project/sqlacodegen/))
is a tool for
reading from an existing [relational database](/databases.html) to
generate code to create [SQLAlchemy](/sqlalchemy.html) models based
on that database. The project is primarily written and maintained
by [Alex Grönholm (agronholm)](https://github.com/agronholm) and it
is open sourced under the
[MIT license](https://github.com/agronholm/sqlacodegen/blob/master/LICENSE).

[**sqlacodegen / sqlacodegen / codegen.py**](https://github.com/agronholm/sqlacodegen/blob/master/sqlacodegen/./codegen.py)

```python
# codegen.py
from __future__ import unicode_literals, division, print_function, absolute_import

import inspect
import re
import sys
from collections import defaultdict
from importlib import import_module
from inspect import ArgSpec
from keyword import iskeyword

import sqlalchemy
import sqlalchemy.exc
from sqlalchemy import (
    Enum, ForeignKeyConstraint, PrimaryKeyConstraint, CheckConstraint, UniqueConstraint, Table,
    Column, Float)
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.types import Boolean, String
~~from sqlalchemy.util import OrderedDict

try:
    from sqlalchemy import ARRAY
except ImportError:
    from sqlalchemy.dialects.postgresql import ARRAY

try:
    from sqlalchemy import Computed
except ImportError:
    Computed = None

try:
    import geoalchemy2  # noqa: F401
except ImportError:
    pass

_re_boolean_check_constraint = re.compile(r"(?:(?:.*?)\.)?(.*?) IN \(0, 1\)")
_re_column_name = re.compile(r'(?:(["`]?)(?:.*)\1\.)?(["`]?)(.*)\2')
_re_enum_check_constraint = re.compile(r"(?:(?:.*?)\.)?(.*?) IN \((.+)\)")
_re_enum_item = re.compile(r"'(.*?)(?<!\\)'")
_re_invalid_identifier = re.compile(r'[^a-zA-Z0-9_]' if sys.version_info[0] < 3 else r'(?u)\W')


class _DummyInflectEngine(object):


## ... source file abbreviated to get to OrderedDict examples ...


        if name[0].isdigit() or iskeyword(name):
            name = '_' + name
        elif name == 'metadata':
            name = 'metadata_'

        return _re_invalid_identifier.sub('_', name)


class ModelTable(Model):
    def __init__(self, table):
        super(ModelTable, self).__init__(table)
        self.name = self._convert_to_valid_identifier(table.name)

    def add_imports(self, collector):
        super(ModelTable, self).add_imports(collector)
        collector.add_import(Table)


class ModelClass(Model):
    parent_name = 'Base'

    def __init__(self, table, association_tables, inflect_engine, detect_joined):
        super(ModelClass, self).__init__(table)
        self.name = self._tablename_to_classname(table.name, inflect_engine)
        self.children = []
~~        self.attributes = OrderedDict()

        for column in table.columns:
            self._add_attribute(column.name, column)

        pk_column_names = set(col.name for col in table.primary_key.columns)
        for constraint in sorted(table.constraints, key=_get_constraint_sort_key):
            if isinstance(constraint, ForeignKeyConstraint):
                target_cls = self._tablename_to_classname(constraint.elements[0].column.table.name,
                                                          inflect_engine)
                if (detect_joined and self.parent_name == 'Base' and
                        set(_get_column_names(constraint)) == pk_column_names):
                    self.parent_name = target_cls
                else:
                    relationship_ = ManyToOneRelationship(self.name, target_cls, constraint,
                                                          inflect_engine)
                    self._add_attribute(relationship_.preferred_name, relationship_)

        for association_table in association_tables:
            fk_constraints = [c for c in association_table.constraints
                              if isinstance(c, ForeignKeyConstraint)]
            fk_constraints.sort(key=_get_constraint_sort_key)
            target_cls = self._tablename_to_classname(
                fk_constraints[1].elements[0].column.table.name, inflect_engine)
            relationship_ = ManyToManyRelationship(self.name, target_cls, association_table)


## ... source file abbreviated to get to OrderedDict examples ...


    def _add_attribute(self, attrname, value):
        attrname = tempname = self._convert_to_valid_identifier(attrname)
        counter = 1
        while tempname in self.attributes:
            tempname = attrname + str(counter)
            counter += 1

        self.attributes[tempname] = value
        return tempname

    def add_imports(self, collector):
        super(ModelClass, self).add_imports(collector)

        if any(isinstance(value, Relationship) for value in self.attributes.values()):
            collector.add_literal_import('sqlalchemy.orm', 'relationship')

        for child in self.children:
            child.add_imports(collector)


class Relationship(object):
    def __init__(self, source_cls, target_cls):
        super(Relationship, self).__init__()
        self.source_cls = source_cls
        self.target_cls = target_cls
~~        self.kwargs = OrderedDict()


class ManyToOneRelationship(Relationship):
    def __init__(self, source_cls, target_cls, constraint, inflect_engine):
        super(ManyToOneRelationship, self).__init__(source_cls, target_cls)

        column_names = _get_column_names(constraint)
        colname = column_names[0]
        tablename = constraint.elements[0].column.table.name
        if not colname.endswith('_id'):
            self.preferred_name = inflect_engine.singular_noun(tablename) or tablename
        else:
            self.preferred_name = colname[:-3]

        if any(isinstance(c, (PrimaryKeyConstraint, UniqueConstraint)) and
               set(col.name for col in c.columns) == set(column_names)
               for c in constraint.table.constraints):
            self.kwargs['uselist'] = 'False'

        if source_cls == target_cls:
            self.preferred_name = 'parent' if not colname.endswith('_id') else colname[:-3]
            pk_col_names = [col.name for col in constraint.table.primary_key]
            self.kwargs['remote_side'] = '[{0}]'.format(', '.join(pk_col_names))

    @staticmethod
    def singular_noun(noun):
        return noun


def _get_column_names(constraint):
    if isinstance(constraint.columns, list):
        return constraint.columns
    return list(constraint.columns.keys())


def _get_constraint_sort_key(constraint):
    if isinstance(constraint, CheckConstraint):
        return 'C{0}'.format(constraint.sqltext)
    return constraint.__class__.__name__[0] + repr(_get_column_names(constraint))


~~class ImportCollector(OrderedDict):
    def add_import(self, obj):
        type_ = type(obj) if not isinstance(obj, type) else obj
        pkgname = type_.__module__

        if pkgname.startswith('sqlalchemy.dialects.'):
            dialect_pkgname = '.'.join(pkgname.split('.')[0:3])
            dialect_pkg = import_module(dialect_pkgname)

            if type_.__name__ in dialect_pkg.__all__:
                pkgname = dialect_pkgname
        else:
            pkgname = 'sqlalchemy' if type_.__name__ in sqlalchemy.__all__ else type_.__module__
        self.add_literal_import(pkgname, type_.__name__)

    def add_literal_import(self, pkgname, name):
        names = self.setdefault(pkgname, set())
        names.add(name)


class Model(object):
    def __init__(self, table):
        super(Model, self).__init__()
        self.table = table
        self.schema = table.schema


## ... source file continues with no further OrderedDict examples...

```

