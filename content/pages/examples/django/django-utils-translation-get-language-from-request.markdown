title: django.utils.translation get_language_from_request Example Code
category: page
slug: django-utils-translation-get-language-from-request-examples
sortorder: 500011502
toc: False
sidebartitle: django.utils.translation get_language_from_request
meta: Python example code for the get_language_from_request callable from the django.utils.translation module of the Django project.


get_language_from_request is a callable within the django.utils.translation module of the Django project.


## Example 1 from django-angular
[django-angular](https://github.com/jrief/django-angular)
([project examples website](https://django-angular.awesto.com/classic_form/))
is a library with helper code to make it easier to use
[Angular](/angular.html) as the front-end to [Django](/django.html) projects.
The code for django-angular is
[open source under the MIT license](https://github.com/jrief/django-angular/blob/master/LICENSE.txt).

[**django-angular / djng / templatetags / djng_tags.py**](https://github.com/jrief/django-angular/blob/master/djng/templatetags/djng_tags.py)

```python
# djng_tags.py
import json

from django.template import Library
from django.template.base import Node, NodeList, TextNode, VariableNode
from django.utils.html import format_html
from django.utils.safestring import mark_safe
~~from django.utils.translation import get_language_from_request

from djng.core.urlresolvers import get_all_remote_methods, get_current_remote_methods


register = Library()


@register.simple_tag(name='djng_all_rmi')
def djng_all_rmi():
    return mark_safe(json.dumps(get_all_remote_methods()))


@register.simple_tag(name='djng_current_rmi', takes_context=True)
def djng_current_rmi(context):
    return mark_safe(json.dumps(get_current_remote_methods(context.get('view'))))


@register.simple_tag(name='load_djng_urls', takes_context=True)
def djng_urls(context, *namespaces):
    raise DeprecationWarning(
        "load_djng_urls templatetag is deprecated and has been removed from this version of django-angular."
        "Please refer to documentation for updated way to manage django urls in angular.")




## ... source file abbreviated to get to get_language_from_request examples ...


@register.tag
def angularjs(parser, token):
    bits = token.contents.split()
    if len(bits) < 2:
        bits.append('1')
    values = [parser.compile_filter(bit) for bit in bits[1:]]
    django_nodelist = parser.parse(('endangularjs',))
    angular_nodelist = NodeList()
    for node in django_nodelist:
        if isinstance(node, VariableNode):
            tokens = node.filter_expression.token.split('.')
            token = tokens[0]
            for part in tokens[1:]:
                if part.isdigit():
                    token += '[%s]' % part
                else:
                    token += '.%s' % part
            node = TextNode('{{ %s }}' % token)
        angular_nodelist.append(node)
    parser.delete_first_token()
    return AngularJsNode(django_nodelist, angular_nodelist, values[0])


@register.simple_tag(name='djng_locale_script', takes_context=True)
def djng_locale_script(context, default_language='en'):
~~    language = get_language_from_request(context['request'])
    if not language:
        language = default_language
    return format_html('angular-locale_{}.js', language.lower())



## ... source file continues with no further get_language_from_request examples...

```


## Example 2 from django-cms
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
from django.utils.http import is_safe_url, urlquote
from django.utils.timezone import now
~~from django.utils.translation import get_language_from_request
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
    return redirect_url



## ... source file abbreviated to get to get_language_from_request examples ...


            response.xframe_options_exempt = True
            response._headers = headers
            max_age = int(
                (expires_datetime - response_timestamp).total_seconds() + 0.5)
            patch_cache_control(response, max_age=max_age)
            return response

    site = get_current_site()
    page = get_page_from_request(request, use_path=slug)
    toolbar = get_toolbar_from_request(request)
    tree_nodes = TreeNode.objects.get_for_site(site)

    if not page and not slug and not tree_nodes.exists():
        return _render_welcome_page(request)

    if not page:
        _handle_no_page(request)

    request.current_page = page

    if hasattr(request, 'user') and request.user.is_staff:
        user_languages = get_language_list(site_id=site.pk)
    else:
        user_languages = get_public_languages(site_id=site.pk)

~~    request_language = get_language_from_request(request, check_path=True)

    if not page.is_home and request_language not in user_languages:
        return _handle_no_page(request)

    available_languages = [
        language for language in user_languages
        if language in list(page.get_published_languages())
    ]

    own_urls = [
        request.build_absolute_uri(request.path),
        '/%s' % request.path,
        request.path,
    ]

    try:
        redirect_on_fallback = get_redirect_on_fallback(request_language, site_id=site.pk)
    except LanguageError:
        redirect_on_fallback = False

    if request_language not in user_languages:
        default_language = get_default_language_for_site(site.pk)
        fallbacks = get_fallback_languages(default_language, site_id=site.pk)
        fallbacks = [default_language] + fallbacks


## ... source file continues with no further get_language_from_request examples...

```

