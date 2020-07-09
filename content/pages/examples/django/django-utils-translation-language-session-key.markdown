title: django.utils.translation LANGUAGE_SESSION_KEY Example Code
category: page
slug: django-utils-translation-language-session-key-examples
sortorder: 500011498
toc: False
sidebartitle: django.utils.translation LANGUAGE_SESSION_KEY
meta: Python example code for the LANGUAGE_SESSION_KEY constant from the django.utils.translation module of the Django project.


LANGUAGE_SESSION_KEY is a constant within the django.utils.translation module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / middleware / language.py**](https://github.com/divio/django-cms/blob/develop/cms/middleware/language.py)

```python
# language.py
import datetime

~~from django.utils.translation import LANGUAGE_SESSION_KEY, get_language
from django.conf import settings

from cms.utils.compat import DJANGO_2_2
from cms.utils.compat.dj import MiddlewareMixin


class LanguageCookieMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        language = get_language()
        if hasattr(request, 'session') and DJANGO_2_2:
~~            session_language = request.session.get(LANGUAGE_SESSION_KEY, None)
            if session_language and not session_language == language:
                request.session[LANGUAGE_SESSION_KEY] = language
                request.session.save()
        if settings.LANGUAGE_COOKIE_NAME in request.COOKIES and \
                        request.COOKIES[settings.LANGUAGE_COOKIE_NAME] == language:
            return response
        max_age = 365 * 24 * 60 * 60  # 10 years
        expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language, expires=expires)
        return response



## ... source file continues with no further LANGUAGE_SESSION_KEY examples...

```

