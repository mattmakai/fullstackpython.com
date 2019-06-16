title: django.utils.timezone Examples
category: page
slug: django-utils-timezone-examples
sortorder: 50020
toc: False
sidebartitle: django.utils.timezone
meta: Python code examples for timezone-related classes and functions provided by the Django codebase. 


# django.utils.timezone Examples
[timezone.py](https://github.com/django/django/blob/master/django/utils/timezone.py)
is a source file within the [Django](/django.html) project that contains
timezone-related classes and functions that are helpful when building
web applications.

## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/) 
for use with Django web apps that is open sourced under the 
[BSD 3-Clause "New" License](https://github.com/divio/django-cms/blob/develop/LICENSE).

[**django-cms/cms/models/query.py**](https://github.com/divio/django-cms/blob/develop/cms/models/query.py)

```python
# -*- coding: utf-8 -*-
from django.db.models import Q
~~from django.utils import timezone

from treebeard.mp_tree import MP_NodeQuerySet

from cms.publisher.query import PublisherQuerySet
from cms.exceptions import NoHomeFound


class PageQuerySet(PublisherQuerySet):

    def on_site(self, site=None):
        from cms.utils import get_current_site

        if site is None:
            site = get_current_site()
        return self.filter(node__site=site)

    def published(self, site=None, language=None):
~~        now = timezone.now()
        if language:
~~            pub = self.on_site(site).filter(
~~                Q(publication_date__lte=now) | Q(publication_date__isnull=True),
~~                Q(publication_end_date__gt=now) | Q(publication_end_date__isnull=True),
~~                title_set__published=True, title_set__language=language,
            )
        else:
~~            pub = self.on_site(site).filter(
~~                Q(publication_date__lte=now) | Q(publication_date__isnull=True),
~~                Q(publication_end_date__gt=now) | Q(publication_end_date__isnull=True),
~~                title_set__published=True,
            )
        return pub.exclude(title_set__publisher_state=4)
```
