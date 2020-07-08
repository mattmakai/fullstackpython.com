title: django.forms MediaDefiningClass Example Code
category: page
slug: django-forms-mediadefiningclass-examples
sortorder: 500011271
toc: False
sidebartitle: django.forms MediaDefiningClass
meta: Python example code for the MediaDefiningClass class from the django.forms module of the Django project.


MediaDefiningClass is a class within the django.forms module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / toolbar_base.py**](https://github.com/divio/django-cms/blob/develop/cms/./toolbar_base.py)

```python
# toolbar_base.py
~~from django.forms import MediaDefiningClass

from six import with_metaclass

from cms.exceptions import LanguageError
from cms.utils import get_current_site, get_language_from_request
from cms.utils.i18n import get_language_object


~~class CMSToolbar(with_metaclass(MediaDefiningClass)):
    supported_apps = None

    def __init__(self, request, toolbar, is_current_app, app_path):
        self.request = request
        self.toolbar = toolbar
        self.is_current_app = is_current_app
        self.app_path = app_path
        self.current_site = get_current_site()
        try:
            self.current_lang = get_language_object(get_language_from_request(self.request), self.current_site.pk)['code']
        except LanguageError:
            self.current_lang = None

    def populate(self):
        pass

    def post_template_populate(self):
        pass

    @classmethod
    def check_current_app(cls, key, app_name):
        if cls.supported_apps is None:
            local_apps = ".".join(key.split(".")[:-2]),
        else:


## ... source file continues with no further MediaDefiningClass examples...

```


## Example 2 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / admin / menu.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/admin/menu.py)

```python
# menu.py
~~from django.forms import Media, MediaDefiningClass
from django.forms.utils import flatatt
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from wagtail.core import hooks


class MenuItem(metaclass=MediaDefiningClass):
    template = 'wagtailadmin/shared/menu_item.html'

    def __init__(self, label, url, name=None, classnames='', icon_name='', attrs=None, order=1000):
        self.label = label
        self.url = url
        self.classnames = classnames
        self.icon_name = icon_name
        self.name = (name or slugify(str(label)))
        self.order = order

        if attrs:
            self.attr_string = flatatt(attrs)
        else:
            self.attr_string = ""



## ... source file continues with no further MediaDefiningClass examples...

```

