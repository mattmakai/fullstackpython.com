title: sqlalchemy.orm.query Query Example Code
category: page
slug: sqlalchemy-orm-query-query-examples
sortorder: 500031088
toc: False
sidebartitle: sqlalchemy.orm.query Query
meta: Example code for understanding how to use the Query class from the sqlalchemy.orm.query module of the SQLAlchemy project.


`Query` is a class within the `sqlalchemy.orm.query` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-query-querycontext-examples.html">QueryContext</a>
is another callable from the `sqlalchemy.orm.query` package with code examples.

## Example 1 from graphene-sqlalchemy
[graphene-sqlalchemy](https://github.com/graphql-python/graphene-sqlalchemy)
([project documentation](https://docs.graphene-python.org/projects/sqlalchemy/en/latest/)
and
[PyPI package information](https://pypi.org/project/graphene-sqlalchemy/))
is a [SQLAlchemy](/sqlalchemy.html) integration for
[Graphene](https://graphene-python.org/), which makes it easier to build
GraphQL-based [APIs](/application-programming-interfaces.html) into Python
[web applications](/web-development.html). The package allows you to
subclass SQLAlchemy classes and build queries around them with custom
code to match the backend queries with the GraphQL-based request queries.
The project is provided as open source under the
[MIT license](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/LICENSE.md).

[**graphene-sqlalchemy / graphene_sqlalchemy / fields.py**](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/graphene_sqlalchemy/./fields.py)

```python
# fields.py
import warnings
from functools import partial

import six
from promise import Promise, is_thenable
~~from sqlalchemy.orm.query import Query

from graphene import NonNull
from graphene.relay import Connection, ConnectionField
from graphene.relay.connection import PageInfo
from graphql_relay.connection.arrayconnection import connection_from_list_slice

from .batching import get_batch_resolver
from .utils import get_query


class UnsortedSQLAlchemyConnectionField(ConnectionField):
    @property
    def type(self):
        from .types import SQLAlchemyObjectType

        _type = super(ConnectionField, self).type
        nullable_type = get_nullable_type(_type)
        if issubclass(nullable_type, Connection):
            return _type
        assert issubclass(nullable_type, SQLAlchemyObjectType), (
            "SQLALchemyConnectionField only accepts SQLAlchemyObjectType types, not {}"
        ).format(nullable_type.__name__)
        assert (
            nullable_type.connection
        ), "The type {} doesn't have a connection".format(
            nullable_type.__name__
        )
        assert _type == nullable_type, (
            "Passing a SQLAlchemyObjectType instance is deprecated. "
            "Pass the connection type instead accessible via SQLAlchemyObjectType.connection"
        )
        return nullable_type.connection

    @property
    def model(self):
        return get_nullable_type(self.type)._meta.node._meta.model

    @classmethod
    def get_query(cls, model, info, **args):
        return get_query(model, info.context)

    @classmethod
    def resolve_connection(cls, connection_type, model, info, args, resolved):
        if resolved is None:
            resolved = cls.get_query(model, info, **args)
~~        if isinstance(resolved, Query):
            _len = resolved.count()
        else:
            _len = len(resolved)
        connection = connection_from_list_slice(
            resolved,
            args,
            slice_start=0,
            list_length=_len,
            list_slice_length=_len,
            connection_type=connection_type,
            pageinfo_type=PageInfo,
            edge_type=connection_type.Edge,
        )
        connection.iterable = resolved
        connection.length = _len
        return connection

    @classmethod
    def connection_resolver(cls, resolver, connection_type, model, root, info, **args):
        resolved = resolver(root, info, **args)

        on_resolve = partial(cls.resolve_connection, connection_type, model, info, args)
        if is_thenable(resolved):
            return Promise.resolve(resolved).then(on_resolve)


## ... source file continues with no further Query examples...

```

