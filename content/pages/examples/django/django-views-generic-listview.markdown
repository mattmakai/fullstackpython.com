title: django.views.generic ListView Example Code
category: page
slug: django-views-generic-listview-examples
sortorder: 500011524
toc: False
sidebartitle: django.views.generic ListView
meta: Python example code for the ListView class from the django.views.generic module of the Django project.


ListView is a class within the django.views.generic module of the Django project.


## Example 1 from django-mongonaut
[django-mongonaut](https://github.com/jazzband/django-mongonaut)
([project documentation](https://django-mongonaut.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-mongonaut/))
provides an introspective interface for working with
[MongoDB](/mongodb.html) via mongoengine. The project has its own new code
to map MongoDB to the [Django](/django.html) Admin interface.

django-mongonaut's highlighted features include automatic introspection of
mongoengine documents, the ability to constrain who sees what and what
they can do and full control for adding, editing and deleting documents.

The django-mongonaut project is open sourced under the
[MIT License](https://github.com/jazzband/django-mongonaut/blob/master/LICENSE.txt)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-mongonaut / mongonaut / views.py**](https://github.com/jazzband/django-mongonaut/blob/master/mongonaut/./views.py)

```python
# views.py
import math

from django.contrib import messages
from django.urls import reverse
from django.forms import Form
from django.http import HttpResponseForbidden
from django.http import Http404
from django.utils.functional import cached_property
from django.views.generic.edit import DeletionMixin
~~from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from mongoengine.fields import EmbeddedDocumentField, ListField

from mongonaut.forms import MongoModelForm
from mongonaut.mixins import MongonautFormViewMixin
from mongonaut.mixins import MongonautViewMixin
from mongonaut.utils import is_valid_object_id


~~class IndexView(MongonautViewMixin, ListView):

    template_name = "mongonaut/index.html"
    queryset = []
    permission = 'has_view_permission'

    def get_queryset(self):
        return self.get_mongoadmins()


class DocumentListView(MongonautViewMixin, FormView):
    form_class = Form
    success_url = '/'
    template_name = "mongonaut/document_list.html"
    permission = 'has_view_permission'

    documents_per_page = 25


    def get_qset(self, queryset, q):
        if self.mongoadmin.search_fields and q:
            params = {}
            for field in self.mongoadmin.search_fields:
                if field == 'id':
                    if is_valid_object_id(q):


## ... source file continues with no further ListView examples...

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

[**django-oauth-toolkit / oauth2_provider / views / token.py**](https://github.com/jazzband/django-oauth-toolkit/blob/master/oauth2_provider/views/token.py)

```python
# token.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
~~from django.views.generic import DeleteView, ListView

from ..models import get_access_token_model


~~class AuthorizedTokensListView(LoginRequiredMixin, ListView):
    context_object_name = "authorized_tokens"
    template_name = "oauth2_provider/authorized-tokens.html"
    model = get_access_token_model()

    def get_queryset(self):
        return super().get_queryset().select_related("application").filter(
            user=self.request.user
        )


class AuthorizedTokenDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "oauth2_provider/authorized-token-delete.html"
    success_url = reverse_lazy("oauth2_provider:authorized-token-list")
    model = get_access_token_model()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)



## ... source file continues with no further ListView examples...

```


## Example 3 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / views.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/./views.py)

```python
# views.py
import re
import six
from collections import Counter

try:
    from django.urls import reverse_lazy
except ImportError:
    from django.core.urlresolvers import reverse_lazy

import django
from django.db import DatabaseError
from django.db.models import Count
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST
from django.utils.decorators import method_decorator
~~from django.views.generic import ListView
from django.views.generic.base import View
from django.views.generic.edit import CreateView, DeleteView
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.core.exceptions import ImproperlyConfigured
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import LoginView

from explorer import app_settings
from explorer.connections import connections
from explorer.exporters import get_exporter_class
from explorer.forms import QueryForm
from explorer.models import Query, QueryLog, MSG_FAILED_BLACKLIST
from explorer.tasks import execute_query
from explorer.utils import (
    url_get_rows,
    url_get_query_id,
    url_get_log_id,
    url_get_params,
    safe_login_prompt,
    fmt_sql,
    allowed_query_pks,
    url_get_show,
    url_get_fullscreen
)


## ... source file abbreviated to get to ListView examples ...


    permission_required = 'change_permission'

    @method_decorator(xframe_options_sameorigin)
    def dispatch(self, *args, **kwargs):
        return super(SchemaView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        connection = kwargs.get('connection')
        if connection not in connections:
            raise Http404
        schema = schema_info(connection)
        if schema:
            return render(None, 'explorer/schema.html',
                                      {'schema': schema_info(connection)})
        else:
            return render(None, 'explorer/schema_building.html')


@require_POST
def format_sql(request):
    sql = request.POST.get('sql', '')
    formatted = fmt_sql(sql)
    return JsonResponse({"formatted": formatted})


~~class ListQueryView(PermissionRequiredMixin, ExplorerContextMixin, ListView):

    permission_required = 'view_permission_list'

    def recently_viewed(self):
        qll = QueryLog.objects.filter(run_by_user=self.request.user, query_id__isnull=False).order_by(
            '-run_at').select_related('query')
        ret = []
        tracker = []
        for ql in qll:
            if len(ret) == app_settings.EXPLORER_RECENT_QUERY_COUNT:
                break

            if ql.query_id not in tracker:
                ret.append(ql)
                tracker.append(ql.query_id)
        return ret

    def get_context_data(self, **kwargs):
        context = super(ListQueryView, self).get_context_data(**kwargs)
        context['object_list'] = self._build_queries_and_headers()
        context['recent_queries'] = self.recently_viewed()
        context['tasks_enabled'] = app_settings.ENABLE_TASKS
        return context



## ... source file abbreviated to get to ListView examples ...


        for q in self.object_list:
            model_dict = model_to_dict(q)
            header = q.title.split(' - ')[0]
            collapse_target = pattern.sub('', header)

            if headers[header] > 1 and header not in rendered_headers:
                dict_list.append({'title': header,
                                  'is_header': True,
                                  'is_in_category': False,
                                  'collapse_target': collapse_target,
                                  'count': headers[header]})
                rendered_headers.append(header)

            model_dict.update({'is_in_category': headers[header] > 1,
                               'collapse_target': collapse_target,
                               'created_at': q.created_at,
                               'is_header': False,
                               'run_count': q.run_count,
                               'created_by_user': six.text_type(q.created_by_user) if q.created_by_user else None})
            dict_list.append(model_dict)
        return dict_list

    model = Query


~~class ListQueryLogView(PermissionRequiredMixin, ExplorerContextMixin, ListView):

    permission_required = 'view_permission'

    def get_queryset(self):
        kwargs = {'sql__isnull': False}
        if url_get_query_id(self.request):
            kwargs['query_id'] = url_get_query_id(self.request)
        return QueryLog.objects.filter(**kwargs).all()

    context_object_name = "recent_logs"
    model = QueryLog
    paginate_by = 20


class CreateQueryView(PermissionRequiredMixin, ExplorerContextMixin, CreateView):

    permission_required = 'change_permission'

    def form_valid(self, form):
        form.instance.created_by_user = self.request.user
        return super(CreateQueryView, self).form_valid(form)

    form_class = QueryForm
    template_name = 'explorer/query.html'


## ... source file continues with no further ListView examples...

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
from django.utils.translation import ngettext
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.generic import DetailView
from django.views.generic import FormView
~~from django.views.generic import ListView
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

    template_name = "wiki/view.html"

    @method_decorator(get_article(can_read=True))


## ... source file abbreviated to get to ListView examples ...



    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["selected_tab"] = "source"
        return super().get_context_data(**kwargs)


~~class History(ListView, ArticleMixin):

    template_name = "wiki/history.html"
    allow_empty = True
    context_object_name = "revisions"
    paginator_class = WikiPaginator
    paginate_by = 10

    def get_queryset(self):
        return models.ArticleRevision.objects.filter(article=self.article).order_by(
            "-created"
        )

    def get_context_data(self, **kwargs):
        kwargs_article = ArticleMixin.get_context_data(self, **kwargs)
~~        kwargs_listview = ListView.get_context_data(self, **kwargs)
        kwargs.update(kwargs_article)
        kwargs.update(kwargs_listview)
        kwargs["selected_tab"] = "history"
        return kwargs

    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)


~~class Dir(ListView, ArticleMixin):

    template_name = "wiki/dir.html"
    allow_empty = True
    context_object_name = "directory"
    model = models.URLPath
    paginator_class = WikiPaginator
    paginate_by = 30

    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        self.filter_form = forms.DirFilterForm(request.GET)
        if self.filter_form.is_valid():
            self.query = self.filter_form.cleaned_data["query"]
        else:
            self.query = None
        return super().dispatch(request, article, *args, **kwargs)

    def get_queryset(self):
        children = self.urlpath.get_children().can_read(self.request.user)
        if self.query:
            children = children.filter(
                Q(article__current_revision__title__icontains=self.query)
                | Q(slug__icontains=self.query)
            )
        if not self.article.can_moderate(self.request.user):
            children = children.active()
        children = children.select_related_common().order_by(
            "article__current_revision__title"
        )
        return children

    def get_context_data(self, **kwargs):
        kwargs_article = ArticleMixin.get_context_data(self, **kwargs)
~~        kwargs_listview = ListView.get_context_data(self, **kwargs)
        kwargs.update(kwargs_article)
        kwargs.update(kwargs_listview)
        kwargs["filter_query"] = self.query
        kwargs["filter_form"] = self.filter_form

        updated_children = kwargs[self.context_object_name]
        for child in updated_children:
            child.set_cached_ancestors_from_parent(self.urlpath)
        kwargs[self.context_object_name] = updated_children

        return kwargs


~~class SearchView(ListView):

    template_name = "wiki/search.html"
    paginator_class = WikiPaginator
    paginate_by = 25
    context_object_name = "articles"

    def dispatch(self, request, *args, **kwargs):
        self.urlpath = None
        if request.user.is_anonymous and not settings.ANONYMOUS:
            return redirect(settings.LOGIN_URL)
        self.search_form = forms.SearchForm(request.GET)
        if self.search_form.is_valid():
            self.query = self.search_form.cleaned_data["q"]
        else:
            self.query = None
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if not self.query:
            return models.Article.objects.none().order_by("-current_revision__created")
        articles = models.Article.objects
        path = self.kwargs.get("path", None)
        if path:
            try:

    def get_initial(self):
        return {
            "revision": self.article.current_revision,
            "purge": True,
        }

    def get_context_data(self, **kwargs):
        kwargs["purge_form"] = self.get_form()
        kwargs["form"] = kwargs["purge_form"]
        return super().get_context_data(**kwargs)


class Source(ArticleMixin, TemplateView):
    template_name = "wiki/source.html"


## ... source file continues with no further ListView examples...

```

