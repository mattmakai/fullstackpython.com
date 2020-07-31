title: sqlalchemy.orm.relationships RelationshipProperty Example Code
category: page
slug: sqlalchemy-orm-relationships-relationshipproperty-examples
sortorder: 500031090
toc: False
sidebartitle: sqlalchemy.orm.relationships RelationshipProperty
meta: Example code for understanding how to use the RelationshipProperty class from the sqlalchemy.orm.relationships module of the SQLAlchemy project.


`RelationshipProperty` is a class within the `sqlalchemy.orm.relationships` module of the SQLAlchemy project.



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
~~from sqlalchemy.orm.relationships import RelationshipProperty as SA_RelationshipProperty
from sqlalchemy.util.langhelpers import public_factory
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


~~class RelationshipProperty(SA_RelationshipProperty):

    def __init__(self,
                 argument,
                 supports_json = False,
                 supports_yaml = False,
                 supports_dict = False,
                 on_serialize = None,
                 on_deserialize = None,
                 **kwargs):
        if on_serialize is not None and not isinstance(on_serialize, dict):
            on_serialize = {
                'csv': on_serialize,
                'json': on_serialize,
                'yaml': on_serialize,
                'dict': on_serialize
            }
        elif on_serialize is not None:
            if 'csv' not in on_serialize:
                on_serialize['csv'] = None
            if 'json' not in on_serialize:
                on_serialize['json'] = None
            if 'yaml' not in on_serialize:
                on_serialize['yaml'] = None
            if 'dict' not in on_serialize:


## ... source file abbreviated to get to RelationshipProperty examples ...


                raise SQLAthanorError('on_deserialize for %s must be callable' % key)

        if supports_json is True:
            supports_json = (True, True)
        elif not supports_json:
            supports_json = (False, False)

        if supports_yaml is True:
            supports_yaml = (True, True)
        elif not supports_yaml:
            supports_yaml = (False, False)

        if supports_dict is True:
            supports_dict = (True, True)
        elif not supports_dict:
            supports_dict = (False, False)

        self.supports_csv = (False, False)
        self.csv_sequence = None
        self.supports_json = supports_json
        self.supports_yaml = supports_yaml
        self.supports_dict = supports_dict
        self.on_serialize = on_serialize
        self.on_deserialize = on_deserialize

~~        comparator_factory = kwargs.pop('comparator_factory', RelationshipProperty.Comparator)

~~        super(RelationshipProperty, self).__init__(argument,
                                                   comparator_factory = comparator_factory,
                                                   **kwargs)

    class Comparator(SA_RelationshipProperty.Comparator):
        @property
        def supports_csv(self):
            return self.prop.supports_csv

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


## ... source file continues with no further RelationshipProperty examples...

```

