title: django.views.generic.edit DeleteView Example Code
category: page
slug: django-views-generic-edit-deleteview-examples
sortorder: 500011535
toc: False
sidebartitle: django.views.generic.edit DeleteView
meta: Python example code for the DeleteView class from the django.views.generic.edit module of the Django project.


DeleteView is a class within the django.views.generic.edit module of the Django project.


## Example 1 from django-sql-explorer
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
from django.views.generic import ListView
from django.views.generic.base import View
~~from django.views.generic.edit import CreateView, DeleteView
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

from explorer.schema import schema_info


## ... source file abbreviated to get to DeleteView examples ...


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


~~class DeleteQueryView(PermissionRequiredMixin, ExplorerContextMixin, DeleteView):

    permission_required = 'change_permission'
    model = Query
    success_url = reverse_lazy("explorer_index")


class PlayQueryView(PermissionRequiredMixin, ExplorerContextMixin, View):

    permission_required = 'change_permission'

    def get(self, request):
        if url_get_query_id(request):
            query = get_object_or_404(Query, pk=url_get_query_id(request))
            return self.render_with_sql(request, query, run_query=False)

        if url_get_log_id(request):
            log = get_object_or_404(QueryLog, pk=url_get_log_id(request))
            query = Query(sql=log.sql, title="Playground", connection=log.connection)
            return self.render_with_sql(request, query)

        return self.render()

    def post(self, request):
        sql = request.POST.get('sql')


## ... source file continues with no further DeleteView examples...

```

