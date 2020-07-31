title: sqlalchemy.orm.exc NoResultFound Example Code
category: page
slug: sqlalchemy-orm-exc-noresultfound-examples
sortorder: 500031080
toc: False
sidebartitle: sqlalchemy.orm.exc NoResultFound
meta: Example code for understanding how to use the NoResultFound class from the sqlalchemy.orm.exc module of the SQLAlchemy project.


`NoResultFound` is a class within the `sqlalchemy.orm.exc` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-exc-unmappedclasserror-examples.html">UnmappedClassError</a>
and
<a href="/sqlalchemy-orm-exc-unmappedinstanceerror-examples.html">UnmappedInstanceError</a>
are a couple of other callables within the `sqlalchemy.orm.exc` package that also have code examples.

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

[**graphene-sqlalchemy / graphene_sqlalchemy / types.py**](https://github.com/graphql-python/graphene-sqlalchemy/blob/master/graphene_sqlalchemy/./types.py)

```python
# types.py
from collections import OrderedDict

import sqlalchemy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import (ColumnProperty, CompositeProperty,
                            RelationshipProperty)
~~from sqlalchemy.orm.exc import NoResultFound

from graphene import Field
from graphene.relay import Connection, Node
from graphene.types.objecttype import ObjectType, ObjectTypeOptions
from graphene.types.utils import yank_fields_from_attrs
from graphene.utils.orderedtype import OrderedType

from .converter import (convert_sqlalchemy_column,
                        convert_sqlalchemy_composite,
                        convert_sqlalchemy_hybrid_method,
                        convert_sqlalchemy_relationship)
from .enums import (enum_for_field, sort_argument_for_object_type,
                    sort_enum_for_object_type)
from .registry import Registry, get_global_registry
from .resolvers import get_attr_resolver, get_custom_resolver
from .utils import get_query, is_mapped_class, is_mapped_instance


class ORMField(OrderedType):
    def __init__(
        self,
        model_attr=None,
        type=None,
        required=None,


## ... source file abbreviated to get to NoResultFound examples ...



        super(SQLAlchemyObjectType, cls).__init_subclass_with_meta__(
            _meta=_meta, interfaces=interfaces, **options
        )

        if not skip_registry:
            registry.register(cls)

    @classmethod
    def is_type_of(cls, root, info):
        if isinstance(root, cls):
            return True
        if not is_mapped_instance(root):
            raise Exception(('Received incompatible instance "{}".').format(root))
        return isinstance(root, cls._meta.model)

    @classmethod
    def get_query(cls, info):
        model = cls._meta.model
        return get_query(model, info.context)

    @classmethod
    def get_node(cls, info, id):
        try:
            return cls.get_query(info).get(id)
~~        except NoResultFound:
            return None

    def resolve_id(self, info):
        keys = self.__mapper__.primary_key_from_instance(self)
        return tuple(keys) if len(keys) > 1 else keys[0]

    @classmethod
    def enum_for_field(cls, field_name):
        return enum_for_field(cls, field_name)

    sort_enum = classmethod(sort_enum_for_object_type)

    sort_argument = classmethod(sort_argument_for_object_type)



## ... source file continues with no further NoResultFound examples...

```


## Example 2 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management that is
powered by [SQLAlchemy](/sqlalchemy.html) on the backend. The code
for this project is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / web / rh.py**](https://github.com/indico/indico/blob/master/indico/web/rh.py)

```python
# rh.py

from __future__ import absolute_import, unicode_literals

import cProfile
import inspect
import itertools
import os
import time
from functools import partial, wraps

import jsonschema
from flask import current_app, g, redirect, request, session
from sqlalchemy.exc import DatabaseError
~~from sqlalchemy.orm.exc import NoResultFound
from werkzeug.exceptions import BadRequest, Forbidden, MethodNotAllowed, NotFound
from werkzeug.routing import BuildError
from werkzeug.wrappers import Response

from indico.core import signals
from indico.core.config import config
from indico.core.db import db
from indico.core.db.sqlalchemy.core import handle_sqlalchemy_database_error
from indico.core.logger import Logger, sentry_set_tags
from indico.core.notifications import flush_email_queue, init_email_queue
from indico.util import fossilize
from indico.util.i18n import _
from indico.util.locators import get_locator
from indico.util.signals import values_from_signal
from indico.web.flask.util import url_for
from indico.web.util import is_signed_url_valid


HTTP_VERBS = {'GET', 'PATCH', 'POST', 'PUT', 'DELETE'}
logger = Logger.get('rh')


class RH(object):
    CSRF_ENABLED = True  # require a csrf_token when accessing the RH with anything but GET


## ... source file abbreviated to get to NoResultFound examples ...


            valid_methods = [m for m in HTTP_VERBS if hasattr(self, '_process_' + m)]
            raise MethodNotAllowed(valid_methods)
        return method()

    def _check_csrf(self):
        token = request.headers.get('X-CSRF-Token') or request.form.get('csrf_token')
        if token is None:
            token = next((v for k, v in request.form.iteritems() if k.endswith('-csrf_token')), None)
        if self.CSRF_ENABLED and request.method != 'GET' and token != session.csrf_token:
            msg = _("It looks like there was a problem with your current session. Please use your browser's back "
                    "button, reload the page and try again.")
            raise BadRequest(msg)

    def _check_event_feature(self):
        from indico.modules.events.features.util import require_feature
        event_id = request.view_args.get('confId') or request.view_args.get('event_id')
        if event_id is not None:
            require_feature(event_id, self.EVENT_FEATURE)

    def _do_process(self):
        try:
            args_result = self._process_args()
            signals.rh.process_args.send(type(self), rh=self, result=args_result)
            if isinstance(args_result, (current_app.response_class, Response)):
                return args_result
~~        except NoResultFound:  # sqlalchemy .one() not finding anything
            raise NotFound(_('The specified item could not be found.'))

        rv = self.normalize_url()
        if rv is not None:
            return rv

        self._check_access()
        signals.rh.check_access.send(type(self), rh=self)

        signal_rv = values_from_signal(signals.rh.before_process.send(type(self), rh=self),
                                       single_value=True, as_list=True)
        if signal_rv and len(signal_rv) != 1:
            raise Exception('More than one signal handler returned custom RH result')
        elif signal_rv:
            return signal_rv[0]

        if config.PROFILE:
            result = [None]
            profile_path = os.path.join(config.TEMP_DIR, '{}-{}.prof'.format(type(self).__name__, time.time()))
            cProfile.runctx('result[0] = self._process()', globals(), locals(), profile_path)
            rv = result[0]
        else:
            rv = self._process()



## ... source file continues with no further NoResultFound examples...

```


## Example 3 from marshmallow-sqlalchemy
[marshmallow-sqlalchemy](https://github.com/marshmallow-code/marshmallow-sqlalchemy)
([project documentation](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/))
is a code library that makes it easier to use
[SQLAlchemy](/sqlalchemy.html) with the
[Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
data serialization tool.

The marshmallow-sqlalchemy project is provided as open source under the
[MIT license](https://github.com/marshmallow-code/marshmallow-sqlalchemy/blob/dev/LICENSE).

[**marshmallow-sqlalchemy / src/marshmallow_sqlalchemy / fields.py**](https://github.com/marshmallow-code/marshmallow-sqlalchemy/blob/dev/src/marshmallow_sqlalchemy/./fields.py)

```python
# fields.py
from marshmallow import fields
from marshmallow.utils import is_iterable_but_not_string

from sqlalchemy import inspect
~~from sqlalchemy.orm.exc import NoResultFound


def get_primary_keys(model):
    mapper = model.__mapper__
    return [mapper.get_property_by_column(column) for column in mapper.primary_key]


def ensure_list(value):
    return value if is_iterable_but_not_string(value) else [value]


class RelatedList(fields.List):
    def get_value(self, obj, attr, accessor=None):
        return super(fields.List, self).get_value(obj, attr, accessor=accessor)


class Related(fields.Field):

    default_error_messages = {
        "invalid": "Could not deserialize related value {value!r}; "
        "expected a dictionary with keys {keys!r}"
    }

    def __init__(self, column=None, **kwargs):


## ... source file abbreviated to get to NoResultFound examples ...


        return self.root.session

    @property
    def transient(self):
        return self.root.transient

    def _serialize(self, value, attr, obj):
        ret = {prop.key: getattr(value, prop.key, None) for prop in self.related_keys}
        return ret if len(ret) > 1 else list(ret.values())[0]

    def _deserialize(self, value, *args, **kwargs):
        if not isinstance(value, dict):
            if len(self.related_keys) != 1:
                keys = [prop.key for prop in self.related_keys]
                if hasattr(self, "make_error"):
                    raise self.make_error("invalid", value=value, keys=keys)
                else:  # marshmallow 2
                    self.fail("invalid", value=value, keys=keys)
            value = {self.related_keys[0].key: value}
        if self.transient:
            return self.related_model(**value)
        try:
            result = self._get_existing_instance(
                self.session.query(self.related_model), value
            )
~~        except NoResultFound:
            return self.related_model(**value)
        return result

    def _get_existing_instance(self, query, value):
        if self.columns:
            result = query.filter_by(
                **{prop.key: value.get(prop.key) for prop in self.related_keys}
            ).one()
        else:
            lookup_values = [value.get(prop.key) for prop in self.related_keys]
            try:
                result = query.get(lookup_values)
            except TypeError:
                keys = [prop.key for prop in self.related_keys]
                if hasattr(self, "make_error"):
                    raise self.make_error("invalid", value=value, keys=keys)
                else:  # marshmallow 2
                    self.fail("invalid", value=value, keys=keys)
            if result is None:
~~                raise NoResultFound
        return result


class Nested(fields.Nested):

    def _deserialize(self, *args, **kwargs):
        if hasattr(self.schema, "session"):
            self.schema.session = self.root.session
            self.schema.transient = self.root.transient
        return super()._deserialize(*args, **kwargs)



## ... source file continues with no further NoResultFound examples...

```

