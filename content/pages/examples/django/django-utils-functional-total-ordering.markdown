title: django.utils.functional total_ordering Example Code
category: page
slug: django-utils-functional-total-ordering-examples
sortorder: 500011459
toc: False
sidebartitle: django.utils.functional total_ordering
meta: Python example code for the total_ordering callable from the django.utils.functional module of the Django project.


total_ordering is a callable within the django.utils.functional module of the Django project.


## Example 1 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / admin / search.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/admin/search.py)

```python
# search.py
from django.forms import Media, MediaDefiningClass
from django.forms.utils import flatatt
from django.template.loader import render_to_string
~~from django.utils.functional import cached_property, total_ordering
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from wagtail.admin.forms.search import SearchForm
from wagtail.core import hooks


~~@total_ordering
class SearchArea(metaclass=MediaDefiningClass):
    template = 'wagtailadmin/shared/search_area.html'

    def __init__(self, label, url, name=None, classnames='', attrs=None, order=1000):
        self.label = label
        self.url = url
        self.classnames = classnames
        self.name = (name or slugify(str(label)))
        self.order = order

        if attrs:
            self.attr_string = flatatt(attrs)
        else:
            self.attr_string = ""

    def __lt__(self, other):
        return (self.order, self.label) < (other.order, other.label)

    def __eq__(self, other):
        return (self.order, self.label) == (other.order, other.label)

    def is_shown(self, request):
        return True



## ... source file continues with no further total_ordering examples...

```

