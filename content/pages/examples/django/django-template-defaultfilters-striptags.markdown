title: django.template.defaultfilters striptags Example Code
category: page
slug: django-template-defaultfilters-striptags-examples
sortorder: 500011387
toc: False
sidebartitle: django.template.defaultfilters striptags
meta: Python example code that shows how to use the striptags callable from the django.template.defaultfilters module of the Django project.


`striptags` is a callable within the `django.template.defaultfilters` module of the Django project.

<a href="/django-template-defaultfilters-escape-examples.html">escape</a>,
<a href="/django-template-defaultfilters-filesizeformat-examples.html">filesizeformat</a>,
<a href="/django-template-defaultfilters-safe-examples.html">safe</a>,
<a href="/django-template-defaultfilters-slugify-examples.html">slugify</a>,
<a href="/django-template-defaultfilters-title-examples.html">title</a>,
and <a href="/django-template-defaultfilters-truncatechars-examples.html">truncatechars</a>
are several other callables with code examples from the same `django.template.defaultfilters` package.

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
from urllib.parse import quote as urlquote

from django import template
from django.apps import apps
from django.conf import settings as django_settings
from django.contrib.contenttypes.models import ContentType
from django.db.models import Model
from django.forms import BaseForm
~~from django.template.defaultfilters import striptags
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
        try:
            article = models.ArticleForObject.objects.get(


## ... source file abbreviated to get to striptags examples ...


@register.inclusion_tag("wiki/includes/form.html", takes_context=True)
def wiki_form(context, form_obj):
    if not isinstance(form_obj, BaseForm):
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

~~        content = striptags(content)
        words = content.split()

        return words

    max_words = int(max_words)

    match_position = content.lower().find(keyword.lower())

    if match_position != -1:
        try:
            match_start = content.rindex(" ", 0, match_position) + 1
        except ValueError:
            match_start = 0
        try:
            match_end = content.index(" ", match_position + len(keyword))
        except ValueError:
            match_end = len(content)
        all_before = clean_text(content[:match_start])
        match = content[match_start:match_end]
        all_after = clean_text(content[match_end:])
        before_words = all_before[-max_words // 2 :]
        after_words = all_after[: max_words - len(before_words)]
        before = " ".join(before_words)
        after = " ".join(after_words)
~~        html = ("%s %s %s" % (before, striptags(match), after)).strip()
        kw_p = re.compile(r"(\S*%s\S*)" % keyword, re.IGNORECASE)
        html = kw_p.sub(r"<strong>\1</strong>", html)

        return mark_safe(html)

    return " ".join(clean_text(content)[:max_words])


@register.filter
def can_read(obj, user):
    return obj.can_read(user)


@register.filter
def can_write(obj, user):
    return obj.can_write(user)


@register.filter
def can_delete(obj, user):
    return obj.can_delete(user)


@register.filter


## ... source file continues with no further striptags examples...

```

