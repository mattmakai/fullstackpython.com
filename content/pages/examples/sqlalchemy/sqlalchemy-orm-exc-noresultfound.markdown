title: sqlalchemy.orm.exc NoResultFound code examples
category: page
slug: sqlalchemy-orm-exc-noresultfound-examples
sortorder: 500031046
toc: False
sidebartitle: sqlalchemy.orm.exc NoResultFound
meta: Python example code for the NoResultFound class from the sqlalchemy.orm.exc module of the SQLAlchemy project.


NoResultFound is a class within the sqlalchemy.orm.exc module of the SQLAlchemy project.


## Example 1 from marshmallow-sqlalchemy
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

