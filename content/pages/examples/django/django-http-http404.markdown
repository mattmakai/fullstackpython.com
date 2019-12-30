title: django.http Http404 Python Code Examples
category: page
slug: django-http-http404-examples
sortorder: 500013410
toc: False
sidebartitle: django.http Http404
meta: Example code for the Http404 Exception class from the django.http module.


[Http404](https://docs.djangoproject.com/en/dev/topics/http/views/#the-http404-exception)
([source code](https://github.com/django/django/blob/master/django/http/response.py))
is a [Django](/django.html) convenience exception class that returns 
your application's standard error page and an 
[HTTP 404](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) status
code.

Note that while Http404 is typically imported from `django.http`, the
source code for the exception lives under `django.http.responses`.


## Example 1 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a 
[Django](/django.html)-based content management system (CMS) with 
open source code provided under the 
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / core / models.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/core/models.py)

```python
import json
import logging
from collections import defaultdict
from io import StringIO
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core import checks
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.handlers.base import BaseHandler
from django.core.handlers.wsgi import WSGIRequest
from django.db import models, transaction
from django.db.models import Case, Q, Value, When
from django.db.models.functions import Concat, Substr
~~from django.http import Http404
from django.template.response import TemplateResponse
from django.urls import reverse
from django.utils import timezone
from django.utils.functional import cached_property
from django.utils.text import capfirst, slugify
from django.utils.translation import ugettext_lazy as _

## ... code is abbreviated here due to the long file length ...


    def route(self, request, path_components):
        if path_components:
            # request is for a child of this page
            child_slug = path_components[0]
            remaining_components = path_components[1:]

~~            try:
~~                subpage = self.get_children().get(slug=child_slug)
~~            except Page.DoesNotExist:
~~                raise Http404

            return subpage.specific.route(request, remaining_components)

~~        else:
~~            # request is for this very page
~~            if self.live:
~~                return RouteResult(self)
~~            else:
~~                raise Http404

```
