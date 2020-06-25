title: sqlalchemy.dialects.postgresql ARRAY code examples
category: page
slug: sqlalchemy-dialects-postgresql-array-examples
sortorder: 500031005
toc: False
sidebartitle: sqlalchemy.dialects.postgresql ARRAY
meta: Python example code for the ARRAY class from the sqlalchemy.dialects.postgresql module of the SQLAlchemy project.


ARRAY is a class within the sqlalchemy.dialects.postgresql module of the SQLAlchemy project.


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

[**sqlalchemy-utils / sqlalchemy_utils / asserts.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./asserts.py)

```python
# asserts.py
from decimal import Decimal

import sqlalchemy as sa
~~from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.exc import DataError, IntegrityError


def _update_field(obj, field, value):
    session = sa.orm.object_session(obj)
    column = sa.inspect(obj.__class__).columns[field]
    query = column.table.update().values(**{column.key: value})
    session.execute(query)
    session.flush()


def _expect_successful_update(obj, field, value, reraise_exc):
    try:
        _update_field(obj, field, value)
    except (reraise_exc) as e:
        session = sa.orm.object_session(obj)
        session.rollback()
        assert False, str(e)


def _expect_failing_update(obj, field, value, expected_exc):
    try:
        _update_field(obj, field, value)
    except expected_exc:
        pass
    else:
        raise AssertionError('Expected update to raise %s' % expected_exc)
    finally:
        session = sa.orm.object_session(obj)
        session.rollback()


def _repeated_value(type_):
~~    if isinstance(type_, ARRAY):
        if isinstance(type_.item_type, sa.Integer):
            return [0]
        elif isinstance(type_.item_type, sa.String):
            return [u'a']
        elif isinstance(type_.item_type, sa.Numeric):
            return [Decimal('0')]
        else:
            raise TypeError('Unknown array item type')
    else:
        return u'a'


def _expected_exception(type_):
~~    if isinstance(type_, ARRAY):
        return IntegrityError
    else:
        return DataError


def assert_nullable(obj, column):
    _expect_successful_update(obj, column, None, IntegrityError)


def assert_non_nullable(obj, column):
    _expect_failing_update(obj, column, None, IntegrityError)


def assert_max_length(obj, column, max_length):
    type_ = sa.inspect(obj.__class__).columns[column].type
    _expect_successful_update(
        obj,
        column,
        _repeated_value(type_) * max_length,
        _expected_exception(type_)
    )
    _expect_failing_update(
        obj,
        column,


## ... source file continues with no further ARRAY examples...

```

