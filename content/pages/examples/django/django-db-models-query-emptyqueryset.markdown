title: django.db.models.query EmptyQuerySet Example Code
category: page
slug: django-db-models-query-emptyqueryset-examples
sortorder: 500011239
toc: False
sidebartitle: django.db.models.query EmptyQuerySet
meta: Python example code for the EmptyQuerySet class from the django.db.models.query module of the Django project.


EmptyQuerySet is a class within the django.db.models.query module of the Django project.


## Example 1 from django-wiki
[django-wiki](https://github.com/django-wiki/django-wiki)
([project documentation](https://django-wiki.readthedocs.io/en/master/),
[demo](https://demo.django-wiki.org/),
and [PyPI page](https://pypi.org/project/django-wiki/))
is a wiki system code library for [Django](/django.html)
projects that makes it easier to create user-editable content.
The project aims to provide necessary core features and then
have an easy plugin format for additional features, rather than
having every exhaustive feature built into the core system.
django-wiki is a rewrite of an earlier now-defunct project
named [django-simplewiki](https://code.google.com/p/django-simple-wiki/).

The code for django-wiki is provided as open source under the
[GNU General Public License 3.0](https://github.com/django-wiki/django-wiki/blob/master/COPYING).

[**django-wiki / src/wiki / managers.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/./managers.py)

```python
# managers.py
from django.db import models
from django.db.models import Count
from django.db.models import Q
~~from django.db.models.query import EmptyQuerySet
from django.db.models.query import QuerySet
from mptt.managers import TreeManager


class ArticleQuerySet(QuerySet):
    def can_read(self, user):
        if user.has_perm("wiki.moderator"):
            return self
        if user.is_anonymous:
            q = self.filter(other_read=True)
        else:
            q = self.filter(
                Q(other_read=True)
                | Q(owner=user)
                | (Q(group__user=user) & Q(group_read=True))
            ).annotate(Count("id"))
        return q

    def can_write(self, user):
        if user.has_perm("wiki.moderator"):
            return self
        if user.is_anonymous:
            q = self.filter(other_write=True)
        else:
            q = self.filter(
                Q(other_write=True)
                | Q(owner=user)
                | (Q(group__user=user) & Q(group_write=True))
            )
        return q

    def active(self):
        return self.filter(current_revision__deleted=False)


~~class ArticleEmptyQuerySet(EmptyQuerySet):
    def can_read(self, user):
        return self

    def can_write(self, user):
        return self

    def active(self):
        return self


class ArticleFkQuerySetMixin:
    def can_read(self, user):
        if user.has_perm("wiki.moderate"):
            return self
        if user.is_anonymous:
            q = self.filter(article__other_read=True)
        else:
            q = self.filter(
                Q(article__other_read=True)
                | Q(article__owner=user)
                | (Q(article__group__user=user) & Q(article__group_read=True))
            ).annotate(Count("id"))
        return q



## ... source file abbreviated to get to EmptyQuerySet examples ...



    def can_read(self, user):
        return self.get_queryset().can_read(user)

    def can_write(self, user):
        return self.get_queryset().can_write(user)


class ArticleFkManager(models.Manager):
    def get_empty_query_set(self):
        return self.get_queryset().none()

    def get_queryset(self):
        return ArticleFkQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()

    def can_read(self, user):
        return self.get_queryset().can_read(user)

    def can_write(self, user):
        return self.get_queryset().can_write(user)


~~class URLPathEmptyQuerySet(EmptyQuerySet, ArticleFkEmptyQuerySetMixin):
    def select_related_common(self):
        return self

    def default_order(self):
        return self


class URLPathQuerySet(QuerySet, ArticleFkQuerySetMixin):
    def select_related_common(self):
        return self.select_related(
            "parent", "article__current_revision", "article__owner"
        )

    def default_order(self):
        return self.order_by("article__current_revision__title")


class URLPathManager(TreeManager):
    def get_empty_query_set(self):
        return self.get_queryset().none()

    def get_queryset(self):
        return URLPathQuerySet(self.model, using=self._db).order_by(
            self.tree_id_attr, self.left_attr
                Q(article__other_write=True)
                | Q(article__owner=user)
                | (Q(article__group__user=user) & Q(article__group_write=True))
            ).annotate(Count("id"))
        return q

    def active(self):
        return self.filter(article__current_revision__deleted=False)


class ArticleFkEmptyQuerySetMixin:
    def can_read(self, user):
        return self

    def can_write(self, user):
        return self

    def active(self):
        return self


class ArticleFkQuerySet(ArticleFkQuerySetMixin, QuerySet):
    pass


~~class ArticleFkEmptyQuerySet(ArticleFkEmptyQuerySetMixin, EmptyQuerySet):
    pass


class ArticleManager(models.Manager):
    def get_empty_query_set(self):
        return self.get_queryset().none()

    def get_queryset(self):
        return ArticleQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()


## ... source file continues with no further EmptyQuerySet examples...

```

