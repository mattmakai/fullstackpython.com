title: sqlalchemy.dialects.postgresql.base PGTypeCompiler code examples
category: page
slug: sqlalchemy-dialects-postgresql-base-pgtypecompiler-examples
sortorder: 500031013
toc: False
sidebartitle: sqlalchemy.dialects.postgresql.base PGTypeCompiler
meta: Python example code for the PGTypeCompiler class from the sqlalchemy.dialects.postgresql.base module of the SQLAlchemy project.


PGTypeCompiler is a class within the sqlalchemy.dialects.postgresql.base module of the SQLAlchemy project.


## Example 1 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlalchemy.html) when building
projects that involve more specific storage requirements such as
[currency](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.currency).
The wide array of
[data types](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html)
includes [ranged values](https://sqlalchemy-utils.readthedocs.io/en/latest/range_data_types.html)
and [aggregated attributes](https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html).

[**sqlalchemy-utils / sqlalchemy_utils / types / ltree.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/types/ltree.py)

```python
# ltree.py
from __future__ import absolute_import

from sqlalchemy import types
from sqlalchemy.dialects.postgresql import ARRAY
~~from sqlalchemy.dialects.postgresql.base import ischema_names, PGTypeCompiler
from sqlalchemy.sql import expression

from ..primitives import Ltree
from .scalar_coercible import ScalarCoercible


class LtreeType(types.Concatenable, types.UserDefinedType, ScalarCoercible):

    class comparator_factory(types.Concatenable.Comparator):
        def ancestor_of(self, other):
            if isinstance(other, list):
                return self.op('@>')(expression.cast(other, ARRAY(LtreeType)))
            else:
                return self.op('@>')(other)

        def descendant_of(self, other):
            if isinstance(other, list):
                return self.op('<@')(expression.cast(other, ARRAY(LtreeType)))
            else:
                return self.op('<@')(other)

        def lquery(self, other):
            if isinstance(other, list):
                return self.op('?')(expression.cast(other, ARRAY(LQUERY)))


## ... source file continues with no further PGTypeCompiler examples...

```

