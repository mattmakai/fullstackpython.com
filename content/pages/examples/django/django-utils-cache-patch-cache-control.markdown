title: django.utils.cache patch_cache_control Example Code
category: page
slug: django-utils-cache-patch-cache-control-examples
sortorder: 500011426
toc: False
sidebartitle: django.utils.cache patch_cache_control
meta: Python example code for the patch_cache_control callable from the django.utils.cache module of the Django project.


patch_cache_control is a callable within the django.utils.cache module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / views.py**](https://github.com/divio/django-cms/blob/develop/cms/./views.py)

```python
# views.py

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
~~from django.utils.cache import patch_cache_control
from django.utils.http import is_safe_url, urlquote
from django.utils.timezone import now
from django.utils.translation import get_language_from_request
from django.views.decorators.http import require_POST

from cms.cache.page import get_page_cache
from cms.exceptions import LanguageError
from cms.forms.login import CMSToolbarLoginForm
from cms.models.pagemodel import TreeNode
from cms.page_rendering import _handle_no_page, render_page, render_object_structure, _render_welcome_page
from cms.toolbar.utils import get_toolbar_from_request
from cms.utils import get_current_site
from cms.utils.conf import get_cms_setting
from cms.utils.i18n import (get_fallback_languages, get_public_languages,
                            get_redirect_on_fallback, get_language_list,
                            get_default_language_for_site,
                            is_language_prefix_patterns_used)
from cms.utils.page import get_page_from_request
from cms.utils.page_permissions import user_can_change_page


def _clean_redirect_url(redirect_url, language):
    if (redirect_url and is_language_prefix_patterns_used() and redirect_url[0] == "/"
            and not redirect_url.startswith('/%s/' % language)):
        redirect_url = "/%s/%s" % (language, redirect_url.lstrip("/"))
    return redirect_url


def details(request, slug):
    response_timestamp = now()
    if get_cms_setting("PAGE_CACHE") and (
        not hasattr(request, 'toolbar') or (
            not request.toolbar.edit_mode_active and
            not request.toolbar.show_toolbar and
            not request.user.is_authenticated
        )
    ):
        cache_content = get_page_cache(request)
        if cache_content is not None:
            content, headers, expires_datetime = cache_content
            response = HttpResponse(content)
            response.xframe_options_exempt = True
            response._headers = headers
            max_age = int(
                (expires_datetime - response_timestamp).total_seconds() + 0.5)
~~            patch_cache_control(response, max_age=max_age)
            return response

    site = get_current_site()
    page = get_page_from_request(request, use_path=slug)
    toolbar = get_toolbar_from_request(request)
    tree_nodes = TreeNode.objects.get_for_site(site)

    if not page and not slug and not tree_nodes.exists():
        return _render_welcome_page(request)

    if not page:
        _handle_no_page(request)

    request.current_page = page

    if hasattr(request, 'user') and request.user.is_staff:
        user_languages = get_language_list(site_id=site.pk)
    else:
        user_languages = get_public_languages(site_id=site.pk)

    request_language = get_language_from_request(request, check_path=True)

    if not page.is_home and request_language not in user_languages:
        return _handle_no_page(request)


## ... source file continues with no further patch_cache_control examples...

```


## Example 2 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/models.py)

```python
# models.py
import json
import logging
from collections import defaultdict
from io import StringIO
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core import checks
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.handlers.base import BaseHandler
from django.core.handlers.wsgi import WSGIRequest
from django.db import models, transaction
from django.db.models import Case, Q, Value, When
from django.db.models.functions import Concat, Lower, Substr
from django.http import Http404
from django.http.request import split_domain_port
from django.template.response import TemplateResponse
from django.urls import NoReverseMatch, reverse
from django.utils import timezone
~~from django.utils.cache import patch_cache_control
from django.utils.functional import cached_property
from django.utils.text import capfirst, slugify
from django.utils.translation import gettext_lazy as _
from modelcluster.models import (
    ClusterableModel, get_all_child_m2m_relations, get_all_child_relations)
from treebeard.mp_tree import MP_Node

from wagtail.core.query import PageQuerySet, TreeQuerySet
from wagtail.core.signals import page_published, page_unpublished, post_page_move, pre_page_move
from wagtail.core.sites import get_site_for_hostname
from wagtail.core.url_routing import RouteResult
from wagtail.core.utils import WAGTAIL_APPEND_SLASH, camelcase_to_underscore, resolve_model_string
from wagtail.search import index


logger = logging.getLogger('wagtail.core')

PAGE_TEMPLATE_VAR = 'page'


class SiteManager(models.Manager):
    def get_queryset(self):
        return super(SiteManager, self).get_queryset().order_by(Lower("hostname"))



## ... source file abbreviated to get to patch_cache_control examples ...



    def _get_dummy_header_url(self, original_request=None):
        return self.full_url

    DEFAULT_PREVIEW_MODES = [('', _('Default'))]

    @property
    def preview_modes(self):
        return Page.DEFAULT_PREVIEW_MODES

    @property
    def default_preview_mode(self):
        return self.preview_modes[0][0]

    def is_previewable(self):
        page = self
        if page.specific_class.preview_modes != type(page).preview_modes:
            page = page.specific

        return bool(page.preview_modes)

    def serve_preview(self, request, mode_name):
        request.is_preview = True

        response = self.serve(request)
~~        patch_cache_control(response, private=True)
        return response

    def get_cached_paths(self):
        return ['/']

    def get_sitemap_urls(self, request=None):
        return [
            {
                'location': self.get_full_url(request),
                'lastmod': (self.last_published_at or self.latest_revision_created_at),
            }
        ]

    def get_static_site_paths(self):
        yield '/'

        for child in self.get_children().live():
            for path in child.specific.get_static_site_paths():
                yield '/' + child.slug + path

    def get_ancestors(self, inclusive=False):
        return Page.objects.ancestor_of(self, inclusive)

    def get_descendants(self, inclusive=False):


## ... source file continues with no further patch_cache_control examples...

```

