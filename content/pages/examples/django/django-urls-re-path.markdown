title: django.urls re_path Example Code
category: page
slug: django-urls-re-path-examples
sortorder: 500011408
toc: False
sidebartitle: django.urls re_path
meta: Python example code for the re_path callable from the django.urls module of the Django project.


re_path is a callable within the django.urls module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / urls.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/urls.py)

```python
# urls.py
~~from django.urls import path, re_path

from . import views


urlpatterns = [
    path("signup/", views.signup, name="account_signup"),
    path("login/", views.login, name="account_login"),
    path("logout/", views.logout, name="account_logout"),
    path("password/change/", views.password_change,
         name="account_change_password"),
    path("password/set/", views.password_set, name="account_set_password"),
    path("inactive/", views.account_inactive, name="account_inactive"),

    path("email/", views.email, name="account_email"),
    path("confirm-email/", views.email_verification_sent,
         name="account_email_verification_sent"),
~~    re_path(r"^confirm-email/(?P<key>[-:\w]+)/$", views.confirm_email,
            name="account_confirm_email"),

    path("password/reset/", views.password_reset,
         name="account_reset_password"),
    path("password/reset/done/", views.password_reset_done,
         name="account_reset_password_done"),
~~    re_path(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
            views.password_reset_from_key,
            name="account_reset_password_from_key"),
    path("password/reset/key/done/", views.password_reset_from_key_done,
         name="account_reset_password_from_key_done"),
]



## ... source file continues with no further re_path examples...

```


## Example 2 from django-oauth-toolkit
[django-oauth-toolkit](https://github.com/jazzband/django-oauth-toolkit)
([project website](http://dot.evonove.it/) and
[PyPI package information](https://pypi.org/project/django-oauth-toolkit/1.2.0/))
is a code library for adding and handling [OAuth2](https://oauth.net/)
flows within your [Django](/django.html) web application and
[API](/application-programming-interfaces.html).

The django-oauth-toolkit project is open sourced under the
[FreeBSD license](https://github.com/jazzband/django-oauth-toolkit/blob/master/LICENSE)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-oauth-toolkit / oauth2_provider / urls.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/./urls.py)

```python
# urls.py
~~from django.urls import re_path

from . import views


app_name = "oauth2_provider"


base_urlpatterns = [
~~    re_path(r"^authorize/$", views.AuthorizationView.as_view(), name="authorize"),
~~    re_path(r"^token/$", views.TokenView.as_view(), name="token"),
~~    re_path(r"^revoke_token/$", views.RevokeTokenView.as_view(), name="revoke-token"),
~~    re_path(r"^introspect/$", views.IntrospectTokenView.as_view(), name="introspect"),
]


management_urlpatterns = [
~~    re_path(r"^applications/$", views.ApplicationList.as_view(), name="list"),
~~    re_path(r"^applications/register/$", views.ApplicationRegistration.as_view(), name="register"),
~~    re_path(r"^applications/(?P<pk>[\w-]+)/$", views.ApplicationDetail.as_view(), name="detail"),
~~    re_path(r"^applications/(?P<pk>[\w-]+)/delete/$", views.ApplicationDelete.as_view(), name="delete"),
~~    re_path(r"^applications/(?P<pk>[\w-]+)/update/$", views.ApplicationUpdate.as_view(), name="update"),
~~    re_path(r"^authorized_tokens/$", views.AuthorizedTokensListView.as_view(), name="authorized-token-list"),
~~    re_path(r"^authorized_tokens/(?P<pk>[\w-]+)/delete/$", views.AuthorizedTokenDeleteView.as_view(),
            name="authorized-token-delete"),
]


urlpatterns = base_urlpatterns + management_urlpatterns



## ... source file continues with no further re_path examples...

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
~~from django.urls import re_path
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
            self, "article_delete_view", article.Delete.as_view()


## ... source file abbreviated to get to re_path examples ...


        self.profile_update_view = getattr(
            self, "profile_update_view", accounts.Update.as_view()
        )

        self.deleted_list_view = getattr(
            self, "deleted_list_view", deleted_list.DeletedListView.as_view()
        )

    def get_urls(self):
        urlpatterns = self.get_root_urls()
        urlpatterns += self.get_accounts_urls()
        urlpatterns += self.get_deleted_list_urls()
        urlpatterns += self.get_revision_urls()
        urlpatterns += self.get_article_urls()
        urlpatterns += self.get_plugin_urls()

        urlpatterns += self.get_article_path_urls()
        return urlpatterns

    @property
    def urls(self):
        return self.get_urls(), "wiki", self.name

    def get_root_urls(self):
        urlpatterns = [
~~            re_path(r"^$", self.article_view, name="root", kwargs={"path": ""}),
~~            re_path(r"^create-root/$", self.root_view, name="root_create"),
~~            re_path(r"^missing-root/$", self.root_missing_view, name="root_missing"),
~~            re_path(r"^_search/$", self.search_view, name="search"),
~~            re_path(
                r"^_revision/diff/(?P<revision_id>[0-9]+)/$",
                self.article_diff_view,
                name="diff",
            ),
        ]
        return urlpatterns

    def get_deleted_list_urls(self):
        urlpatterns = [
~~            re_path("^_admin/$", self.deleted_list_view, name="deleted_list"),
        ]
        return urlpatterns

    def get_accounts_urls(self):
        if settings.ACCOUNT_HANDLING:
            urlpatterns = [
~~                re_path(r"^_accounts/sign-up/$", self.signup_view, name="signup"),
~~                re_path(r"^_accounts/logout/$", self.logout_view, name="logout"),
~~                re_path(r"^_accounts/login/$", self.login_view, name="login"),
~~                re_path(
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
~~            re_path(
                r"^change/(?P<revision_id>[0-9]+)/$",
                self.revision_change_view,
                name="change_revision",
            ),
~~            re_path(r"^preview/$", self.article_preview_view, name="preview_revision"),
~~            re_path(
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
~~            re_path(r"^$", self.article_view, name="get"),
~~            re_path(r"^delete/$", self.article_delete_view, name="delete"),
~~            re_path(r"^deleted/$", self.article_deleted_view, name="deleted"),
~~            re_path(r"^edit/$", self.article_edit_view, name="edit"),
~~            re_path(r"^move/$", self.article_move_view, name="move"),
~~            re_path(r"^preview/$", self.article_preview_view, name="preview"),
~~            re_path(r"^history/$", self.article_history_view, name="history"),
~~            re_path(r"^settings/$", self.article_settings_view, name="settings"),
~~            re_path(r"^source/$", self.article_source_view, name="source"),
~~            re_path(
                r"^revision/change/(?P<revision_id>[0-9]+)/$",
                self.revision_change_view,
                name="change_revision",
            ),
~~            re_path(
                r"^revision/merge/(?P<revision_id>[0-9]+)/$",
                self.revision_merge_view,
                name="merge_revision",
            ),
~~            re_path(
                r"^plugin/(?P<slug>\w+)/$", self.article_plugin_view, name="plugin"
            ),
        ]
        return [
~~            re_path(r"^(?P<article_id>[0-9]+)/", include(urlpatterns)),
        ]

    def get_article_path_urls(self):
        urlpatterns = [
~~            re_path(
                r"^(?P<path>.+/|)_create/$", self.article_create_view, name="create"
            ),
~~            re_path(
                r"^(?P<path>.+/|)_delete/$", self.article_delete_view, name="delete"
            ),
~~            re_path(
                r"^(?P<path>.+/|)_deleted/$", self.article_deleted_view, name="deleted"
            ),
~~            re_path(r"^(?P<path>.+/|)_edit/$", self.article_edit_view, name="edit"),
~~            re_path(r"^(?P<path>.+/|)_move/$", self.article_move_view, name="move"),
~~            re_path(
                r"^(?P<path>.+/|)_preview/$", self.article_preview_view, name="preview"
            ),
~~            re_path(
                r"^(?P<path>.+/|)_history/$", self.article_history_view, name="history"
            ),
~~            re_path(r"^(?P<path>.+/|)_dir/$", self.article_dir_view, name="dir"),
~~            re_path(r"^(?P<path>.+/|)_search/$", self.search_view, name="search"),
~~            re_path(
                r"^(?P<path>.+/|)_settings/$",
                self.article_settings_view,
                name="settings",
            ),
~~            re_path(
                r"^(?P<path>.+/|)_source/$", self.article_source_view, name="source"
            ),
~~            re_path(
                r"^(?P<path>.+/|)_revision/change/(?P<revision_id>[0-9]+)/$",
                self.revision_change_view,
                name="change_revision",
            ),
~~            re_path(
                r"^(?P<path>.+/|)_revision/merge/(?P<revision_id>[0-9]+)/$",
                self.revision_merge_view,
                name="merge_revision",
            ),
~~            re_path(
                r"^(?P<path>.+/|)_plugin/(?P<slug>\w+)/$",
                self.article_plugin_view,
                name="plugin",
            ),
~~            re_path(r"^(?P<path>.+/|)$", self.article_view, name="get"),
        ]
        return urlpatterns

    def get_plugin_urls(self):
        urlpatterns = []
        for plugin in registry.get_plugins().values():
            slug = getattr(plugin, "slug", None)
            if slug:
                article_urlpatterns = plugin.urlpatterns.get("article", [])
                urlpatterns += [
~~                    re_path(
                        r"^(?P<article_id>[0-9]+)/plugin/" + slug + "/",
                        include(article_urlpatterns),
                    ),
~~                    re_path(
                        r"^(?P<path>.+/|)_plugin/" + slug + "/",
                        include(article_urlpatterns),
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



## ... source file continues with no further re_path examples...

```

