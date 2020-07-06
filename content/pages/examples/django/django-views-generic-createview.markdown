title: django.views.generic CreateView Example Code
category: page
slug: django-views-generic-createview-examples
sortorder: 500011520
toc: False
sidebartitle: django.views.generic CreateView
meta: Python example code for the CreateView class from the django.views.generic module of the Django project.


CreateView is a class within the django.views.generic module of the Django project.


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
~~from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import UpdateView
from django.views.generic import View
from wiki import forms
from wiki.conf import settings

User = get_user_model()


~~class Signup(CreateView):
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
        context = super().get_context_data(**kwargs)
        context["honeypot_class"] = context["form"].honeypot_class
        context["honeypot_jsfunction"] = context["form"].honeypot_jsfunction
        return context

    def get_success_url(self, *args):
        messages.success(
            self.request, _("You are now signed up... and now you can sign in!")


## ... source file continues with no further CreateView examples...

```

