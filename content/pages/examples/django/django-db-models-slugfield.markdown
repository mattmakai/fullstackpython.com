title: django.db.models SlugField Example Code
category: page
slug: django-db-models-slugfield-examples
sortorder: 500012900
toc: False
sidebartitle: django.db.models SlugField
meta: Python code examples for the Django ORM's SlugField class, found within the django.db.models module of the Django project. 


[SlugField](https://docs.djangoproject.com/en/dev/ref/models/fields/#django.db.models.SlugField)
([source code](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py))
is a field for storing 
[URL slugs](https://stackoverflow.com/questions/427102/what-is-a-slug-in-django)
in a [relational database](/databases.html). SlugField is a column 
defined by the [Django ORM](/django-orm.html).

`SlugField` is actually defined within the 
[django.db.models.fields](https://github.com/django/django/blob/master/django/db/models/fields/__init__.py)
module but is typically imported from
[django.db.models](https://github.com/django/django/tree/master/django/db/models)
rather than including the `fields` module reference.


## Example 1 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a
[Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board / web / gadgets / models.py**](https://github.com/mik4el/gadget-board/blob/master/web/gadgets/models.py)

```python
~~from django.db import models
from django.contrib.postgres.fields import JSONField
from django.template.defaultfilters import slugify
from authentication.models import Account


class Gadget(models.Model):
    name = models.CharField(max_length=40, unique=True)
~~    slug = models.SlugField(null=True, blank=True)
    description = models.TextField()
    users_can_upload = models.ManyToManyField(Account)
    image_name = models.CharField(max_length=140, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def image_url(self):
        if self.image_name != "":
            return "backend/static/media/{}".format(self.image_name)
        else:
            return "backend/static/dashboard_icon_big.png"

    def __str__(self):
        return self.name

~~    def save(self, *args, **kwargs):
~~        if not self.id:
~~            self.slug = slugify(self.name)
~~
~~        super(Gadget, self).save(*args, **kwargs)


class GadgetData(models.Model):
    gadget = models.ForeignKey(Gadget, db_index=True, on_delete=models.DO_NOTHING)  # Add index on filtered fields
    data = JSONField()
    added_by = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(null=True, blank=True, db_index=True)  # Add index on filtered fields
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} {} {}'.format(self.gadget, self.timestamp, self.added_by)

```


## Example 2 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/models.py)

```python
import json
import logging
from collections import defaultdict
from io import StringIO
from urllib.parse import urlparse
from warnings import warn

from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core import checks
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.handlers.base import BaseHandler
from django.core.handlers.wsgi import WSGIRequest
~~from django.db import models, transaction
from django.db.models import Case, Q, Value, When
from django.db.models.functions import Concat, Substr
from django.http import Http404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.text import capfirst, slugify
from django.utils.translation import ugettext_lazy as _
from modelcluster.models import (
    ClusterableModel, get_all_child_m2m_relations, get_all_child_relations)
from treebeard.mp_tree import MP_Node

from wagtail.core.query import PageQuerySet, TreeQuerySet
from wagtail.core.signals import page_published, page_unpublished
from wagtail.core.sites import get_site_for_hostname
from wagtail.core.url_routing import RouteResult
from wagtail.core.utils import WAGTAIL_APPEND_SLASH, camelcase_to_underscore, resolve_model_string
from wagtail.search import index
from wagtail.utils.deprecation import RemovedInWagtail29Warning


## ... code abbreviated to get to the SlugField example ...
class AbstractPage(MP_Node):
    """
    Abstract superclass for Page. According to Django's inheritance rules, managers set on
    abstract models are inherited by subclasses, but managers set on concrete models that are extended
    via multi-table inheritance are not. We therefore need to attach PageManager to an abstract
    superclass to ensure that it is retained by subclasses of Page.
    """
    objects = PageManager()

    class Meta:
        abstract = True


class Page(AbstractPage, index.Indexed, ClusterableModel, metaclass=PageBase):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        help_text=_("The page title as you'd like it to be seen by the public")
    )
    # to reflect title of a current draft in the admin UI
    draft_title = models.CharField(
        max_length=255,
        editable=False
    )
~~    slug = models.SlugField(
~~        verbose_name=_('slug'),
~~        allow_unicode=True,
~~        max_length=255,
~~        help_text=_("The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/")
~~    )
    content_type = models.ForeignKey(
        'contenttypes.ContentType',
        verbose_name=_('content type'),
        related_name='pages',
        on_delete=models.SET(get_default_page_content_type)
    )
    live = models.BooleanField(verbose_name=_('live'), default=True, editable=False)
    has_unpublished_changes = models.BooleanField(
        verbose_name=_('has unpublished changes'),
        default=False,
        editable=False
    )
    url_path = models.TextField(verbose_name=_('URL path'), blank=True, editable=False)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('owner'),
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
        related_name='owned_pages'
    )

## ... code file continues here without further SlugField examples ...
```


## Example 3 from django-taggit
[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
([source code](https://github.com/jazzband/django-debug-toolbar) and
[PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / migrations / 0001_initial.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/migrations/0001_initial.py)

```python
# 0001_initial.py
~~from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("contenttypes", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        help_text="",
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="", unique=True, max_length=100, verbose_name="Name"
                    ),
                ),
~~                (
~~                    "slug",
~~                    models.SlugField(
~~                        help_text="", unique=True, max_length=100, verbose_name="Slug"
~~                    ),
~~                ),
            ],
            options={"verbose_name": "Tag", "verbose_name_plural": "Tags"},
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="TaggedItem",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        help_text="",
                        verbose_name="ID",
                    ),
                ),
                (
                    "object_id",
                    models.IntegerField(
                        help_text="", verbose_name="Object id", db_index=True
                    ),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        related_name="taggit_taggeditem_tagged_items",
                        verbose_name="Content type",
                        to="contenttypes.ContentType",
                        help_text="",
                        on_delete=models.CASCADE,
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        related_name="taggit_taggeditem_items",
                        to="taggit.Tag",
                        help_text="",
                        on_delete=models.CASCADE,
                    ),
                ),
            ],
            options={
                "verbose_name": "Tagged Item",
                "verbose_name_plural": "Tagged Items",
            },
            bases=(models.Model,),
        ),
    ]

```

