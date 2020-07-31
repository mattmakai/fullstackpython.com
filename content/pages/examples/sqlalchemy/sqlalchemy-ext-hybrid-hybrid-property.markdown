title: sqlalchemy.ext.hybrid hybrid_property Example Code
category: page
slug: sqlalchemy-ext-hybrid-hybrid-property-examples
sortorder: 500031051
toc: False
sidebartitle: sqlalchemy.ext.hybrid hybrid_property
meta: Python example code that shows how to use the hybrid_property callable from the sqlalchemy.ext.hybrid module of the SQLAlchemy project.


`hybrid_property` is a callable within the `sqlalchemy.ext.hybrid` module of the SQLAlchemy project.

<a href="/sqlalchemy-ext-hybrid-hybrid-method-examples.html">HYBRID_METHOD</a>,
<a href="/sqlalchemy-ext-hybrid-hybrid-method-examples.html">hybrid_method</a>,
and <a href="/sqlalchemy-ext-hybrid-hybrid-property-examples.html">hybrid_property</a>
are several other callables with code examples from the same `sqlalchemy.ext.hybrid` package.

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

[**sqlalchemy-utils / sqlalchemy_utils / i18n.py**](https://github.com/kvesteri/sqlalchemy-utils/blob/master/sqlalchemy_utils/./i18n.py)

```python
# i18n.py
import inspect

import six
import sqlalchemy as sa
from sqlalchemy.ext.compiler import compiles
~~from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.sql.expression import ColumnElement

from .exceptions import ImproperlyConfigured

try:
    import babel
    import babel.dates
except ImportError:
    babel = None


def get_locale():
    try:
        return babel.Locale('en')
    except AttributeError:
        raise ImproperlyConfigured(
            'Could not load get_locale function using Babel. Either '
            'install Babel or make a similar function and override it '
            'in this module.'
        )


if six.PY2:
    def get_args_count(func):


## ... source file abbreviated to get to hybrid_property examples ...


                    return getattr(obj, attr.key)[default_locale]
                except (TypeError, KeyError):
                    return self.default_value
        return getter

    def setter_factory(self, attr):
        def setter(obj, value):
            if getattr(obj, attr.key) is None:
                setattr(obj, attr.key, {})
            locale = cast_locale(obj, self.current_locale, attr)
            getattr(obj, attr.key)[locale] = value
        return setter

    def expr_factory(self, attr):
        def expr(cls):
            cls_attr = getattr(cls, attr.key)
            current_locale = cast_locale_expr(cls, self.current_locale, attr)
            default_locale = cast_locale_expr(cls, self.default_locale, attr)
            return sa.func.coalesce(
                cls_attr[current_locale],
                cls_attr[default_locale]
            )
        return expr

    def __call__(self, attr):
~~        return hybrid_property(
            fget=self.getter_factory(attr),
            fset=self.setter_factory(attr),
            expr=self.expr_factory(attr)
        )



## ... source file continues with no further hybrid_property examples...

```

