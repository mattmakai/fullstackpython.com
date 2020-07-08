title: django.forms BaseForm Example Code
category: page
slug: django-forms-baseform-examples
sortorder: 500011255
toc: False
sidebartitle: django.forms BaseForm
meta: Python example code for the BaseForm class from the django.forms module of the Django project.


BaseForm is a class within the django.forms module of the Django project.


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

[**django-wiki / src/wiki / templatetags / wiki_tags.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/templatetags/wiki_tags.py)

```python
# wiki_tags.py
import re

from django import template
from django.apps import apps
from django.conf import settings as django_settings
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model
~~from django.forms import BaseForm
from django.template.defaultfilters import striptags
from django.utils.http import urlquote
from django.utils.safestring import mark_safe
from wiki import models
from wiki.conf import settings
from wiki.core.plugins import registry as plugin_registry

register = template.Library()


_cache = {}


@register.simple_tag(takes_context=True)
def article_for_object(context, obj):
    if not isinstance(obj, Model):
        raise TypeError(
            "A Wiki article can only be associated to a Django Model "
            "instance, not %s" % type(obj)
        )

    content_type = ContentType.objects.get_for_model(obj)

    if True or obj not in _cache:


## ... source file abbreviated to get to BaseForm examples ...


@register.inclusion_tag("wiki/includes/render.html", takes_context=True)
def wiki_render(context, article, preview_content=None):

    if preview_content:
        content = article.render(preview_content=preview_content)
    elif article.current_revision:
        content = article.get_cached_content(user=context.get("user"))
    else:
        content = None

    context.update(
        {
            "article": article,
            "content": content,
            "preview": preview_content is not None,
            "plugins": plugin_registry.get_plugins(),
            "STATIC_URL": django_settings.STATIC_URL,
            "CACHE_TIMEOUT": settings.CACHE_TIMEOUT,
        }
    )
    return context


@register.inclusion_tag("wiki/includes/form.html", takes_context=True)
def wiki_form(context, form_obj):
~~    if not isinstance(form_obj, BaseForm):
        raise TypeError(
            "Error including form, it's not a form, it's a %s" % type(form_obj)
        )
    context.update({"form": form_obj})
    return context


@register.inclusion_tag("wiki/includes/messages.html", takes_context=True)
def wiki_messages(context):

    messages = context.get("messages", [])
    for message in messages:
        message.css_class = settings.MESSAGE_TAG_CSS_CLASS[message.level]
    context.update({"messages": messages})
    return context


@register.filter
def get_content_snippet(content, keyword, max_words=30):

    def clean_text(content):

        content = striptags(content)
        words = content.split()


## ... source file continues with no further BaseForm examples...

```

