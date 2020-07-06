title: django.views.generic RedirectView Example Code
category: page
slug: django-views-generic-redirectview-examples
sortorder: 500011525
toc: False
sidebartitle: django.views.generic RedirectView
meta: Python example code for the RedirectView class from the django.views.generic module of the Django project.


RedirectView is a class within the django.views.generic module of the Django project.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration
system built with [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

[**dccnsys / wwwdccn / registration / urls.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/registration/urls.py)

```python
# urls.py
from django.urls import path
~~from django.views.generic import RedirectView

from . import views

urlpatterns = [
~~    path('', RedirectView.as_view(pattern_name='register-personal'),
         name='register'),
    path('personal/', views.personal, name='register-personal'),
    path('professional/', views.professional, name='register-professional'),
    path('subscriptions/', views.subscriptions, name='register-subscriptions'),
]



## ... source file continues with no further RedirectView examples...

```


## Example 2 from django-wiki
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
~~from django.views.generic import RedirectView
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
    def dispatch(self, request, article, *args, **kwargs):


## ... source file abbreviated to get to RedirectView examples ...


                form = form_class(self.article, self.request)
            self.forms.append(form)
        return super().get(*args, **kwargs)

    def get(self, *args, **kwargs):
        self.forms = []

        new_article = models.Article.objects.get(id=self.article.id)

        for Form in self.get_form_classes():
            self.forms.append(Form(new_article, self.request))

        return super().get(*args, **kwargs)

    def get_success_url(self):
        if self.urlpath:
            return redirect("wiki:settings", path=self.urlpath.path)
        return redirect("wiki:settings", article_id=self.article.id)

    def get_context_data(self, **kwargs):
        kwargs["selected_tab"] = "settings"
        kwargs["forms"] = self.forms
        return super().get_context_data(**kwargs)


~~class ChangeRevisionView(RedirectView):

    permanent = False

    @method_decorator(get_article(can_write=True, not_locked=True))
    def dispatch(self, request, article, *args, **kwargs):
        self.article = article
        self.urlpath = kwargs.pop("kwargs", False)
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


## ... source file continues with no further RedirectView examples...

```

