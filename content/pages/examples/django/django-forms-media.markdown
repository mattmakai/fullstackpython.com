title: django.forms Media Example Code
category: page
slug: django-forms-media-examples
sortorder: 500011270
toc: False
sidebartitle: django.forms Media
meta: Python example code for the Media class from the django.forms module of the Django project.


Media is a class within the django.forms module of the Django project.


## Example 1 from wagtail
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



## ... source file abbreviated to get to Media examples ...


    def render_html(self, request):
        context = self.get_context(request)
        return render_to_string(self.template, context, request=request)


class Menu:
    def __init__(self, register_hook_name, construct_hook_name=None):
        self.register_hook_name = register_hook_name
        self.construct_hook_name = construct_hook_name
        self._registered_menu_items = None

    @property
    def registered_menu_items(self):
        if self._registered_menu_items is None:
            self._registered_menu_items = [fn() for fn in hooks.get_hooks(self.register_hook_name)]
        return self._registered_menu_items

    def menu_items_for_request(self, request):
        return [item for item in self.registered_menu_items if item.is_shown(request)]

    def active_menu_items(self, request):
        return [item for item in self.menu_items_for_request(request) if item.is_active(request)]

    @property
    def media(self):
~~        media = Media()
        for item in self.registered_menu_items:
            media += item.media
        return media

    def render_html(self, request):
        menu_items = self.menu_items_for_request(request)

        if self.construct_hook_name:
            for fn in hooks.get_hooks(self.construct_hook_name):
                fn(request, menu_items)

        rendered_menu_items = []
        for item in sorted(menu_items, key=lambda i: i.order):
            rendered_menu_items.append(item.render_html(request))
        return mark_safe(''.join(rendered_menu_items))


class SubmenuMenuItem(MenuItem):
    template = 'wagtailadmin/shared/menu_submenu_item.html'

    def __init__(self, label, menu, **kwargs):
        self.menu = menu
        super().__init__(label, '#', **kwargs)



## ... source file continues with no further Media examples...

```

