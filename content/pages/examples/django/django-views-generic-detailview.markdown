title: django.views.generic DetailView Example Code
category: page
slug: django-views-generic-detailview-examples
sortorder: 500011522
toc: False
sidebartitle: django.views.generic DetailView
meta: Python example code for the DetailView class from the django.views.generic module of the Django project.


DetailView is a class within the django.views.generic module of the Django project.


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
from django.utils.translation import ngettext
from django.views.decorators.clickjacking import xframe_options_sameorigin
~~from django.views.generic import DetailView
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

    template_name = "wiki/view.html"


## ... source file abbreviated to get to DetailView examples ...


    def post(self, request, *args, **kwargs):
        edit_form = forms.EditForm(
            request, self.article.current_revision, request.POST, preview=True
        )
        if edit_form.is_valid():
            self.title = edit_form.cleaned_data["title"]
            self.content = edit_form.cleaned_data["content"]
            self.preview = True
        return super().get(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if self.revision and not self.title:
            self.title = self.revision.title
        if self.revision and not self.content:
            self.content = self.revision.content
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs["title"] = self.title
        kwargs["revision"] = self.revision
        kwargs["content"] = self.content
        kwargs["preview"] = self.preview
        return ArticleMixin.get_context_data(self, **kwargs)


~~class DiffView(DetailView):
    model = models.ArticleRevision
    pk_url_kwarg = "revision_id"

    def render_to_response(self, context, **response_kwargs):
        revision = self.get_object()
        other_revision = revision.previous_revision

        baseText = other_revision.content if other_revision is not None else ""
        newText = revision.content

        differ = difflib.Differ(charjunk=difflib.IS_CHARACTER_JUNK)
        diff = differ.compare(
            baseText.splitlines(keepends=True), newText.splitlines(keepends=True)
        )
        other_changes = []

        if not other_revision or other_revision.title != revision.title:
            other_changes.append((_("New title"), revision.title))

        return object_to_json_response(
            {"diff": list(diff), "other_changes": other_changes}
        )




## ... source file continues with no further DetailView examples...

```

