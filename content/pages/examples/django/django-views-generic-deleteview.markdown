title: django.views.generic DeleteView Example Code
category: page
slug: django-views-generic-deleteview-examples
sortorder: 500011521
toc: False
sidebartitle: django.views.generic DeleteView
meta: Python example code for the DeleteView class from the django.views.generic module of the Django project.


DeleteView is a class within the django.views.generic module of the Django project.


## Example 1 from django-oauth-toolkit
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


class AuthorizedTokensListView(LoginRequiredMixin, ListView):
    context_object_name = "authorized_tokens"
    template_name = "oauth2_provider/authorized-tokens.html"
    model = get_access_token_model()

    def get_queryset(self):
        return super().get_queryset().select_related("application").filter(
            user=self.request.user
        )


~~class AuthorizedTokenDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "oauth2_provider/authorized-token-delete.html"
    success_url = reverse_lazy("oauth2_provider:authorized-token-list")
    model = get_access_token_model()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)



## ... source file continues with no further DeleteView examples...

```

