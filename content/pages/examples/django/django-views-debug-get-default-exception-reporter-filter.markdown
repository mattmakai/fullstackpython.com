title: django.views.debug get_default_exception_reporter_filter Example Code
category: page
slug: django-views-debug-get-default-exception-reporter-filter-examples
sortorder: 500011515
toc: False
sidebartitle: django.views.debug get_default_exception_reporter_filter
meta: Python example code for the get_default_exception_reporter_filter callable from the django.views.debug module of the Django project.


get_default_exception_reporter_filter is a callable within the django.views.debug module of the Django project.


## Example 1 from django-debug-toolbar
[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
([project documentation](https://github.com/jazzband/django-debug-toolbar)
and [PyPI page](https://pypi.org/project/django-debug-toolbar/))
grants a developer detailed request-response cycle information while
developing a [Django](/django.html) web application.
The code for django-debug-toolbar is
[open source](https://github.com/jazzband/django-debug-toolbar/blob/master/LICENSE)
and maintained by the developer community group known as
[Jazzband](https://jazzband.co/).

[**django-debug-toolbar / debug_toolbar / panels / settings.py**](https://github.com/jazzband/django-debug-toolbar/blob/master/debug_toolbar/panels/settings.py)

```python
# settings.py
from collections import OrderedDict

import django
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from debug_toolbar.panels import Panel

if django.VERSION >= (3, 1):
~~    from django.views.debug import get_default_exception_reporter_filter

~~    get_safe_settings = get_default_exception_reporter_filter().get_safe_settings
else:
    from django.views.debug import get_safe_settings


class SettingsPanel(Panel):

    template = "debug_toolbar/panels/settings.html"

    nav_title = _("Settings")

    def title(self):
        return _("Settings from <code>%s</code>") % settings.SETTINGS_MODULE

    def generate_stats(self, request, response):
        self.record_stats(
            {
                "settings": OrderedDict(
                    sorted(get_safe_settings().items(), key=lambda s: s[0])
                )
            }
        )



## ... source file continues with no further get_default_exception_reporter_filter examples...

```

