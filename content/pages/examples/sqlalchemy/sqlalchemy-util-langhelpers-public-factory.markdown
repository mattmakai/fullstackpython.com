title: sqlalchemy.util.langhelpers public_factory Example Code
category: page
slug: sqlalchemy-util-langhelpers-public-factory-examples
sortorder: 500031154
toc: False
sidebartitle: sqlalchemy.util.langhelpers public_factory
meta: Python example code that shows how to use the public_factory callable from the sqlalchemy.util.langhelpers module of the SQLAlchemy project.


`public_factory` is a callable within the `sqlalchemy.util.langhelpers` module of the SQLAlchemy project.

<a href="/sqlalchemy-util-langhelpers-symbol-examples.html">symbol</a>
is another callable from the `sqlalchemy.util.langhelpers` package with code examples.

## Example 1 from SQLAthanor
[SQLAthanor](https://github.com/insightindustry/sqlathanor)
([PyPI package information](https://pypi.org/project/sqlathanor/)
and
[project documentation](https://sqlathanor.readthedocs.io/en/latest/index.html))
is a [SQLAlchemy](/sqlalchemy.html) extension that provides serialization and
deserialization support for JSON, CSV, YAML and Python dictionaries.
This project is similar to [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
with one major difference: SQLAthanor works through SQLAlchemy models
while Marshmallow is less coupled to SQLAlchemy because it requires
separate representations of the serialization objects. Both libraries
have their uses depending on whether the project plans to use SQLAlchemy
for object representations or would prefer to avoid that couping.
SQLAthanor is open sourced under the
[MIT license](https://github.com/insightindustry/sqlathanor/blob/master/LICENSE).

[**SQLAthanor / sqlathanor / schema.py**](https://github.com/insightindustry/sqlathanor/blob/master/sqlathanor/./schema.py)

```python
# schema.py


import functools
import operator

from sqlalchemy import Column as SA_Column
from sqlalchemy import Table as SA_Table
from sqlalchemy.orm import class_mapper
from sqlalchemy.orm.relationships import RelationshipProperty as SA_RelationshipProperty
~~from sqlalchemy.util.langhelpers import public_factory
from sqlalchemy.ext.hybrid import hybrid_property as SA_hybrid_property

from sqlalchemy import exc, orm, util, inspect


from validator_collection import checkers, validators

from sqlathanor import attributes
from sqlathanor._serialization_support import SerializationMixin
from sqlathanor.default_deserializers import get_type_mapping
from sqlathanor.utilities import parse_json, parse_yaml, parse_csv, read_csv_data
from sqlathanor.errors import SQLAthanorError


class Column(SerializationMixin, SA_Column):


    def __init__(self, *args, **kwargs):
        super(Column, self).__init__(*args, **kwargs)


class RelationshipProperty(SA_RelationshipProperty):

    def __init__(self,


## ... source file abbreviated to get to public_factory examples ...


        @property
        def csv_sequence(self):
            return self.prop.csv_sequence

        @property
        def supports_json(self):
            return self.prop.supports_json

        @property
        def supports_yaml(self):
            return self.prop.supports_yaml

        @property
        def supports_dict(self):
            return self.prop.supports_dict

        @property
        def on_serialize(self):
            return self.prop.on_serialize

        @property
        def on_deserialize(self):
            return self.prop.on_deserialize


~~relationship = public_factory(RelationshipProperty, ".orm.relationship")


class Table(SA_Table):


    def __init__(self, *args, **kwargs):
        super(Table, self).__init__(*args, **kwargs)

    @classmethod
    def from_dict(cls,
                  serialized,
                  tablename,
                  metadata,
                  primary_key,
                  column_kwargs = None,
                  skip_nested = True,
                  default_to_str = False,
                  type_mapping = None,
                  **kwargs):
        if not isinstance(serialized, dict):
            raise ValueError('serialized must be a dict')

        if not serialized:
            raise ValueError('serialized cannot be empty')


## ... source file continues with no further public_factory examples...

```

