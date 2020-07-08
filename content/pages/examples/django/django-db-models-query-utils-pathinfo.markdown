title: django.db.models.query_utils PathInfo Example Code
category: page
slug: django-db-models-query-utils-pathinfo-examples
sortorder: 500011246
toc: False
sidebartitle: django.db.models.query_utils PathInfo
meta: Python example code for the PathInfo class from the django.db.models.query_utils module of the Django project.


PathInfo is a class within the django.db.models.query_utils module of the Django project.


## Example 1 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / managers.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/./managers.py)

```python
# managers.py
import uuid
from operator import attrgetter

from django import VERSION
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import connections, models, router
from django.db.models import signals
from django.db.models.fields.related import (
    ManyToManyRel,
    OneToOneRel,
    RelatedField,
    lazy_related_operation,
)
~~from django.db.models.query_utils import PathInfo
from django.utils.text import capfirst
from django.utils.translation import gettext_lazy as _

from taggit.forms import TagField
from taggit.models import (
    CommonGenericTaggedItemBase,
    GenericUUIDTaggedItemBase,
    TaggedItem,
)
from taggit.utils import require_instance_manager


class ExtraJoinRestriction:

    contains_aggregate = False

    def __init__(self, alias, col, content_types):
        self.alias = alias
        self.col = col
        self.content_types = content_types

    def as_sql(self, compiler, connection):
        qn = compiler.quote_name_unless_alias
        if len(self.content_types) == 1:


## ... source file abbreviated to get to PathInfo examples ...


                    filtered_relation=filtered_relation
                )
        else:
            if VERSION < (2, 0):
                join1infos = linkfield2.get_reverse_path_info()
                join2infos = linkfield1.get_path_info()
            else:
                join1infos = linkfield2.get_reverse_path_info(
                    filtered_relation=filtered_relation
                )
                join2infos = linkfield1.get_path_info(
                    filtered_relation=filtered_relation
                )
        pathinfos.extend(join1infos)
        pathinfos.extend(join2infos)
        return pathinfos

    def _get_gfk_case_path_info(self, direct=False, filtered_relation=None):
        pathinfos = []
        from_field = self.model._meta.pk
        opts = self.through._meta
        linkfield = self.through._meta.get_field(self.m2m_reverse_field_name())
        if direct:
            if VERSION < (2, 0):
                join1infos = [
~~                    PathInfo(
                        self.model._meta,
                        opts,
                        [from_field],
                        self.remote_field,
                        True,
                        False,
                    )
                ]
                join2infos = linkfield.get_path_info()
            else:
                join1infos = [
~~                    PathInfo(
                        self.model._meta,
                        opts,
                        [from_field],
                        self.remote_field,
                        True,
                        False,
                        filtered_relation,
                    )
                ]
                join2infos = linkfield.get_path_info(
                    filtered_relation=filtered_relation
                )
        else:
            if VERSION < (2, 0):
                join1infos = linkfield.get_reverse_path_info()
                join2infos = [
~~                    PathInfo(opts, self.model._meta, [from_field], self, True, False)
                ]
            else:
                join1infos = linkfield.get_reverse_path_info(
                    filtered_relation=filtered_relation
                )
                join2infos = [
~~                    PathInfo(
                        opts,
                        self.model._meta,
                        [from_field],
                        self,
                        True,
                        False,
                        filtered_relation,
                    )
                ]
        pathinfos.extend(join1infos)
        pathinfos.extend(join2infos)
        return pathinfos

    def get_path_info(self, filtered_relation=None):
        if self.use_gfk:
            return self._get_gfk_case_path_info(
                direct=True, filtered_relation=filtered_relation
            )
        else:
            return self._get_mm_case_path_info(
                direct=True, filtered_relation=filtered_relation
            )

    def get_reverse_path_info(self, filtered_relation=None):


## ... source file continues with no further PathInfo examples...

```

