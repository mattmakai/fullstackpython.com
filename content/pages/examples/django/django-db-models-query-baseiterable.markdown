title: django.db.models.query BaseIterable Example Code
category: page
slug: django-db-models-query-baseiterable-examples
sortorder: 500011238
toc: False
sidebartitle: django.db.models.query BaseIterable
meta: Python example code for the BaseIterable class from the django.db.models.query module of the Django project.


BaseIterable is a class within the django.db.models.query module of the Django project.


## Example 1 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / query.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/query.py)

```python
# query.py
import posixpath
import warnings
from collections import defaultdict

from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.db.models import CharField, Q
from django.db.models.functions import Length, Substr
~~from django.db.models.query import BaseIterable
from treebeard.mp_tree import MP_NodeQuerySet

from wagtail.search.queryset import SearchableQuerySetMixin


class TreeQuerySet(MP_NodeQuerySet):
    def delete(self):
        super().delete()

    delete.queryset_only = True

    def descendant_of_q(self, other, inclusive=False):
        q = Q(path__startswith=other.path) & Q(depth__gte=other.depth)

        if not inclusive:
            q &= -Q(pk=other.pk)

        return q

    def descendant_of(self, other, inclusive=False):
        return self.filter(self.descendant_of_q(other, inclusive))

    def not_descendant_of(self, other, inclusive=False):
        return self.exclude(self.descendant_of_q(other, inclusive))


## ... source file abbreviated to get to BaseIterable examples ...



    if missing_pks:
        generic_pages = Page.objects.filter(pk__in=missing_pks).select_related('content_type').in_bulk()
        warnings.warn(
            "Specific versions of the following pages could not be found. "
            "This is most likely because a database migration has removed "
            "the relevant table or record since the page was created:\n{}".format([
                {'id': p.id, 'title': p.title, 'type': p.content_type}
                for p in generic_pages.values()
            ]), category=RuntimeWarning
        )
    else:
        generic_pages = {}

    for pk, content_type in pks_and_types:
        try:
            page = pages_by_type[content_type][pk]
        except KeyError:
            page = generic_pages[pk]
        if annotation_aliases:
            for annotation, value in annotations_by_pk.get(page.pk, {}).items():
                setattr(page, annotation, value)
        yield page


~~class SpecificIterable(BaseIterable):
    def __iter__(self):
        return specific_iterator(self.queryset)


~~class DeferredSpecificIterable(BaseIterable):
    def __iter__(self):
        return specific_iterator(self.queryset, defer=True)



## ... source file continues with no further BaseIterable examples...

```

