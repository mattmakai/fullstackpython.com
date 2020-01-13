title: django.urls.exceptions Resolver404 Django Code Examples
category: page
slug: django-urls-exceptions-resolver404-examples
sortorder: 500013641
toc: False
sidebartitle: django.urls.exceptions Resolver404
meta: Python example code for the Resolver404 exception class from Django's django.urls.exceptions module.


[Resolver404](https://docs.djangoproject.com/en/stable/ref/exceptions/#resolver404)
([source code](https://github.com/django/django/blob/master/django/urls/exceptions.py))
is a [Django](/django.html) exception that is raised when the path 
passed to the `resolve` function does not map to a view that is specified 
in your project's `views.py` file.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / page_rendering.py**](https://github.com/divio/django-cms/blob/develop/cms/page_rendering.py)

```python
# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import Http404
from django.shortcuts import render
from django.template.response import TemplateResponse
~~from django.urls import Resolver404, resolve, reverse

from cms import __version__
from cms.cache.page import set_page_cache
from cms.models import Page
from cms.utils.conf import get_cms_setting
from cms.utils.page import get_page_template_from_request
from cms.utils.page_permissions import user_can_change_page, user_can_view_page


def render_page(request, page, current_language, slug):
    """
    Renders a page
    """
    context = {}
    context['lang'] = current_language
    context['current_page'] = page
    context['has_change_permissions'] = user_can_change_page(request.user, page)
    context['has_view_permissions'] = user_can_view_page(request.user, page)

    if not context['has_view_permissions']:
        return _handle_no_page(request)

    template = get_page_template_from_request(request)
    response = TemplateResponse(request, template, context)
    response.add_post_render_callback(set_page_cache)

    # Add headers for X Frame Options - this really should be changed upon moving to class based views
    xframe_options = page.get_xframe_options()
    # xframe_options can be None if there's no xframe information on the page
    # (eg. a top-level page which has xframe options set to "inherit")
    if xframe_options == Page.X_FRAME_OPTIONS_INHERIT or xframe_options is None:
        # This is when we defer to django's own clickjacking handling
        return response

    # We want to prevent django setting this in their middlewear
    response.xframe_options_exempt = True

    if xframe_options == Page.X_FRAME_OPTIONS_ALLOW:
        # Do nothing, allowed is no header.
        return response
    elif xframe_options == Page.X_FRAME_OPTIONS_SAMEORIGIN:
        response['X-Frame-Options'] = 'SAMEORIGIN'
    elif xframe_options == Page.X_FRAME_OPTIONS_DENY:
        response['X-Frame-Options'] = 'DENY'
    return response


def render_object_structure(request, obj):
    context = {
        'object': obj,
        'cms_toolbar': request.toolbar,
    }
    return render(request, 'cms/toolbar/structure.html', context)


~~def _handle_no_page(request):
~~    try:
~~        #add a $ to the end of the url (does not match on the cms anymore)
~~        resolve('%s$' % request.path)
~~    except Resolver404 as e:
~~        # raise a django http 404 page
~~        exc = Http404(dict(path=request.path, tried=e.args[0]['tried']))
~~        raise exc
~~    raise Http404('CMS Page not found: %s' % request.path)


def _render_welcome_page(request):
    context = {
        'cms_version': __version__,
        'cms_edit_on': get_cms_setting('CMS_TOOLBAR_URL__EDIT_ON'),
        'django_debug': settings.DEBUG,
        'next_url': reverse('pages-root'),
    }
    return TemplateResponse(request, "cms/welcome.html", context)

```


## Example 2 from django-wiki
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

[**django-wiki / src/ wiki / forms.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/forms.py)

```python

__all__ = [
    'UserCreationForm',
    'UserUpdateForm',
    'WikiSlugField',
    'SpamProtectionMixin',
    'CreateRootForm',
    'MoveForm',
    'EditForm',
    'SelectWidgetBootstrap',
    'TextInputPrepend',
    'CreateForm',
    'DeleteForm',
    'PermissionsForm',
    'DirFilterForm',
    'SearchForm',
]

from datetime import timedelta

from django import forms
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core import validators
from django.core.validators import RegexValidator
from django.forms.widgets import HiddenInput
from django.shortcuts import get_object_or_404
~~from django.urls import Resolver404, resolve
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.translation import gettext, gettext_lazy as _, pgettext_lazy
from wiki import models
from wiki.conf import settings
from wiki.core import permissions
from wiki.core.diff import simple_merge
from wiki.core.plugins.base import PluginSettingsFormMixin
from wiki.editors import getEditor

from .forms_account_handling import UserCreationForm, UserUpdateForm

validate_slug_numbers = RegexValidator(
    r'^[0-9]+$',
    _("A 'slug' cannot consist solely of numbers."),
    'invalid',
    inverse_match=True
)


class WikiSlugField(forms.CharField):
    """
    In future versions of Django, we might be able to define this field as
    the default field directly on the model. For now, it's used in CreateForm.
    """

    default_validators = [validators.validate_slug, validate_slug_numbers]

    def __init__(self, *args, **kwargs):
        self.allow_unicode = kwargs.pop('allow_unicode', False)
        if self.allow_unicode:
            self.default_validators = [
                validators.validate_unicode_slug,
                validate_slug_numbers
            ]
        super().__init__(*args, **kwargs)


def _clean_slug(slug, urlpath):
    if slug.startswith("_"):
        raise forms.ValidationError(
            gettext('A slug may not begin with an underscore.'))
    if slug == 'admin':
        raise forms.ValidationError(
            gettext("'admin' is not a permitted slug name."))

    if settings.URL_CASE_SENSITIVE:
        already_existing_slug = models.URLPath.objects.filter(
            slug=slug,
            parent=urlpath)
    else:
        slug = slug.lower()
        already_existing_slug = models.URLPath.objects.filter(
            slug__iexact=slug,
            parent=urlpath)
    if already_existing_slug:
        already_urlpath = already_existing_slug[0]
        if already_urlpath.article and already_urlpath.article.current_revision.deleted:
            raise forms.ValidationError(
                gettext('A deleted article with slug "%s" already exists.') %
                already_urlpath.slug)
        else:
            raise forms.ValidationError(
                gettext('A slug named "%s" already exists.') %
                already_urlpath.slug)

~~    if settings.CHECK_SLUG_URL_AVAILABLE:
~~        try:
~~            # Fail validation if URL resolves to non-wiki app
~~            match = resolve(urlpath.path + '/' + slug + '/')
~~            if match.app_name != 'wiki':
~~                raise forms.ValidationError(
~~                    gettext('This slug conflicts with an existing URL.'))
~~        except Resolver404:
~~            pass

    return slug



## ... source file continues with no further relevant examples ...
```
