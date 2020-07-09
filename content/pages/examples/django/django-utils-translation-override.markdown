title: django.utils.translation override Example Code
category: page
slug: django-utils-translation-override-examples
sortorder: 500011506
toc: False
sidebartitle: django.utils.translation override
meta: Python example code for the override callable from the django.utils.translation module of the Django project.


override is a callable within the django.utils.translation module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / appresolver.py**](https://github.com/divio/django-cms/blob/develop/cms/./appresolver.py)

```python
# appresolver.py
from collections import OrderedDict
from importlib import import_module

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.db import OperationalError, ProgrammingError
~~from django.utils.translation import get_language, override
from django.urls import Resolver404, reverse

from six import string_types

from cms.apphook_pool import apphook_pool
from cms.models.pagemodel import Page
from cms.utils import get_current_site
from cms.utils.compat import DJANGO_1_11
from cms.utils.compat.dj import RegexPattern, URLPattern, URLResolver
from cms.utils.i18n import get_language_list
from cms.utils.moderator import use_draft


APP_RESOLVERS = []


def clear_app_resolvers():
    global APP_RESOLVERS
    APP_RESOLVERS = []


def applications_page_check(request, current_page=None, path=None):
    if current_page:
        return current_page


## ... source file abbreviated to get to override examples ...


    from cms.models import Title

    included = []

    title_qs = Title.objects.public().filter(page__node__site=site)

    hooked_applications = OrderedDict()

    titles = (title_qs.exclude(page__application_urls=None)
              .exclude(page__application_urls='')
              .order_by('-page__node__path').select_related())
    for title in titles:
        path = title.path
        mix_id = "%s:%s:%s" % (
            path + "/", title.page.application_urls, title.language)
        if mix_id in included:
            continue
        if not settings.APPEND_SLASH:
            path += '/'
        app = apphook_pool.get_apphook(title.page.application_urls)
        if not app:
            continue
        if title.page_id not in hooked_applications:
            hooked_applications[title.page_id] = {}
        app_ns = app.app_name, title.page.application_namespace
~~        with override(title.language):
            hooked_applications[title.page_id][title.language] = (
                app_ns, get_patterns_for_title(path, title), app)
        included.append(mix_id)
    app_patterns = []
    for page_id in hooked_applications.keys():
        resolver = None
        for lang in hooked_applications[page_id].keys():
            (app_ns, inst_ns), current_patterns, app = hooked_applications[page_id][lang]  # nopyflakes
            if not resolver:
                regex_pattern = RegexPattern(r'') if not DJANGO_1_11 else r''
                resolver = AppRegexURLResolver(
                    regex_pattern, 'app_resolver', app_name=app_ns, namespace=inst_ns)
                resolver.page_id = page_id
            if app.permissions:
                _set_permissions(current_patterns, app.exclude_permissions)

            resolver.url_patterns_dict[lang] = current_patterns
        app_patterns.append(resolver)
        APP_RESOLVERS.append(resolver)
    return app_patterns



## ... source file continues with no further override examples...

```


## Example 2 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / admin / mail.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/admin/mail.py)

```python
# mail.py
import logging

from django.conf import settings
from django.core.mail import get_connection
from django.core.mail.message import EmailMultiAlternatives
from django.template.loader import render_to_string
~~from django.utils.translation import override

from wagtail.admin.auth import users_with_page_permission
from wagtail.core.models import PageRevision
from wagtail.users.models import UserProfile


logger = logging.getLogger('wagtail.admin')


def send_mail(subject, message, recipient_list, from_email=None, **kwargs):
    if not from_email:
        if hasattr(settings, 'WAGTAILADMIN_NOTIFICATION_FROM_EMAIL'):
            from_email = settings.WAGTAILADMIN_NOTIFICATION_FROM_EMAIL
        elif hasattr(settings, 'DEFAULT_FROM_EMAIL'):
            from_email = settings.DEFAULT_FROM_EMAIL
        else:
            from_email = 'webmaster@localhost'

    connection = kwargs.get('connection', False) or get_connection(
        username=kwargs.get('auth_user', None),
        password=kwargs.get('auth_password', None),
        fail_silently=kwargs.get('fail_silently', None),
    )
    multi_alt_kwargs = {


## ... source file abbreviated to get to override examples ...


    email_recipients = [
        recipient for recipient in recipients
        if recipient.email and recipient.pk != excluded_user_id and getattr(
            UserProfile.get_for_user(recipient),
            notification + '_notifications'
        )
    ]

    if not email_recipients:
        return True

    template_subject = 'wagtailadmin/notifications/' + notification + '_subject.txt'
    template_text = 'wagtailadmin/notifications/' + notification + '.txt'
    template_html = 'wagtailadmin/notifications/' + notification + '.html'

    context = {
        "revision": revision,
        "settings": settings,
    }

    sent_count = 0
    for recipient in email_recipients:
        try:
            context["user"] = recipient

~~            with override(recipient.wagtail_userprofile.get_preferred_language()):
                email_subject = render_to_string(template_subject, context).strip()
                email_content = render_to_string(template_text, context).strip()

            kwargs = {}
            if getattr(settings, 'WAGTAILADMIN_NOTIFICATION_USE_HTML', False):
                kwargs['html_message'] = render_to_string(template_html, context)

            send_mail(email_subject, email_content, [recipient.email], **kwargs)
            sent_count += 1
        except Exception:
            logger.exception(
                "Failed to send notification email '%s' to %s",
                email_subject, recipient.email
            )

    return sent_count == len(email_recipients)



## ... source file continues with no further override examples...

```

