title: django.template.defaultfilters truncatechars Example Code
category: page
slug: django-template-defaultfilters-truncatechars-examples
sortorder: 500011389
toc: False
sidebartitle: django.template.defaultfilters truncatechars
meta: Python example code that shows how to use the truncatechars callable from the django.template.defaultfilters module of the Django project.


`truncatechars` is a callable within the `django.template.defaultfilters` module of the Django project.

<a href="/django-template-defaultfilters-escape-examples.html">escape</a>,
<a href="/django-template-defaultfilters-filesizeformat-examples.html">filesizeformat</a>,
<a href="/django-template-defaultfilters-safe-examples.html">safe</a>,
<a href="/django-template-defaultfilters-slugify-examples.html">slugify</a>,
<a href="/django-template-defaultfilters-striptags-examples.html">striptags</a>,
and <a href="/django-template-defaultfilters-title-examples.html">title</a>
are several other callables with code examples from the same `django.template.defaultfilters` package.

## Example 1 from django-appmail
[Django-Appmail](https://github.com/yunojuno/django-appmail)
([PyPI package information](https://pypi.org/project/django-appmail/))
is a [Django](/django.html) app for handling transactional email templates.
While the project began development as a way to work with the Mandrill
transactional [API](/application-programming-interfaces.html), it is
not exclusive to that API. The project simply provides a way to store
and render email content. The library does not send or receive emails.

Django-Appmail is open sourced under the
[MIT license](https://github.com/yunojuno/django-appmail/blob/master/LICENSE).

[**django-appmail / appmail / admin.py**](https://github.com/yunojuno/django-appmail/blob/master/appmail/./admin.py)

```python
# admin.py
from __future__ import annotations

import json
from typing import Optional, Tuple

from django.contrib import admin, messages
from django.core.exceptions import ValidationError
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponseRedirect
~~from django.template.defaultfilters import truncatechars
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _lazy

from .compat import JSONField
from .forms import JSONWidget
from .models import EmailTemplate, LoggedMessage


class ValidTemplateListFilter(admin.SimpleListFilter):

    title = _lazy("Is valid")
    parameter_name = "valid"

    def lookups(
        self, request: HttpRequest, model_admin: admin.ModelAdmin
    ) -> Tuple[Tuple[str, str], Tuple[str, str]]:
        return (("1", _lazy("True")), ("0", _lazy("False")))

    def queryset(self, request: HttpRequest, queryset: QuerySet) -> QuerySet:
        valid_ids = []
        invalid_ids = []
        for obj in queryset:


## ... source file abbreviated to get to truncatechars examples ...



    exclude = ("html", "context")

    formfield_overrides = {JSONField: {"widget": JSONWidget}}

    list_display = ("to", "template_name", "_subject", "timestamp")

    list_filter = ("timestamp", "template__name", "template__language")

    raw_id_fields = ("user", "template")

    readonly_fields = (
        "to",
        "user",
        "template",
        "template_context",
        "subject",
        "body",
        "render_html",
        "timestamp",
    )

    search_fields = ("to", "subject")

    def _subject(self, obj: LoggedMessage) -> str:
~~        return truncatechars(obj.subject, 50)

    def template_name(self, obj: LoggedMessage) -> str:
        return obj.template.name

    def template_context(self, obj: LoggedMessage) -> str:
        return self.pretty_print(obj.context)

    def render_html(self, obj: LoggedMessage) -> str:
        if obj.id is None:
            url = ""
        else:
            url = reverse(
                "appmail:render_message_body_html", kwargs={"email_id": obj.id}
            )
        return self.iframe(url)

    render_html.short_description = "HTML (rendered)"  # type: ignore
    render_html.allow_tags = True  # type: ignore



## ... source file continues with no further truncatechars examples...

```


## Example 2 from elasticsearch-django
[elasticsearch-django](https://github.com/yunojuno/elasticsearch-django)
([PyPI package information](https://pypi.org/project/elasticsearch-django/))
is a [Django](/django.html) app for managing
[ElasticSearch](https://github.com/elastic/elasticsearch) indexes
populated by [Django ORM](/django-orm.html) models. The project is
available as open source under the
[MIT license](https://github.com/yunojuno/elasticsearch-django/blob/master/LICENSE).

[**elasticsearch-django / elasticsearch_django / admin.py**](https://github.com/yunojuno/elasticsearch-django/blob/master/elasticsearch_django/./admin.py)

```python
# admin.py
import logging

import simplejson as json  # simplejson supports Decimal serialization
from django.contrib import admin
~~from django.template.defaultfilters import truncatechars, truncatewords
from django.utils.safestring import mark_safe

from .models import SearchQuery

logger = logging.getLogger(__name__)


def pprint(data: dict) -> str:
    pretty = json.dumps(data, sort_keys=True, indent=4, separators=(",", ": "))
    html = pretty.replace(" ", "&nbsp;").replace("\n", "<br>")
    return mark_safe("<code>%s</code>" % html)


class SearchQueryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "search_terms_display",
        "total_hits_display",
        "returned_",
        "min_",
        "max_",
        "reference",
        "executed_at",
    )
    list_filter = ("index", "query_type")
    search_fields = ("search_terms", "user__first_name", "user__last_name", "reference")
    exclude = ("hits", "aggregations", "query", "page", "total_hits_")
    readonly_fields = (
        "user",
        "index",
        "search_terms",
        "query_type",
        "total_hits",
        "total_hits_relation",
        "returned_",
        "min_",
        "max_",
        "duration",
        "query_",
        "hits_",
        "aggregations_",
        "executed_at",
    )

    def search_terms_display(self, instance: SearchQuery) -> str:
        raw = instance.search_terms
~~        return truncatechars(truncatewords(raw, 5), 50)

    def query_(self, instance: SearchQuery) -> str:
        return pprint(instance.query)

    def max_(self, instance: SearchQuery) -> str:
        return "-" if instance.page_size == 0 else str(instance.max_score)

    max_.short_description = "Max score"  # type: ignore

    def min_(self, instance: SearchQuery) -> str:
        return "-" if instance.page_size == 0 else str(instance.min_score)

    min_.short_description = "Min score"  # type: ignore

    def total_hits_display(self, instance: SearchQuery) -> str:
        if instance.total_hits_relation == SearchQuery.TotalHitsRelation.ESTIMATE:
            return f"{instance.total_hits}*"
        return f"{instance.total_hits}"

    def returned_(self, instance: SearchQuery) -> str:
        if instance.page_size == 0:
            return "-"
        return "%i - %i" % (instance.page_from, instance.page_to)



## ... source file continues with no further truncatechars examples...

```

