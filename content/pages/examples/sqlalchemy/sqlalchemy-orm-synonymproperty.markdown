title: sqlalchemy.orm SynonymProperty code examples
category: page
slug: sqlalchemy-orm-synonymproperty-examples
sortorder: 500031038
toc: False
sidebartitle: sqlalchemy.orm SynonymProperty
meta: Python example code for the SynonymProperty class from the sqlalchemy.orm module of the SQLAlchemy project.


SynonymProperty is a class within the sqlalchemy.orm module of the SQLAlchemy project.


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
from sqlalchemy.dialects import postgresql, mysql, mssql
~~from sqlalchemy.orm import SynonymProperty
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


## ... source file abbreviated to get to SynonymProperty examples ...


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
        result = dict_cls()
        base_fields = base_fields or {}
        for prop in model.__mapper__.iterate_properties:
            key = self._get_field_name(prop)
            if self._should_exclude_field(prop, fields=fields, exclude=exclude):
                result[key] = None
                continue
~~            if isinstance(prop, SynonymProperty):
                continue
            if hasattr(prop, "columns"):
                if not include_fk:
                    for column in prop.columns:
                        if not column.foreign_keys:
                            break
                    else:
                        continue
            if not include_relationships and hasattr(prop, "direction"):
                continue
            field = base_fields.get(key) or self.property2field(prop)
            if field:
                result[key] = field
        return result

    def fields_for_table(
        self,
        table,
        *,
        include_fk=False,
        fields=None,
        exclude=None,
        base_fields=None,
        dict_cls=dict,


## ... source file continues with no further SynonymProperty examples...

```

