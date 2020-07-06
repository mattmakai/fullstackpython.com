title: django.views.generic TemplateView Example Code
category: page
slug: django-views-generic-templateview-examples
sortorder: 500011526
toc: False
sidebartitle: django.views.generic TemplateView
meta: Python example code for the TemplateView class from the django.views.generic module of the Django project.


TemplateView is a class within the django.views.generic module of the Django project.


## Example 1 from django-markdown-view
[django-markdown-view](https://github.com/rgs258/django-markdown-view)
([PyPI package information](https://pypi.org/project/django-markdown-view/))
is a Django extension for serving [Markdown](/markdown.html) files as
[Django templates](/django-templates.html). The project is open
sourced under the
[BSD 3-Clause "New" or "Revised" license](https://github.com/rgs258/django-markdown-view/blob/master/LICENSE).

[**django-markdown-view / markdown_view / views.py**](https://github.com/rgs258/django-markdown-view/blob/master/markdown_view/./views.py)

```python
# views.py
import logging

import markdown
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template import Engine, Template, Context
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
~~from django.views.generic import TemplateView
from markdown_view.constants import (
    DEFAULT_MARKDOWN_VIEW_LOADERS,
    DEFAULT_MARKDOWN_VIEW_EXTENSIONS, DEFAULT_MARKDOWN_VIEW_TEMPLATE,
    DEFAULT_MARKDOWN_VIEW_USE_REQUEST_CONTEXT, DEFAULT_MARKDOWN_VIEW_EXTRA_CONTEXT,
)

logger = logging.getLogger(__name__)


~~class MarkdownView(TemplateView):
    file_name = None

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        if self.file_name:
            engine = Engine(loaders=getattr(
                settings, "MARKDOWN_VIEW_LOADERS", DEFAULT_MARKDOWN_VIEW_LOADERS)
            )
            template = engine.get_template(self.file_name)
            md = markdown.Markdown(extensions=getattr(
                settings,
                "MARKDOWN_VIEW_EXTENSIONS",
                DEFAULT_MARKDOWN_VIEW_EXTENSIONS
            ))
            template = Template(
                "{{% load static %}}{}".format(md.convert(template.source))
            )
            render_context_base = {}
            if getattr(
                settings,
                "MARKDOWN_VIEW_USE_REQUEST_CONTEXT",
                DEFAULT_MARKDOWN_VIEW_USE_REQUEST_CONTEXT
            ):
                render_context_base = context


## ... source file continues with no further TemplateView examples...

```


## Example 2 from django-mongonaut
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
from django.views.generic import ListView
~~from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from mongoengine.fields import EmbeddedDocumentField, ListField

from mongonaut.forms import MongoModelForm
from mongonaut.mixins import MongonautFormViewMixin
from mongonaut.mixins import MongonautViewMixin
from mongonaut.utils import is_valid_object_id


class IndexView(MongonautViewMixin, ListView):

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


## ... source file abbreviated to get to TemplateView examples ...


            for key in [x for x in self.mongoadmin.list_fields if x != 'id' and x in self.document._fields.keys()]:

                if isinstance(self.document._fields[key], EmbeddedDocumentField):
                    continue
                if isinstance(self.document._fields[key], ListField):
                    continue
                context['keys'].append(key)

        if self.mongoadmin.search_fields:
            context['search_field'] = True

        return context

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        mongo_ids = self.get_initial()['mongo_id']
        for form_mongo_id in form.data.getlist('mongo_id'):
            for mongo_id in mongo_ids:
                if form_mongo_id == mongo_id:
                    self.document.objects.get(pk=mongo_id).delete()

        return self.form_invalid(form)


~~class DocumentDetailView(MongonautViewMixin, TemplateView):
    template_name = "mongonaut/document_detail.html"
    permission = 'has_view_permission'

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        self.set_mongoadmin()
        context = self.set_permissions_in_context(context)
        self.document_type = getattr(self.models, self.document_name)
        self.ident = self.kwargs.get('id')
        self.document = self.document_type.objects.get(pk=self.ident)

        context['document'] = self.document
        context['app_label'] = self.app_label
        context['document_name'] = self.document_name
        context['keys'] = ['id', ]
        context['embedded_documents'] = []
        context['list_fields'] = []
        for key in sorted([x for x in self.document._fields.keys() if x != 'id']):
            if isinstance(self.document._fields[key], EmbeddedDocumentField):
                context['embedded_documents'].append(key)
                continue
            if isinstance(self.document._fields[key], ListField):
                context['list_fields'].append(key)
                continue


## ... source file abbreviated to get to TemplateView examples ...


    def get_context_data(self, **kwargs):
        context = super(DocumentAddFormView, self).get_context_data(**kwargs)
        self.set_mongoadmin()
        context = self.set_permissions_in_context(context)
        self.document_type = getattr(self.models, self.document_name)

        context['app_label'] = self.app_label
        context['document_name'] = self.document_name
        context['form_action'] = reverse('document_detail_add_form', args=[self.kwargs.get('app_label'),
                                                                           self.kwargs.get('document_name')])

        return context

    def get_form(self):
        self.set_mongonaut_base()
        self.document_type = getattr(self.models, self.document_name)
        self.form = Form()

        if self.request.method == 'POST':
            self.form = self.process_post_form('Your new document has been added and saved.')
        else:
            self.form = MongoModelForm(model=self.document_type).get_form()
        return self.form


~~class DocumentDeleteView(DeletionMixin, MongonautViewMixin, TemplateView):

    success_url = "/"
    template_name = "mongonaut/document_delete.html"

    def get_success_url(self):
        self.set_mongonaut_base()
        messages.add_message(self.request, messages.INFO, 'Your document has been deleted.')
        return reverse('document_list', kwargs={'app_label': self.app_label, 'document_name': self.document_name})

    def get_object(self):
        self.set_mongoadmin()
        self.document_type = getattr(self.models, self.document_name)
        self.ident = self.kwargs.get('id')
        self.document = self.document_type.objects.get(pk=self.ident)
        return self.document



## ... source file continues with no further TemplateView examples...

```


## Example 3 from django-smithy
[django-smithy](https://github.com/jamiecounsell/django-smithy) is
a [Django](/django.html) code library that allows users to send
HTTP requests from the Django admin user interface. The code for
the project is open source under the
[MIT license](https://github.com/jamiecounsell/django-smithy/blob/master/LICENSE).

[**django-smithy / smithy / urls.py**](https://github.com/jamiecounsell/django-smithy/blob/master/smithy/./urls.py)

```python
# urls.py
from django.conf.urls import url
~~from django.views.generic import TemplateView

from . import views


app_name = 'smithy'

urlpatterns = [

]



## ... source file continues with no further TemplateView examples...

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
from django.views.generic import ListView
from django.views.generic import RedirectView
~~from django.views.generic import TemplateView
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


~~class ArticleView(ArticleMixin, TemplateView):

    template_name = "wiki/view.html"

    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)


## ... source file abbreviated to get to TemplateView examples ...


        try:
            root = models.URLPath.root()
        except NoRootURL:
            pass
        else:
            if root.article:
                return redirect("wiki:get", path=root.path)

            root.delete()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        models.URLPath.create_root(
            title=form.cleaned_data["title"],
            content=form.cleaned_data["content"],
            request=self.request,
        )
        return redirect("wiki:root")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["editor"] = editors.getEditor()
        return kwargs


~~class MissingRootView(TemplateView):
    template_name = "wiki/root_missing.html"


    def get_context_data(self, **kwargs):
        kwargs["selected_tab"] = "view"
        return ArticleMixin.get_context_data(self, **kwargs)


class Create(FormView, ArticleMixin):
    form_class = forms.CreateForm
    template_name = "wiki/create.html"

    @method_decorator(get_article(can_write=True, can_create=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        kwargs = self.get_form_kwargs()


## ... source file abbreviated to get to TemplateView examples ...


                self.article.add_revision(revision)
                messages.success(
                    request,
                    _('The article "%s" and its children are now restored.')
                    % revision.title,
                )
                if self.urlpath:
                    return redirect("wiki:get", path=self.urlpath.path)
                else:
                    return redirect("wiki:get", article_id=article.id)

        return super().dispatch1(request, article, *args, **kwargs)

    def get_initial(self):
        return {
            "revision": self.article.current_revision,
            "purge": True,
        }

    def get_context_data(self, **kwargs):
        kwargs["purge_form"] = self.get_form()
        kwargs["form"] = kwargs["purge_form"]
        return super().get_context_data(**kwargs)


~~class Source(ArticleMixin, TemplateView):
    template_name = "wiki/source.html"

    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["selected_tab"] = "source"
        return super().get_context_data(**kwargs)


class History(ListView, ArticleMixin):

    template_name = "wiki/history.html"
    allow_empty = True
    context_object_name = "revisions"
    paginator_class = WikiPaginator
    paginate_by = 10

    def get_queryset(self):
        return models.ArticleRevision.objects.filter(article=self.article).order_by(
            "-created"
        )



## ... source file abbreviated to get to TemplateView examples ...


            | Q(current_revision__content__icontains=self.query)
        )
        if not permissions.can_moderate(
            models.URLPath.root().article, self.request.user
        ):
            articles = articles.active().can_read(self.request.user)
        return articles.order_by("-current_revision__created")

    def get_context_data(self, **kwargs):
        kwargs = super().get_context_data(**kwargs)
        kwargs["search_form"] = self.search_form
        kwargs["search_query"] = self.query
        kwargs["urlpath"] = self.urlpath
        return kwargs


class Plugin(View):
    def dispatch(self, request, path=None, slug=None, **kwargs):
        kwargs["path"] = path
        for plugin in list(plugin_registry.get_plugins().values()):
            if getattr(plugin, "slug", None) == slug:
                return plugin.article_view(request, **kwargs)
        raise Http404()


~~class Settings(ArticleMixin, TemplateView):

    permission_form_class = forms.PermissionsForm
    template_name = "wiki/settings.html"

    @method_decorator(login_required)
    @method_decorator(get_article(can_read=True))
    def dispatch(self, request, article, *args, **kwargs):
        return super().dispatch(request, article, *args, **kwargs)

    def get_form_classes(self):
        settings_forms = []
        if permissions.can_change_permissions(self.article, self.request.user):
            settings_forms.append(self.permission_form_class)
        plugin_forms = [F for F in plugin_registry.get_settings_forms()]
        plugin_forms.sort(key=lambda form: form.settings_order)
        settings_forms += plugin_forms
        for i in range(len(settings_forms)):
            setattr(settings_forms[i], "action", "form%d" % i)

        return settings_forms

    def post(self, *args, **kwargs):
        self.forms = []
        for form_class in self.get_form_classes():


## ... source file abbreviated to get to TemplateView examples ...


        self.change_revision()

        return super().dispatch(request, *args, **kwargs)

    def get_redirect_url(self, **kwargs):
        if self.urlpath:
            return reverse("wiki:history", kwargs={"path": self.urlpath.path})
        else:
            return reverse("wiki:history", kwargs={"article_id": self.article.id})

    def change_revision(self):
        revision = get_object_or_404(
            models.ArticleRevision, article=self.article, id=self.kwargs["revision_id"]
        )
        self.article.current_revision = revision
        self.article.save()
        messages.success(
            self.request,
            _(
                "The article %(title)s is now set to display revision #%(revision_number)d"
            )
            % {"title": revision.title, "revision_number": revision.revision_number},
        )


~~class Preview(ArticleMixin, TemplateView):

    template_name = "wiki/preview_inline.html"

    @method_decorator(xframe_options_sameorigin)
    @method_decorator(get_article(can_read=True, deleted_contents=True))
    def dispatch(self, request, article, *args, **kwargs):
        revision_id = request.GET.get("r", None)
        self.title = None
        self.content = None
        self.preview = False
        if revision_id:
            try:
                revision_id = int(revision_id)
            except ValueError:
                raise Http404()
            self.revision = get_object_or_404(
                models.ArticleRevision, article=article, id=revision_id
            )
        else:
            self.revision = None
        return super().dispatch(request, article, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        edit_form = forms.EditForm(


## ... source file continues with no further TemplateView examples...

```

