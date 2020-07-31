title: sqlalchemy.ext.associationproxy AssociationProxy Example Code
category: page
slug: sqlalchemy-ext-associationproxy-associationproxy-examples
sortorder: 500031045
toc: False
sidebartitle: sqlalchemy.ext.associationproxy AssociationProxy
meta: Example code for understanding how to use the AssociationProxy class from the sqlalchemy.ext.associationproxy module of the SQLAlchemy project.


`AssociationProxy` is a class within the `sqlalchemy.ext.associationproxy` module of the SQLAlchemy project.



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

[**SQLAthanor / sqlathanor / declarative / _base_configuration_mixin.py**](https://github.com/insightindustry/sqlathanor/blob/master/sqlathanor/declarative/_base_configuration_mixin.py)

```python
# _base_configuration_mixin.py


import inspect as inspect_
from collections import OrderedDict

from sqlalchemy.inspection import inspect
from sqlalchemy.exc import InvalidRequestError
~~from sqlalchemy.ext.associationproxy import AssociationProxy
from validator_collection import checkers

from sqlathanor._compat import dict as dict_
from sqlathanor.attributes import AttributeConfiguration, validate_serialization_config, \
    BLANK_ON_SERIALIZE
from sqlathanor.errors import ConfigurationError, UnsupportedSerializationError


class ConfigurationMixin(object):

    @classmethod
    def _get_instance_attributes(cls,
                                 include_private = False,
                                 exclude_methods = True):
        base_attributes = dir(cls)
        instance_attributes = []
        for key in base_attributes:
            if key.startswith('__'):
                continue

            if key.startswith('_') and not key.startswith('__') and not include_private:
                continue

            try:


## ... source file continues with no further AssociationProxy examples...

```

