title: django.contrib.auth.decorators login_required Example Python Code
category: page
slug: django-contrib-auth-decorators-login-required-examples
sortorder: 50025
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
