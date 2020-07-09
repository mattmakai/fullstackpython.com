title: django.utils.http is_safe_url Example Code
category: page
slug: django-utils-http-is-safe-url-examples
sortorder: 500011472
toc: False
sidebartitle: django.utils.http is_safe_url
meta: Python example code for the is_safe_url callable from the django.utils.http module of the Django project.


is_safe_url is a callable within the django.utils.http module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / views.py**](https://github.com/divio/django-cms/blob/develop/cms/./views.py)

```python
# views.py

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login
from django.contrib.auth.views import redirect_to_login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.cache import patch_cache_control
~~from django.utils.http import is_safe_url, urlquote
from django.utils.timezone import now
from django.utils.translation import get_language_from_request
from django.views.decorators.http import require_POST

from cms.cache.page import get_page_cache
from cms.exceptions import LanguageError
from cms.forms.login import CMSToolbarLoginForm
from cms.models.pagemodel import TreeNode
from cms.page_rendering import _handle_no_page, render_page, render_object_structure, _render_welcome_page
from cms.toolbar.utils import get_toolbar_from_request
from cms.utils import get_current_site
from cms.utils.conf import get_cms_setting
from cms.utils.i18n import (get_fallback_languages, get_public_languages,
                            get_redirect_on_fallback, get_language_list,
                            get_default_language_for_site,
                            is_language_prefix_patterns_used)
from cms.utils.page import get_page_from_request
from cms.utils.page_permissions import user_can_change_page


def _clean_redirect_url(redirect_url, language):
    if (redirect_url and is_language_prefix_patterns_used() and redirect_url[0] == "/"
            and not redirect_url.startswith('/%s/' % language)):
        redirect_url = "/%s/%s" % (language, redirect_url.lstrip("/"))


## ... source file abbreviated to get to is_safe_url examples ...


        redirect_url = _clean_redirect_url(redirect_url, request_language)

    if redirect_url:
        if request.user.is_staff and toolbar.edit_mode_active:
            toolbar.redirect_url = redirect_url
        elif redirect_url not in own_urls:
            return HttpResponseRedirect(redirect_url)

    if page.login_required and not request.user.is_authenticated:
        return redirect_to_login(urlquote(request.get_full_path()), settings.LOGIN_URL)

    if hasattr(request, 'toolbar'):
        request.toolbar.set_object(page)

    structure_requested = get_cms_setting('CMS_TOOLBAR_URL__BUILD') in request.GET

    if user_can_change_page(request.user, page) and structure_requested:
        return render_object_structure(request, page)
    return render_page(request, page, current_language=request_language, slug=slug)


@require_POST
def login(request):
    redirect_to = request.GET.get(REDIRECT_FIELD_NAME)

~~    if not is_safe_url(url=redirect_to, allowed_hosts=request.get_host()):
        redirect_to = reverse("pages-root")

    if request.user.is_authenticated:
        return HttpResponseRedirect(redirect_to)

    form = CMSToolbarLoginForm(request=request, data=request.POST)

    if form.is_valid():
        auth_login(request, form.user_cache)
    else:
        redirect_to += u'?cms_toolbar_login_error=1'
    return HttpResponseRedirect(redirect_to)



## ... source file continues with no further is_safe_url examples...

```

