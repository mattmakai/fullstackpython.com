title: sqlalchemy.exc DataError code examples
category: page
slug: sqlalchemy-exc-dataerror-examples
sortorder: 500031000
toc: False
sidebartitle: sqlalchemy.exc DataError
meta: Python example code for the DataError class from the sqlalchemy.exc module of the SQLAlchemy project.


DataError is a class within the sqlalchemy.exc module of the SQLAlchemy project.


## Example 1 from sqlalchemy-utils
[sqlalchemy-utils](https://github.com/kvesteri/sqlalchemy-utils)
([project documentation](https://sqlalchemy-utils.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/SQLAlchemy-Utils/))
is a code library with various helper functions and new data types
that make it easier to use [SQLAlchemy](/sqlachemy.html) when building
projects that involve more specific storage requirements such as
[currency](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.currency).
The wide array of
[data types](https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html)
includes [ranged values](https://sqlalchemy-utils.readthedocs.io/en/latest/range_data_types.html)
and [aggregated attributes](https://sqlalchemy-utils.readthedocs.io/en/latest/aggregates.html).

[**sqlalchemy-utils / sqlalchemy_utils / asserts.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./asserts.py)

```python
# asserts.py
We can easily test the constraints by assert_* functions::


    from sqlalchemy_utils import (
        assert_nullable,
        assert_non_nullable,
        assert_max_length
    )

    assert_nullable(user, 'name')
    assert_non_nullable(user, 'email')
    assert_max_length(user, 'name', 200)

    # raises AssertionError because the max length of email is 255
    assert_max_length(user, 'email', 300)
"""
from decimal import Decimal

import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ARRAY
~~from sqlalchemy.exc import DataError, IntegrityError


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


## ... source file abbreviated to get to DataError examples ...




def _repeated_value(type_):
    if isinstance(type_, ARRAY):
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
    if isinstance(type_, ARRAY):
        return IntegrityError
    else:
~~        return DataError


def assert_nullable(obj, column):
    """
    Assert that given column is nullable. This is checked by running an SQL
    update that assigns given column as None.

    :param obj: SQLAlchemy declarative model object
    :param column: Name of the column
    """
    _expect_successful_update(obj, column, None, IntegrityError)


def assert_non_nullable(obj, column):
    """
    Assert that given column is not nullable. This is checked by running an SQL
    update that assigns given column as None.

    :param obj: SQLAlchemy declarative model object
    :param column: Name of the column
    """
    _expect_failing_update(obj, column, None, IntegrityError)




## ... source file continues with no further DataError examples...


```

