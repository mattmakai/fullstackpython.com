title: django.contrib.auth.decorators login_required Example Python Code
category: page
slug: django-contrib-auth-decorators-login-required-examples
sortorder: 500012150
toc: False
sidebartitle: django.contrib.auth.decorators login_required
meta: Python code examples for the Django function login_required from the django.contrib.auth.decorators module.


[Django](/django.html)'s
[login_required](https://docs.djangoproject.com/en/dev/topics/auth/default/#the-login-required-decorator)
function is used to secure views in your web applications by forcing
the client to authenticate with a valid logged-in User. This decorator
is a handy shortcut that can reduce the amount of code in your view
functions and eliminate the need for every function to have
boilerplate like `if not request.user.is_authenticated:`.


## Example 1 from dccnsys
[dccnsys](https://github.com/dccnconf/dccnsys) is a conference registration 
web app built in [Django](/django.html). The code is open source under the
[MIT license](https://github.com/dccnconf/dccnsys/blob/master/LICENSE).

The dccnsys project provides a typical `login_required` decorator usage 
example. The decorator is placed on a view function, in this case `personal`,
to protect it from being accessible by unauthenticated users.

[**dccnsys / wwwdccn / registration / views.py**](https://github.com/dccnconf/dccnsys/blob/master/wwwdccn/registration/views.py)

```python
from django.contrib.auth import get_user_model
~~from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.models import generate_avatar
from users.forms import (PersonalForm, ProfessionalForm, 
                         SubscriptionsForm)

User = get_user_model()


~~@login_required
def personal(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = PersonalForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            profile.avatar = generate_avatar(profile)
            profile.save()
            return redirect('register-professional')
    else:
        form = PersonalForm(instance=profile)
    return render(request, 'registration/personal.html', {
        'form': form
    })


~~@login_required
def professional(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfessionalForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('register-subscriptions')
    else:
        form = ProfessionalForm(instance=profile)
    return render(request, 'registration/professional.html', {
        'form': form
    })


~~@login_required
def subscriptions(request):
    subscriptions = request.user.subscriptions
    if request.method == 'POST':
        form = SubscriptionsForm(request.POST, instance=subscriptions)
        if form.is_valid():
            form.save()
            request.user.has_finished_registration = True
            request.user.save()
            return redirect('home')
    else:
        form = SubscriptionsForm(instance=subscriptions)
    return render(request, 'registration/subscriptions.html', {
        'form': form
    })
```

## Example 2 from django-oscar
[django-oscar](https://github.com/django-oscar/django-oscar/) 
([project website](http://oscarcommerce.com/))
is a framework for building e-commerce sites on top of 
[Django](/django.html). The code for the project is available open 
source under a 
[custom license written by Tangent Communications PLC](https://github.com/django-oscar/django-oscar/blob/master/LICENSE).

The following `login_required` example is one that surprised me
a bit because I had not previously seen `login_required` applied
on the parameter to the [url](/django-conf-urls-url-examples.html)
function. Typically the decorator is used on view function where
it is defined, but this way works as well as long as you are
consistent about where you apply the decorator in your code base.

[**django-oscar / src / oscar / apps / customer / apps.py**](https://github.com/django-oscar/django-oscar/blob/master/src/oscar/apps/customer/apps.py)

```python
from django.conf.urls import url
~~from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.views import generic

from oscar.core.application import OscarConfig
from oscar.core.loading import get_class


class CustomerConfig(OscarConfig):
    label = 'customer'
    name = 'oscar.apps.customer'
    verbose_name = _('Customer')

    namespace = 'customer'

    def ready(self):
        from . import receivers  # noqa
        from .alerts import receivers  # noqa

        self.summary_view = get_class('customer.views', 
                                      'AccountSummaryView')
        self.order_history_view = get_class('customer.views', 
                                            'OrderHistoryView')
        self.order_detail_view = get_class('customer.views', 
                                           'OrderDetailView')

    ## ... abbreviating code not relevant to login_required ...


    def get_urls(self):
        urls = [
            # Login, logout and register doesn't require login
            url(r'^login/$', self.login_view.as_view(), 
                name='login'),
            url(r'^logout/$', self.logout_view.as_view(), 
                name='logout'),
            url(r'^register/$', self.register_view.as_view(), 
                name='register'),
~~            url(r'^$', login_required(self.summary_view.as_view()),
~~                name='summary'),
~~            url(r'^change-password/$',
~~                login_required(self.change_password_view.as_view()),
~~                name='change-password'),

            # Profile
~~            url(r'^profile/$',
~~                login_required(self.profile_view.as_view()),
~~                name='profile-view'),
~~            url(r'^profile/edit/$',
~~                login_required(self.profile_update_view.as_view()),
~~                name='profile-update'),
~~            url(r'^profile/delete/$',
~~                login_required(self.profile_delete_view.as_view()),
~~                name='profile-delete'),

## the file continues with further examples that show the same usage
```
