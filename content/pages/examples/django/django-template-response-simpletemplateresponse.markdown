title: django.template.response SimpleTemplateResponse Example Code
category: page
slug: django-template-response-simpletemplateresponse-examples
sortorder: 500013500
toc: False
sidebartitle: django.template.response SimpleTemplateResponse
meta: Python open source example code for the SimpleTemplateResponse class in Django within django.template.response.


[SimpleTemplateResponse](https://docs.djangoproject.com/en/stable/ref/template-response/#simpletemplateresponse-objects)
([source code](https://github.com/django/django/blob/master/django/template/response.py))
is a class provided by [Django](/django.html) that retains context for the
HTTP request that originated the call to a view. SimpleTemplateResponse 
is a superclass for the similar
[TemplateResponse](/django-template-response-templateresponse-examples.html) 
class. It is useful for modifying a response before it is rendered, which 
cannot be done with a traditional static 
[HttpResponse](/django-http-httpresponse-examples.html) object.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / admin / pageadmin.py**](https://github.com/divio/django-cms/blob/develop/cms/admin/pageadmin.py)

```python
# -*- coding: utf-8 -*-
from collections import namedtuple
import copy
import json
import sys
import uuid


import django
from django.contrib.admin.helpers import AdminForm
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin, messages
from django.contrib.admin.models import LogEntry, CHANGE
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import get_deleted_objects
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.exceptions import (ObjectDoesNotExist,
                                    PermissionDenied, ValidationError)
from django.db import router, transaction
from django.db.models import Q, Prefetch
from django.http import (
    HttpResponseRedirect,
    HttpResponse,
    Http404,
    HttpResponseBadRequest,
    HttpResponseForbidden,
)
from django.shortcuts import render, get_object_or_404
from django.template.defaultfilters import escape
from django.template.loader import get_template
~~from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.utils.encoding import force_text
from django.utils.translation import ugettext, ugettext_lazy as _, get_language
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.http import QueryDict


## ... source code abbreviated to get to SimpleTemplateResponse example ...


    def changelist_view(self, request, extra_context=None):
        from django.contrib.admin.views.main import ERROR_FLAG

        if not self.has_change_permission(request, obj=None):
            raise PermissionDenied

        if request.method == 'POST' and 'site' in request.POST:
            site_id = request.POST['site']

            if site_id.isdigit() and Site.objects.filter(pk=site_id).exists():
                request.session['cms_admin_site'] = site_id

        site = self.get_site(request)
        # Language may be present in the GET dictionary but empty
        language = request.GET.get('language', get_language())

        if not language:
            language = get_language()

        query = request.GET.get('q', '')
        pages = self.get_queryset(request)
        pages, use_distinct = self.get_search_results(request, pages, query)

        changelist_form = self.changelist_form(request.GET)

        try:
            changelist_form.full_clean()
            pages = changelist_form.run_filters(pages)
        except (ValueError, ValidationError):
            # Wacky lookup parameters were given, so redirect to the main
            # changelist page, without parameters, and pass an 'invalid=1'
            # parameter via the query string. If wacky parameters were given
            # and the 'invalid=1' parameter was already in the query string,
            # something is screwed up with the database, so display an error
            # page.
~~            if ERROR_FLAG in request.GET.keys():
~~                return SimpleTemplateResponse('admin/invalid_setup.html', {
~~                    'title': _('Database error'),
~~                })
            return HttpResponseRedirect(request.path + '?' + ERROR_FLAG + '=1')

        if changelist_form.is_filtered():
            pages = pages.prefetch_related(
                Prefetch(
                    'title_set',
                    to_attr='filtered_translations',
                    queryset=Title.objects.filter(language__in=get_language_list(site.pk))
                ),
            )
            pages = pages.distinct() if use_distinct else pages
            # Evaluates the queryset
            has_items = len(pages) >= 1
        else:
            has_items = pages.exists()

        context = self.admin_site.each_context(request)
        context.update({
            'opts': self.model._meta,
            'media': self.media,
            'CMS_MEDIA_URL': get_cms_setting('MEDIA_URL'),
            'CMS_PERMISSION': get_cms_setting('PERMISSION'),
            'site_languages': get_language_list(site.pk),
            'preview_language': language,
            'changelist_form': changelist_form,
            'cms_current_site': site,
            'has_add_permission': self.has_add_permission(request),
            'module_name': force_text(self.model._meta.verbose_name_plural),
            'admin': self,
            'tree': {
                'site': site,
                'sites': self.get_sites_for_user(request.user),
                'query': query,
                'is_filtered': changelist_form.is_filtered(),
                'items': pages,
                'has_items': has_items,
            },
        })
        context.update(extra_context or {})
        request.current_app = self.admin_site.name
        return TemplateResponse(request, self.change_list_template, context)


## ... source code continues with no further examples ...
```


## Example 2 from django-debug-toolbar
[django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar)
([project documentation](https://github.com/jazzband/django-debug-toolbar)
and [PyPI page](https://pypi.org/project/django-debug-toolbar/))
grants a developer detailed request-response cycle information while
developing a [Django](/django.html) web application.
The code for django-debug-toolbar is
[open source](https://github.com/jazzband/django-debug-toolbar/blob/master/LICENSE)
and maintained by the developer community group known as
[Jazzband](https://jazzband.co/).

[**django-debug-toolbar / debug_toolbar / panels / redirects.py**](https://github.com/jazzband/django-debug-toolbar/blob/master/debug_toolbar/panels/redirects.py)

```python
~~from django.template.response import SimpleTemplateResponse
from django.utils.translation import gettext_lazy as _

from debug_toolbar.panels import Panel


class RedirectsPanel(Panel):
    """
    Panel that intercepts redirects and displays a page with debug info.
    """

    has_content = False

    nav_title = _("Intercept redirects")

    def process_request(self, request):
        response = super().process_request(request)
        if 300 <= int(response.status_code) < 400:
            redirect_to = response.get("Location", None)
            if redirect_to:
                status_line = "{} {}".format(
                    response.status_code, response.reason_phrase
                )
                cookies = response.cookies
~~                context = {"redirect_to": redirect_to, "status_line": status_line}
~~                # Using SimpleTemplateResponse avoids running global context processors.
~~                response = SimpleTemplateResponse(
~~                    "debug_toolbar/redirect.html", context
~~                )
~~                response.cookies = cookies
~~                response.render()
~~        return response

```


