title: flask.helpers url_for Python code examples
category: page
slug: flask-helpers-url-for-examples
sortorder: 500021001
toc: False
sidebartitle: flask.helpers url_for
meta: Python example code for the url_for function from the flask.helpers module of the Flask project.


url_for is a function within the flask.helpers module of the Flask project.


## Example 1 from flask-base
[flask-base](https://github.com/hack4impact/flask-base)
([project documentation](http://hack4impact.github.io/flask-base/))
provides boilerplate code for new [Flask](/flask.html) web apps.
The purpose of the boilerplate is to stitch together disparate
libraries that are commonly used in Flask projects, such as
[Redis](/redis.html) for fast caching and transient data storage,
[SendGrid](https://www.twilio.com/sendgrid) for transactional email,
[SQLAlchemy](/sqlalchemy.html) for persistent data storage through a
[relational database](/databases.html) backend,
[Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/) for form
handling and many others.

flask-base is provided as open source under the
[MIT license](https://github.com/hack4impact/flask-base/blob/master/LICENSE.md).

[**flask-base / app / utils.py**](https://github.com/hack4impact/flask-base/blob/master/app/./utils.py)

```python
~~from flask import url_for
from wtforms.fields import Field
from wtforms.widgets import HiddenInput
from wtforms.compat import text_type


def register_template_utils(app):
    """Register Jinja 2 helpers (called from __init__.py)."""

    @app.template_test()
    def equalto(value, other):
        return value == other

    @app.template_global()
    def is_hidden_field(field):
        from wtforms.fields import HiddenField
        return isinstance(field, HiddenField)

    app.add_template_global(index_for_role)


def index_for_role(role):
~~    return url_for(role.index)




## ... source file abbreviated to get to url_for examples ...


class CustomSelectField(Field):
    widget = HiddenInput()

    def __init__(self, label='', validators=None, multiple=False,
                 choices=[], allow_custom=True, **kwargs):
        super(CustomSelectField, self).__init__(label, validators, **kwargs)
        self.multiple = multiple
        self.choices = choices
        self.allow_custom = allow_custom

    def _value(self):
        return text_type(self.data) if self.data is not None else ''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = valuelist[1]
            self.raw_data = [valuelist[1]]
        else:
            self.data = ''


## ... source file continues with no further url_for examples...


```

