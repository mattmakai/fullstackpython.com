title: django.views.i18n JavaScriptCatalog Example Code
category: page
slug: django-views-i18n-javascriptcatalog-examples
sortorder: 500011541
toc: False
sidebartitle: django.views.i18n JavaScriptCatalog
meta: Python example code for the JavaScriptCatalog class from the django.views.i18n module of the Django project.


JavaScriptCatalog is a class within the django.views.i18n module of the Django project.


## Example 1 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / urls.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/./urls.py)

```python
# urls.py
import django
from django.conf.urls import url

try:
~~    from django.views.i18n import JavaScriptCatalog
~~    javascript_catalog = JavaScriptCatalog.as_view()
except ImportError:  # Django < 2.0
    from django.views.i18n import javascript_catalog

from jet.views import add_bookmark_view, remove_bookmark_view, toggle_application_pin_view, model_lookup_view


app_name = 'jet'

urlpatterns = [
    url(
        r'^add_bookmark/$',
        add_bookmark_view,
        name='add_bookmark'
    ),
    url(
        r'^remove_bookmark/$',
        remove_bookmark_view,
        name='remove_bookmark'
    ),
    url(
        r'^toggle_application_pin/$',
        toggle_application_pin_view,
        name='toggle_application_pin'
    ),


## ... source file continues with no further JavaScriptCatalog examples...

```

