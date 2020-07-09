title: django.utils.functional LazyObject Example Code
category: page
slug: django-utils-functional-lazyobject-examples
sortorder: 500011454
toc: False
sidebartitle: django.utils.functional LazyObject
meta: Python example code for the LazyObject class from the django.utils.functional module of the Django project.


LazyObject is a class within the django.utils.functional module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / utils / __init__.py**](https://github.com/divio/django-cms/blob/develop/cms/utils/__init__.py)

```python
# __init__.py
from django.conf import settings
from django.core.files.storage import get_storage_class
~~from django.utils.functional import LazyObject

from cms.utils.conf import get_site_id  # nopyflakes
from cms.utils.i18n import get_default_language
from cms.utils.i18n import get_language_list
from cms.utils.i18n import get_language_code


def get_current_site():
    from django.contrib.sites.models import Site

    return Site.objects.get_current()


def get_language_from_request(request, current_page=None):
    language = None
    if hasattr(request, 'POST'):
        language = request.POST.get('language', None)
    if hasattr(request, 'GET') and not language:
        language = request.GET.get('language', None)
    site_id = current_page.node.site_id if current_page else None
    if language:
        language = get_language_code(language)
        if not language in get_language_list(site_id):
            language = None
    if not language:
        language = get_language_code(getattr(request, 'LANGUAGE_CODE', None))
    if language:
        if not language in get_language_list(site_id):
            language = None

    if not language and current_page:
        languages = current_page.get_languages()

        if len(languages) > 0:
            language = languages[0]

    if not language:
        language = get_default_language(site_id=site_id)

    return language

default_storage = 'django.contrib.staticfiles.storage.StaticFilesStorage'


~~class ConfiguredStorage(LazyObject):
    def _setup(self):
        self._wrapped = get_storage_class(getattr(settings, 'STATICFILES_STORAGE', default_storage))()

configured_storage = ConfiguredStorage()



## ... source file continues with no further LazyObject examples...

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

[**django-debug-toolbar / debug_toolbar / panels / staticfiles.py**](https://github.com/jazzband/django-debug-toolbar/blob/master/debug_toolbar/panels/staticfiles.py)

```python
# staticfiles.py
from collections import OrderedDict
from os.path import join, normpath

from django.conf import settings
from django.contrib.staticfiles import finders, storage
from django.core.files.storage import get_storage_class
~~from django.utils.functional import LazyObject
from django.utils.translation import gettext_lazy as _, ngettext as __

from debug_toolbar import panels
from debug_toolbar.utils import ThreadCollector

try:
    import threading
except ImportError:
    threading = None


class StaticFile:

    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def real_path(self):
        return finders.find(self.path)

    def url(self):
        return storage.staticfiles_storage.url(self.path)


class FileCollector(ThreadCollector):
    def collect(self, path, thread=None):
        if path.endswith("/"):
            return
        super().collect(StaticFile(path), thread)


collector = FileCollector()


~~class DebugConfiguredStorage(LazyObject):

    def _setup(self):

        configured_storage_cls = get_storage_class(settings.STATICFILES_STORAGE)

        class DebugStaticFilesStorage(configured_storage_cls):
            def __init__(self, collector, *args, **kwargs):
                super().__init__(*args, **kwargs)
                self.collector = collector

            def url(self, path):
                self.collector.collect(path)
                return super().url(path)

        self._wrapped = DebugStaticFilesStorage(collector)


_original_storage = storage.staticfiles_storage


class StaticFilesPanel(panels.Panel):

    name = "Static files"
    template = "debug_toolbar/panels/staticfiles.html"


## ... source file continues with no further LazyObject examples...

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
from django.urls import include
from django.urls import re_path
~~from django.utils.functional import LazyObject
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
            self, "article_delete_view", article.Delete.as_view()
        )


## ... source file abbreviated to get to LazyObject examples ...


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
                        include(article_urlpatterns),
                    ),
                    re_path(
                        r"^(?P<path>.+/|)_plugin/" + slug + "/",
                        include(article_urlpatterns),
                    ),
                ]
                root_urlpatterns = plugin.urlpatterns.get("root", [])
                urlpatterns += [
                    re_path(r"^_plugin/" + slug + "/", include(root_urlpatterns)),
                ]
        return urlpatterns


~~class DefaultWikiSite(LazyObject):
    def _setup(self):
        WikiSiteClass = import_string(apps.get_app_config("wiki").default_site)
        self._wrapped = WikiSiteClass()


site = DefaultWikiSite()



## ... source file continues with no further LazyObject examples...

```

