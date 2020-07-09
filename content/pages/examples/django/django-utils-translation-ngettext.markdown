title: django.utils.translation ngettext Example Code
category: page
slug: django-utils-translation-ngettext-examples
sortorder: 500011505
toc: False
sidebartitle: django.utils.translation ngettext
meta: Python example code for the ngettext callable from the django.utils.translation module of the Django project.


ngettext is a callable within the django.utils.translation module of the Django project.


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

[**django-wiki / src/wiki / views / article.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/views/article.py)

```python
# article.py
import difflib
import logging
from urllib.parse import urljoin

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
~~from django.utils.translation import ngettext
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.generic import DetailView
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import RedirectView
from django.views.generic import TemplateView
from django.views.generic import View
from wiki import editors
from wiki import forms
from wiki import models
from wiki.conf import settings
from wiki.core import permissions
from wiki.core.diff import simple_merge
from wiki.core.exceptions import NoRootURL
from wiki.core.paginator import WikiPaginator
from wiki.core.plugins import registry as plugin_registry
from wiki.core.utils import object_to_json_response
from wiki.decorators import get_article
from wiki.views.mixins import ArticleMixin

log = logging.getLogger(__name__)


class ArticleView(ArticleMixin, TemplateView):


## ... source file abbreviated to get to ngettext examples ...



            for descendant in descendants:
                descendant.refresh_from_db()
                dst_path = descendant.path
                src_path = urljoin(old_path, dst_path[root_len:])
                src_len = len(src_path)
                pos = src_path.rfind("/", 0, src_len - 1)
                slug = src_path[pos + 1 : src_len - 1]
                parent_urlpath = models.URLPath.get_by_path(src_path[0 : max(pos, 0)])

                link = "[wiki:/{path}](wiki:/{path})".format(path=dst_path)
                urlpath_new = models.URLPath._create_urlpath_from_request(
                    self.request,
                    self.article,
                    parent_urlpath,
                    slug,
                    _("Moved: {title}").format(title=descendant.article),
                    _("Article moved to {link}").format(link=link),
                    _("Created redirect (auto)"),
                )
                urlpath_new.moved_to = descendant
                urlpath_new.save()

            messages.success(
                self.request,
~~                ngettext(
                    "Article successfully moved! Created {n} redirect.",
                    "Article successfully moved! Created {n} redirects.",
                    len(descendants),
                ).format(n=len(descendants)),
            )

        else:
            messages.success(self.request, _("Article successfully moved!"))
        return redirect("wiki:get", path=self.urlpath.path)


class Deleted(Delete):


    template_name = "wiki/deleted.html"
    form_class = forms.DeleteForm

    @method_decorator(get_article(can_read=True, deleted_contents=True))
    def dispatch(self, request, article, *args, **kwargs):

        self.urlpath = kwargs.get("urlpath", None)
        self.article = article

        if self.urlpath:


## ... source file continues with no further ngettext examples...

```


## Example 2 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / images / wagtail_hooks.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/images/wagtail_hooks.py)

```python
# wagtail_hooks.py
from django.conf.urls import include, url
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
~~from django.utils.translation import gettext, ngettext

import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.menu import MenuItem
from wagtail.admin.navigation import get_site_for_user
from wagtail.admin.rich_text import HalloPlugin
from wagtail.admin.search import SearchArea
from wagtail.admin.site_summary import SummaryItem
from wagtail.core import hooks
from wagtail.images import admin_urls, get_image_model, image_operations
from wagtail.images.api.admin.views import ImagesAdminAPIViewSet
from wagtail.images.forms import GroupImagePermissionFormSet
from wagtail.images.permissions import permission_policy
from wagtail.images.rich_text import ImageEmbedHandler
from wagtail.images.rich_text.contentstate import ContentstateImageConversionRule
from wagtail.images.rich_text.editor_html import EditorHTMLImageConversionRule


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        url(r'^images/', include(admin_urls, namespace='wagtailimages')),
    ]




## ... source file abbreviated to get to ngettext examples ...


            request.user, ['add', 'change', 'delete']
        )


@hooks.register('register_admin_search_area')
def register_images_search_area():
    return ImagesSearchArea(
        _('Images'), reverse('wagtailimages:index'),
        name='images',
        classnames='icon icon-image',
        order=200)


@hooks.register('register_group_permission_panel')
def register_image_permissions_panel():
    return GroupImagePermissionFormSet


@hooks.register('describe_collection_contents')
def describe_collection_docs(collection):
    images_count = get_image_model().objects.filter(collection=collection).count()
    if images_count:
        url = reverse('wagtailimages:index') + ('?collection_id=%d' % collection.id)
        return {
            'count': images_count,
~~            'count_text': ngettext(
                "%(count)s image",
                "%(count)s images",
                images_count
            ) % {'count': images_count},
            'url': url,
        }



## ... source file continues with no further ngettext examples...

```

