title: django.utils translation Example Code
category: page
slug: django-utils-translation-examples
sortorder: 500011422
toc: False
sidebartitle: django.utils translation
meta: Python example code for the translation callable from the django.utils module of the Django project.


translation is a callable within the django.utils module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / admin / placeholderadmin.py**](https://github.com/divio/django-cms/blob/develop/cms/admin/placeholderadmin.py)

```python
# placeholderadmin.py
import uuid
import warnings

from django.conf.urls import url
from django.contrib.admin.helpers import AdminForm
from django.contrib.admin.utils import get_deleted_objects
from django.core.exceptions import PermissionDenied
from django.db import router, transaction
from django.http import (
    HttpResponse,
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_text
~~from django.utils import translation
from django.utils.translation import ugettext as _
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.decorators.http import require_POST

from six.moves.urllib.parse import parse_qsl, urlparse

from six import get_unbound_function, get_method_function

from cms import operations
from cms.admin.forms import PluginAddValidationForm
from cms.constants import SLUG_REGEXP
from cms.exceptions import PluginLimitReached
from cms.models.placeholdermodel import Placeholder
from cms.models.placeholderpluginmodel import PlaceholderReference
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from cms.signals import pre_placeholder_operation, post_placeholder_operation
from cms.toolbar.utils import get_plugin_tree_as_json
from cms.utils import copy_plugins, get_current_site
from cms.utils.compat import DJANGO_2_0
from cms.utils.conf import get_cms_setting
from cms.utils.i18n import get_language_code, get_language_list
from cms.utils.plugins import has_reached_plugin_limit, reorder_plugins
from cms.utils.urlutils import admin_reverse


## ... source file abbreviated to get to translation examples ...


            'has_add_permission': False,
            'window_close_timeout': 10,
        }
        if cancel_clicked:
            context.update({
                'cancel': True,
            })
            return render(request, 'admin/cms/page/plugin/confirm_form.html', context)
        if not cancel_clicked and request.method == 'POST' and saved_successfully:
            return render(request, 'admin/cms/page/plugin/confirm_form.html', context)
        return render(request, 'admin/cms/page/plugin/change_form.html', context)


class PlaceholderAdminMixin(object):

    def _get_attached_admin(self, placeholder):
        return placeholder._get_attached_admin(admin_site=self.admin_site)

    def _get_operation_language(self, request):
        site = get_current_site()
        parsed_url = urlparse(request.GET['cms_path'])
        queries = dict(parse_qsl(parsed_url.query))
        language = queries.get('language')

        if not language:
~~            language = translation.get_language_from_path(parsed_url.path)
        return get_language_code(language, site_id=site.pk)

    def _get_operation_origin(self, request):
        return urlparse(request.GET['cms_path']).path

    def _send_pre_placeholder_operation(self, request, operation, **kwargs):
        token = str(uuid.uuid4())

        if not request.GET.get('cms_path'):
            warnings.warn('All custom placeholder admin endpoints require '
                          'a "cms_path" GET query which points to the path '
                          'where the request originates from.'
                          'This backwards compatible shim will be removed on 3.5 '
                          'and an HttpBadRequest response will be returned instead.',
                          UserWarning)
            return token

        pre_placeholder_operation.send(
            sender=self.__class__,
            operation=operation,
            request=request,
            language=self._get_operation_language(request),
            token=token,
            origin=self._get_operation_origin(request),


## ... source file continues with no further translation examples...

```


## Example 2 from django-floppyforms
[django-floppyforms](https://github.com/jazzband/django-floppyforms)
([project documentation](https://django-floppyforms.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-floppyforms/))
is a [Django](/django.html) code library for better control
over rendering HTML forms in your [templates](/template-engines.html).

The django-floppyforms code is provided as
[open source](https://github.com/jazzband/django-floppyforms/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-floppyforms / floppyforms / gis / widgets.py**](https://github.com/jazzband/django-floppyforms/blob/master/floppyforms/gis/widgets.py)

```python
# widgets.py
from django.conf import settings
from django.template.defaultfilters import safe
~~from django.utils import translation

import floppyforms as forms

from urllib.parse import urlencode

try:
    from django.contrib.gis import gdal, geos
except ImportError:


__all__ = ('GeometryWidget', 'GeometryCollectionWidget',
           'PointWidget', 'MultiPointWidget',
           'LineStringWidget', 'MultiLineStringWidget',
           'PolygonWidget', 'MultiPolygonWidget',
           'BaseGeometryWidget', 'BaseMetacartaWidget',
           'BaseOsmWidget', 'BaseGMapWidget')


class BaseGeometryWidget(forms.Textarea):
    display_wkt = False
    map_width = 600
    map_height = 400
    map_srid = 4326
    template_name = 'floppyforms/gis/openlayers.html'


## ... source file abbreviated to get to translation examples ...



        if value and value.geom_type.upper() != self.geom_type and self.geom_type != 'GEOMETRY':
            value = None

        wkt = ''
        if value:
            srid = self.map_srid
            if value.srid != srid:
                try:
                    ogr = value.ogr
                    ogr.transform(srid)
                    wkt = ogr.wkt
                except gdal.GDALException:
                    pass  # wkt left as an empty string
            else:
                wkt = value.wkt
        context = super(BaseGeometryWidget, self).get_context(name, wkt, attrs)
        context['module'] = 'map_%s' % name.replace('-', '_')
        context['name'] = name


        if hasattr(settings, 'ADMIN_MEDIA_PREFIX'):
            context['ADMIN_MEDIA_PREFIX'] = settings.ADMIN_MEDIA_PREFIX
        else:
            context['ADMIN_MEDIA_PREFIX'] = settings.STATIC_URL + 'admin/'
~~        context['LANGUAGE_BIDI'] = translation.get_language_bidi()
        return context


class GeometryWidget(BaseGeometryWidget):
    pass


class GeometryCollectionWidget(GeometryWidget):
    is_collection = True
    geom_type = 'GEOMETRYCOLLECTION'


class PointWidget(BaseGeometryWidget):
    is_point = True
    geom_type = 'POINT'


class MultiPointWidget(PointWidget):
    is_collection = True
    geom_type = 'MULTIPOINT'


class LineStringWidget(BaseGeometryWidget):
    is_linestring = True


## ... source file continues with no further translation examples...

```


## Example 3 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / utils.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/./utils.py)

```python
# utils.py
import datetime
import json
from django.template import Context
~~from django.utils import translation
from jet import settings
from jet.models import PinnedApplication

try:
    from django.apps.registry import apps
except ImportError:
    try:
        from django.apps import apps # Fix Django 1.7 import issue
    except ImportError:
        pass
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
try:
    from django.core.urlresolvers import reverse, resolve, NoReverseMatch
except ImportError: # Django 1.11
    from django.urls import reverse, resolve, NoReverseMatch

from django.contrib.admin import AdminSite
from django.utils.encoding import smart_text
from django.utils.text import capfirst
from django.contrib import messages
from django.utils.encoding import force_text
from django.utils.functional import Promise
from django.contrib.admin.options import IncorrectLookupParameters


## ... source file abbreviated to get to translation examples ...



    ChangeList = model_admin.get_changelist(request)

    change_list_args = [
        request, model, list_display, list_display_links, list_filter,
        model_admin.date_hierarchy, search_fields, list_select_related,
        model_admin.list_per_page, model_admin.list_max_show_all,
        model_admin.list_editable, model_admin]

    try:
        sortable_by = model_admin.get_sortable_by(request)
        change_list_args.append(sortable_by)
    except AttributeError:
        pass

    try:
        cl = ChangeList(*change_list_args)
        queryset = cl.get_queryset(request)
    except IncorrectLookupParameters:
        pass

    return queryset


def get_possible_language_codes():
~~    language_code = translation.get_language()

    language_code = language_code.replace('_', '-').lower()
    language_codes = []

    split = language_code.split('-', 2)
    if len(split) == 2:
        language_code = '%s-%s' % (split[0].lower(), split[1].upper()) if split[0] != split[1] else split[0]

    language_codes.append(language_code)

    if len(split) == 2:
        language_codes.append(split[0].lower())

    return language_codes


def get_original_menu_items(context):
    if context.get('user') and user_is_authenticated(context['user']):
        pinned_apps = PinnedApplication.objects.filter(user=context['user'].pk).values_list('app_label', flat=True)
    else:
        pinned_apps = []

    original_app_list = get_app_list(context)



## ... source file continues with no further translation examples...

```


## Example 4 from django-wiki
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

[**django-wiki / src/wiki / models / article.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/models/article.py)

```python
# article.py
from django.conf import settings as django_settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from django.db import models
from django.db.models.fields import GenericIPAddressField as IPAddressField
from django.db.models.signals import post_save
from django.db.models.signals import pre_delete
from django.db.models.signals import pre_save
from django.urls import reverse
~~from django.utils import translation
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel
from wiki import managers
from wiki.conf import settings
from wiki.core import permissions
from wiki.core.markdown import article_markdown
from wiki.decorators import disable_signal_for_loaddata

__all__ = [
    "Article",
    "ArticleForObject",
    "ArticleRevision",
    "BaseRevisionMixin",
]


class Article(models.Model):

    objects = managers.ArticleManager()

    current_revision = models.OneToOneField(
        "ArticleRevision",
        verbose_name=_("current revision"),


## ... source file abbreviated to get to translation examples ...


            return self.current_revision.title
        obj_name = _("Article without content (%(id)d)") % {"id": self.id}
        return str(obj_name)

    class Meta:
        permissions = (
            ("moderate", _("Can edit all articles and lock/unlock/restore")),
            ("assign", _("Can change ownership of any article")),
            ("grant", _("Can assign permissions to other users")),
        )

    def render(self, preview_content=None, user=None):
        if not self.current_revision:
            return ""
        if preview_content:
            content = preview_content
        else:
            content = self.current_revision.content
        return mark_safe(
            article_markdown(
                content, self, preview=preview_content is not None, user=user
            )
        )

    def get_cache_key(self):
~~        lang = translation.get_language()

        return "wiki:article:{id}:{lang}".format(
            id=self.current_revision.id if self.current_revision else self.id, lang=lang
        )

    def get_cache_content_key(self, user=None):
        return "{key}:{user}".format(
            key=self.get_cache_key(), user=user.get_username() if user else ""
        )

    def get_cached_content(self, user=None):

        cache_key = self.get_cache_key()
        cache_content_key = self.get_cache_content_key(user)

        cached_items = cache.get(cache_key, list())

        if cache_content_key in cached_items:
            cached_content = cache.get(cache_content_key)
            if cached_content is not None:
                return mark_safe(cached_content)

        cached_content = self.render(user=user)
        cached_items.append(cache_content_key)


## ... source file continues with no further translation examples...

```


## Example 5 from register
[register](https://github.com/ORGAN-IZE/register) is a [Django](/django.html),
[Bootstrap](/bootstrap-css.html), [PostgreSQL](/postgresql.html) project that is
open source under the
[GNU General Public License v3.0](https://github.com/ORGAN-IZE/register/blob/master/LICENSE).
This web application makes it easier for people to register as organ donors.
You can see the application live at
[https://register.organize.org/](https://register.organize.org/).

[**register / registration / middleware.py**](https://github.com/ORGAN-IZE/register/blob/master/registration/./middleware.py)

```python
# middleware.py
import django.middleware.locale
import django.shortcuts
~~from django.utils import translation
from django.utils.deprecation import MiddlewareMixin


class RequestLocaleMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.method == 'GET':
            language = request.GET.get('lang')
            if language:
~~                translation.activate(language)
~~                request.session[translation.LANGUAGE_SESSION_KEY] = translation.get_language()
                query = request.GET.copy()
                del query['lang']
                path = '?'.join([request.path, query.urlencode()])
                return django.shortcuts.redirect(path)



## ... source file continues with no further translation examples...

```

