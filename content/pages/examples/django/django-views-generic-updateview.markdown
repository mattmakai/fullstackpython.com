title: django.views.generic UpdateView Example Code
category: page
slug: django-views-generic-updateview-examples
sortorder: 500011527
toc: False
sidebartitle: django.views.generic UpdateView
meta: Python example code for the UpdateView class from the django.views.generic module of the Django project.


UpdateView is a class within the django.views.generic module of the Django project.


## Example 1 from django-jet
[django-jet](https://github.com/geex-arts/django-jet)
([project documentation](https://jet.readthedocs.io/en/latest/),
[PyPI project page](https://pypi.org/project/django-jet/) and
[more information](http://jet.geex-arts.com/))
is a fancy [Django](/django.html) Admin panel replacement.

The django-jet project is open source under the
[GNU Affero General Public License v3.0](https://github.com/geex-arts/django-jet/blob/dev/LICENSE).

[**django-jet / jet / dashboard / views.py**](https://github.com/geex-arts/django-jet/blob/dev/jet/dashboard/views.py)

```python
# views.py
from django.contrib import messages
from django.core.exceptions import ValidationError
try:
    from django.core.urlresolvers import reverse
except ImportError: # Django 1.11
    from django.urls import reverse

from django.forms.formsets import formset_factory
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_POST, require_GET
from jet.dashboard.forms import UpdateDashboardModulesForm, AddUserDashboardModuleForm, \
    UpdateDashboardModuleCollapseForm, RemoveDashboardModuleForm, ResetDashboardForm
from jet.dashboard.models import UserDashboardModule
from jet.utils import JsonResponse, get_app_list, SuccessMessageMixin, user_is_authenticated
~~from django.views.generic import UpdateView
from django.utils.translation import ugettext_lazy as _


~~class UpdateDashboardModuleView(SuccessMessageMixin, UpdateView):
    model = UserDashboardModule
    fields = ('title',)
    template_name = 'jet.dashboard/update_module.html'
    success_message = _('Widget was successfully updated')
    object = None
    module = None

    def has_permission(self, request):
        return request.user.is_active and request.user.is_staff

    def get_success_url(self):
        if self.object.app_label:
            return reverse('admin:app_list', kwargs={'app_label': self.object.app_label})
        else:
            return reverse('admin:index')

    def get_module(self):
        object = self.object if getattr(self, 'object', None) is not None else self.get_object()
        return object.load_module()

    def get_settings_form_kwargs(self):
        kwargs = {
            'initial': self.module.settings
        }


## ... source file continues with no further UpdateView examples...

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

[**django-wiki / src/wiki / views / accounts.py**](https://github.com/django-wiki/django-wiki/blob/master/src/wiki/views/accounts.py)

```python
# accounts.py
from django.conf import settings as django_settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.generic import CreateView
from django.views.generic import FormView
~~from django.views.generic import UpdateView
from django.views.generic import View
from wiki import forms
from wiki.conf import settings

User = get_user_model()


class Signup(CreateView):
    model = User
    form_class = forms.UserCreationForm
    template_name = "wiki/accounts/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous and not request.user.is_superuser:
            return redirect("wiki:root")
        if not settings.ACCOUNT_HANDLING:
            return redirect(settings.SIGNUP_URL)
        if not request.user.is_superuser and not settings.ACCOUNT_SIGNUP_ALLOWED:
            c = {"error_msg": _("Account signup is only allowed for administrators.")}
            return render(request, "wiki/error.html", context=c)

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):


## ... source file abbreviated to get to UpdateView examples ...


        kwargs["request"] = self.request
        return kwargs

    def post(self, request, *args, **kwargs):
        self.referer = request.session.get("login_referer", "")
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.referer = request.META.get("HTTP_REFERER", "")
        request.session["login_referer"] = self.referer
        return super().get(request, *args, **kwargs)

    def form_valid(self, form, *args, **kwargs):
        auth_login(self.request, form.get_user())
        messages.info(self.request, _("You are now logged in! Have fun!"))
        if self.request.GET.get("next", None):
            return redirect(self.request.GET["next"])
        if django_settings.LOGIN_REDIRECT_URL:
            return redirect(django_settings.LOGIN_REDIRECT_URL)
        else:
            if not self.referer:
                return redirect("wiki:root")
            return redirect(self.referer)


~~class Update(UpdateView):
    model = User
    form_class = forms.UserUpdateForm
    template_name = "wiki/accounts/account_settings.html"

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.request.user.pk)

    def get(self, request, *args, **kwargs):
        self.referer = request.META.get("HTTP_REFERER", "")
        request.session["login_referer"] = self.referer
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.referer = request.session.get("login_referer", "")
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        pw = form.cleaned_data["password1"]
        if pw != "":
            self.object.set_password(pw)
        self.object.save()

        messages.info(self.request, _("Account info saved!"))



## ... source file continues with no further UpdateView examples...

```

