title: django.urls include Example Code
category: page
slug: django-urls-include-examples
sortorder: 500011406
toc: False
sidebartitle: django.urls include
meta: Python example code for the include callable from the django.urls module of the Django project.


include is a callable within the django.urls module of the Django project.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / wwwdccn / urls.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/wwwdccn/urls.py)

```python
# urls.py
from django.conf import settings
from django.conf.urls.static import static
~~from django.urls import path, include

urlpatterns = [
~~    path('', include('public_site.urls')),
~~    path('user/', include('user_site.urls')),
~~    path('auth/', include('auth_app.urls')),
~~    path('users/', include('users.urls')),
~~    path('registration/', include('registration.urls')),
~~    path('conferences/', include('conferences.urls')),
~~    path('submissions/', include('submissions.urls')),
~~    path('chair/', include('chair.urls')),
~~    path('chair_mail/', include('chair_mail.urls')),
~~    path('review/', include('review.urls')),
~~    path('gears/', include('gears.urls')),
~~    path('proceedings/', include('proceedings.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.USE_LOCAL_MEDIA:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.USE_DEBUG_TOOLBAR:
    import debug_toolbar
    urlpatterns = [
~~        path('__debug__/', include(debug_toolbar.urls)),


    ] + urlpatterns



## ... source file continues with no further include examples...

```


## Example 2 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / urls.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/./urls.py)

```python
# urls.py
from importlib import import_module

~~from django.urls import include, path

from allauth.socialaccount import providers

from . import app_settings


~~urlpatterns = [path('', include('allauth.account.urls'))]

if app_settings.SOCIALACCOUNT_ENABLED:
~~    urlpatterns += [path('social/', include('allauth.socialaccount.urls'))]

provider_urlpatterns = []
for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + '.urls')
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, 'urlpatterns', None)
    if prov_urlpatterns:
        provider_urlpatterns += prov_urlpatterns
urlpatterns += provider_urlpatterns



## ... source file continues with no further include examples...

```


## Example 3 from django-wiki
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

[**django-wiki / src/wiki / sites.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/./sites.py)

```python
# sites.py
from django.apps import apps
~~from django.urls import include
from django.urls import re_path
from django.utils.functional import LazyObject
from django.utils.module_loading import import_string
from wiki.conf import settings
from wiki.core.plugins import registry


class WikiSite:

    def __init__(self, name="wiki"):
        from wiki.views import accounts, article, deleted_list

        self.name = name

        self.root_view = getattr(self, "root_view", article.CreateRootView.as_view())
        self.root_missing_view = getattr(
            self, "root_missing_view", article.MissingRootView.as_view()
        )

        self.article_view = getattr(self, "article_view", article.ArticleView.as_view())
        self.article_create_view = getattr(
            self, "article_create_view", article.Create.as_view()
        )
        self.article_delete_view = getattr(


## ... source file abbreviated to get to include examples ...


                re_path(
                    r"^_accounts/settings/$",
                    self.profile_update_view,
                    name="profile_update",
                ),
            ]
        else:
            urlpatterns = []
        return urlpatterns

    def get_revision_urls(self):
        urlpatterns = [
            re_path(
                r"^change/(?P<revision_id>[0-9]+)/$",
                self.revision_change_view,
                name="change_revision",
            ),
            re_path(r"^preview/$", self.article_preview_view, name="preview_revision"),
            re_path(
                r"^merge/(?P<revision_id>[0-9]+)/preview/$",
                self.revision_preview_merge_view,
                name="merge_revision_preview",
            ),
        ]
        return [
~~            re_path(r"^_revision/(?P<article_id>[0-9]+)/", include(urlpatterns)),
        ]

    def get_article_urls(self):
        urlpatterns = [
            re_path(r"^$", self.article_view, name="get"),
            re_path(r"^delete/$", self.article_delete_view, name="delete"),
            re_path(r"^deleted/$", self.article_deleted_view, name="deleted"),
            re_path(r"^edit/$", self.article_edit_view, name="edit"),
            re_path(r"^move/$", self.article_move_view, name="move"),
            re_path(r"^preview/$", self.article_preview_view, name="preview"),
            re_path(r"^history/$", self.article_history_view, name="history"),
            re_path(r"^settings/$", self.article_settings_view, name="settings"),
            re_path(r"^source/$", self.article_source_view, name="source"),
            re_path(
                r"^revision/change/(?P<revision_id>[0-9]+)/$",
                self.revision_change_view,
                name="change_revision",
            ),
            re_path(
                r"^revision/merge/(?P<revision_id>[0-9]+)/$",
                self.revision_merge_view,
                name="merge_revision",
            ),
            re_path(
                r"^plugin/(?P<slug>\w+)/$", self.article_plugin_view, name="plugin"
            ),
        ]
        return [
~~            re_path(r"^(?P<article_id>[0-9]+)/", include(urlpatterns)),
        ]

    def get_article_path_urls(self):
        urlpatterns = [
            re_path(
                r"^(?P<path>.+/|)_create/$", self.article_create_view, name="create"
            ),
            re_path(
                r"^(?P<path>.+/|)_delete/$", self.article_delete_view, name="delete"
            ),
            re_path(
                r"^(?P<path>.+/|)_deleted/$", self.article_deleted_view, name="deleted"
            ),
            re_path(r"^(?P<path>.+/|)_edit/$", self.article_edit_view, name="edit"),
            re_path(r"^(?P<path>.+/|)_move/$", self.article_move_view, name="move"),
            re_path(
                r"^(?P<path>.+/|)_preview/$", self.article_preview_view, name="preview"
            ),
            re_path(
                r"^(?P<path>.+/|)_history/$", self.article_history_view, name="history"
            ),
            re_path(r"^(?P<path>.+/|)_dir/$", self.article_dir_view, name="dir"),
            re_path(r"^(?P<path>.+/|)_search/$", self.search_view, name="search"),
            re_path(


## ... source file abbreviated to get to include examples ...


                name="change_revision",
            ),
            re_path(
                r"^(?P<path>.+/|)_revision/merge/(?P<revision_id>[0-9]+)/$",
                self.revision_merge_view,
                name="merge_revision",
            ),
            re_path(
                r"^(?P<path>.+/|)_plugin/(?P<slug>\w+)/$",
                self.article_plugin_view,
                name="plugin",
            ),
            re_path(r"^(?P<path>.+/|)$", self.article_view, name="get"),
        ]
        return urlpatterns

    def get_plugin_urls(self):
        urlpatterns = []
        for plugin in registry.get_plugins().values():
            slug = getattr(plugin, "slug", None)
            if slug:
                article_urlpatterns = plugin.urlpatterns.get("article", [])
                urlpatterns += [
                    re_path(
                        r"^(?P<article_id>[0-9]+)/plugin/" + slug + "/",
~~                        include(article_urlpatterns),
                    ),
                    re_path(
                        r"^(?P<path>.+/|)_plugin/" + slug + "/",
~~                        include(article_urlpatterns),
                    ),
                ]
                root_urlpatterns = plugin.urlpatterns.get("root", [])
                urlpatterns += [
~~                    re_path(r"^_plugin/" + slug + "/", include(root_urlpatterns)),
                ]
        return urlpatterns


class DefaultWikiSite(LazyObject):
    def _setup(self):
        WikiSiteClass = import_string(apps.get_app_config("wiki").default_site)
        self._wrapped = WikiSiteClass()


site = DefaultWikiSite()



## ... source file continues with no further include examples...

```


## Example 4 from drf-action-serializer
[drf-action-serializer](https://github.com/gregschmit/drf-action-serializer)
([PyPI page](https://pypi.org/project/drf-action-serializer/))
that makes it easier to configure specific serializers to use based on the
client's request action. For example, a list view should have one serializer
whereas the detail view would have a different serializer.

The project is open source under the
[MIT license](https://github.com/gregschmit/drf-action-serializer/blob/master/LICENSE).

[**drf-action-serializer / action_serializer / urls.py**](https://github.com/gregschmit/drf-action-serializer/blob/master/action_serializer/./urls.py)

```python
# urls.py
from django.contrib import admin
~~from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .sample_group_viewset import GroupViewSet


router = DefaultRouter()
router.register("auth/group", GroupViewSet)
router.register("auth/groups", GroupViewSet)

urlpatterns = [
~~    path("api/", include(router.urls)),
~~    path("admin/doc/", include("django.contrib.admindocs.urls")),
    path("admin/", admin.site.urls),
]



## ... source file continues with no further include examples...

```

