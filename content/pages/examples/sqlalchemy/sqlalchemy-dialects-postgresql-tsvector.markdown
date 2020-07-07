title: sqlalchemy.dialects.postgresql TSVECTOR Example Code
category: page
slug: sqlalchemy-dialects-postgresql-tsvector-examples
sortorder: 500031013
toc: False
sidebartitle: sqlalchemy.dialects.postgresql TSVECTOR
meta: Python example code that shows how to use the TSVECTOR constant from the sqlalchemy.dialects.postgresql module of the SQLAlchemy project.


TSVECTOR is a constant within the sqlalchemy.dialects.postgresql module of the SQLAlchemy project.


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

[**sqlalchemy-utils / sqlalchemy_utils / types / ts_vector.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/types/ts_vector.py)

```python
# ts_vector.py
import sqlalchemy as sa
~~from sqlalchemy.dialects.postgresql import TSVECTOR


class TSVectorType(sa.types.TypeDecorator):
    impl = TSVECTOR

    class comparator_factory(TSVECTOR.Comparator):
        def match(self, other, **kwargs):
            if 'postgresql_regconfig' not in kwargs:
                if 'regconfig' in self.type.options:
                    kwargs['postgresql_regconfig'] = (
                        self.type.options['regconfig']
                    )
~~            return TSVECTOR.Comparator.match(self, other, **kwargs)

        def __or__(self, other):
            return self.op('||')(other)

    def __init__(self, *args, **kwargs):
        self.columns = args
        self.options = kwargs
        super(TSVectorType, self).__init__()



## ... source file continues with no further TSVECTOR examples...

```

