title: django.db IntegrityError Example Code
category: page
slug: django-db-integrityerror-examples
sortorder: 500011161
toc: False
sidebartitle: django.db IntegrityError
meta: Python example code for the IntegrityError class from the django.db module of the Django project.


IntegrityError is a class within the django.db module of the Django project.


## Example 1 from django-taggit
[django-taggit](https://github.com/jazzband/django-taggit/)
([PyPI page](https://pypi.org/project/django-taggit/)) provides a way
to create, store, manage and use tags in a [Django](/django.html) project.
The code for django-taggit is
[open source](https://github.com/jazzband/django-taggit/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-taggit / taggit / models.py**](https://github.com/jazzband/django-taggit/blob/master/taggit/./models.py)

```python
# models.py
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
~~from django.db import IntegrityError, models, router, transaction
from django.utils.text import slugify
from django.utils.translation import gettext, gettext_lazy as _

try:
    from unidecode import unidecode
except ImportError:

    def unidecode(tag):
        return tag


class TagBase(models.Model):
    name = models.CharField(verbose_name=_("name"), unique=True, max_length=100)
    slug = models.SlugField(verbose_name=_("slug"), unique=True, max_length=100)

    def __str__(self):
        return self.name

    def __gt__(self, other):
        return self.name.lower() > other.name.lower()

    def __lt__(self, other):
        return self.name.lower() < other.name.lower()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self._state.adding and not self.slug:
            self.slug = self.slugify(self.name)
            using = kwargs.get("using") or router.db_for_write(
                type(self), instance=self
            )
            kwargs["using"] = using
            try:
                with transaction.atomic(using=using):
                    res = super().save(*args, **kwargs)
                return res
~~            except IntegrityError:
                pass
            slugs = set(
                type(self)
                ._default_manager.filter(slug__startswith=self.slug)
                .values_list("slug", flat=True)
            )
            i = 1
            while True:
                slug = self.slugify(self.name, i)
                if slug not in slugs:
                    self.slug = slug
                    return super().save(*args, **kwargs)
                i += 1
        else:
            return super().save(*args, **kwargs)

    def slugify(self, tag, i=None):
        slug = slugify(unidecode(tag))
        if i is not None:
            slug += "_%d" % i
        return slug


class Tag(TagBase):


## ... source file continues with no further IntegrityError examples...

```

