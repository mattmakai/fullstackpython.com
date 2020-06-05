title: flask.views View code examples
category: page
slug: flask-views-view-examples
sortorder: 500021001
toc: False
sidebartitle: flask.views View
meta: Python example code for the View class from the flask.views module of the Flask project.


View is a class within the flask.views module of the Flask project.


## Example 1 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or
[Markdown](/markdown.html).

FlaskBB is provided as open source
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

[**FlaskBB / flaskbb / utils / views.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/utils/views.py)

```python
# views.py
# -*- coding: utf-8 -*-
"""
    flaskbb.utils.views
    -------------------

    This module contains some helpers for creating views.

    :copyright: (c) 2016 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
from flaskbb.utils.helpers import render_template
~~from flask.views import View


~~class RenderableView(View):
    def __init__(self, template, view):
        self.template = template
        self.view = view

    def dispatch_request(self, *args, **kwargs):
        view_model = self.view(*args, **kwargs)
        return render_template(self.template, **view_model)


## ... source file continues with no further View examples...


```

