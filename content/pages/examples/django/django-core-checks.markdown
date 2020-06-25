title: django.core checks code examples
category: page
slug: django-core-checks-examples
sortorder: 500011079
toc: False
sidebartitle: django.core checks
meta: Python example code for the checks function from the django.core module of the Django project.


checks is a function within the django.core module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / tests / test_apphooks.py**](https://github.com/divio/django-cms/blob/develop/cms/tests/test_apphooks.py)

```python
# test_apphooks.py
import sys
import mock

from django.contrib.admin.models import CHANGE, LogEntry
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
~~from django.core import checks
from django.core.cache import cache
from django.core.checks.urls import check_url_config
from django.test.utils import override_settings
from django.urls import NoReverseMatch, clear_url_caches, resolve, reverse
from django.utils.timezone import now
from django.utils.translation import override as force_language

from six import string_types

from cms.admin.forms import AdvancedSettingsForm
from cms.api import create_page, create_title
from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from cms.appresolver import applications_page_check, clear_app_resolvers, get_app_patterns
from cms.constants import PUBLISHER_STATE_DIRTY
from cms.models import Title, Page
from cms.middleware.page import get_page
from cms.test_utils.project.placeholderapp.models import Example1
from cms.test_utils.testcases import CMSTestCase
from cms.tests.test_menu_utils import DumbPageLanguageUrl
from cms.toolbar.toolbar import CMSToolbar
from cms.utils.conf import get_cms_setting
from cms.utils.urlutils import admin_reverse
from menus.menu_pool import menu_pool


## ... source file abbreviated to get to checks examples ...


        create_title("de", "aphooked-page-de", page)
        self.assertTrue(page.publish('en'))
        self.assertTrue(page.publish('de'))
        self.assertTrue(blank_page.publish('en'))
        with force_language("en"):
            response = self.client.get(self.get_pages_root())
        self.assertTemplateUsed(response, 'sampleapp/home.html')
        self.assertContains(response, '<--noplaceholder-->')
        response = self.client.get('/en/blankapp/')
        self.assertTemplateUsed(response, 'nav_playground.html')

        self.apphook_clear()

    @override_settings(ROOT_URLCONF='cms.test_utils.project.urls_for_apphook_tests')
    def test_apphook_does_not_crash_django_checks(self):
        self.apphook_clear()
        superuser = get_user_model().objects.create_superuser('admin', 'admin@admin.com', 'admin')
        create_page("apphooked-page", "nav_playground.html", "en",
                    created_by=superuser, published=True, apphook="SampleApp")
        self.reload_urls()
~~        checks.run_checks()
        self.apphook_clear()

    @override_settings(ROOT_URLCONF='cms.test_utils.project.urls_for_apphook_tests')
    def test_apphook_on_root_reverse(self):
        self.apphook_clear()
        superuser = get_user_model().objects.create_superuser('admin', 'admin@admin.com', 'admin')
        page = create_page("apphooked-page", "nav_playground.html", "en",
                           created_by=superuser, published=True, apphook="SampleApp")
        create_title("de", "aphooked-page-de", page)
        self.assertTrue(page.publish('de'))
        self.assertTrue(page.publish('en'))

        self.reload_urls()

        self.assertFalse(reverse('sample-settings').startswith('//'))
        self.apphook_clear()

    @override_settings(ROOT_URLCONF='cms.test_utils.project.urls_for_apphook_tests')
    def test_multisite_apphooks(self):
        self.apphook_clear()
        site1, _ = Site.objects.get_or_create(pk=1)
        site2, _ = Site.objects.get_or_create(pk=2)
        superuser = get_user_model().objects.create_superuser('admin', 'admin@admin.com', 'admin')
        home_site_1 = create_page(


## ... source file continues with no further checks examples...

```


## Example 2 from django-cors-headers
[django-cors-headers](https://github.com/ottoyiu/django-cors-headers)
is an
[open source](https://github.com/ottoyiu/django-cors-headers/blob/master/LICENSE)
library for enabling
[Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
handling in your [Django](/django.html) web applications and appropriately
dealing with HTTP headers for CORS requests.

[**django-cors-headers / src/corsheaders / checks.py**](https://github.com/ottoyiu/django-cors-headers/blob/master/src/corsheaders/./checks.py)

```python
# checks.py
import re
from collections.abc import Sequence
from numbers import Integral
from urllib.parse import urlparse

from django.conf import settings
~~from django.core import checks

from corsheaders.conf import conf

re_type = type(re.compile(""))


@checks.register
def check_settings(app_configs, **kwargs):
    errors = []

    if not is_sequence(conf.CORS_ALLOW_HEADERS, str):
        errors.append(
~~            checks.Error(
                "CORS_ALLOW_HEADERS should be a sequence of strings.",
                id="corsheaders.E001",
            )
        )

    if not is_sequence(conf.CORS_ALLOW_METHODS, str):
        errors.append(
~~            checks.Error(
                "CORS_ALLOW_METHODS should be a sequence of strings.",
                id="corsheaders.E002",
            )
        )

    if not isinstance(conf.CORS_ALLOW_CREDENTIALS, bool):
        errors.append(
~~            checks.Error(
                "CORS_ALLOW_CREDENTIALS should be a bool.", id="corsheaders.E003"
            )
        )

    if (
        not isinstance(conf.CORS_PREFLIGHT_MAX_AGE, Integral)
        or conf.CORS_PREFLIGHT_MAX_AGE < 0
    ):
        errors.append(
~~            checks.Error(
                (
                    "CORS_PREFLIGHT_MAX_AGE should be an integer greater than "
                    + "or equal to zero."
                ),
                id="corsheaders.E004",
            )
        )

    if not isinstance(conf.CORS_ORIGIN_ALLOW_ALL, bool):
        errors.append(
~~            checks.Error(
                "CORS_ORIGIN_ALLOW_ALL should be a bool.", id="corsheaders.E005"
            )
        )

    if not is_sequence(conf.CORS_ORIGIN_WHITELIST, str):
        errors.append(
~~            checks.Error(
                "CORS_ORIGIN_WHITELIST should be a sequence of strings.",
                id="corsheaders.E006",
            )
        )
    else:
        special_origin_values = (
            "null",
            "file://",
        )
        for origin in conf.CORS_ORIGIN_WHITELIST:
            if origin in special_origin_values:
                continue
            parsed = urlparse(origin)
            if parsed.scheme == "" or parsed.netloc == "":
                errors.append(
~~                    checks.Error(
                        (
                            "Origin {} in CORS_ORIGIN_WHITELIST is missing "
                            + " scheme or netloc"
                        ).format(repr(origin)),
                        id="corsheaders.E013",
                        hint=(
                            "Add a scheme (e.g. https://) or netloc (e.g. "
                            + "example.com)."
                        ),
                    )
                )
            else:
                for part in ("path", "params", "query", "fragment"):
                    if getattr(parsed, part) != "":
                        errors.append(
~~                            checks.Error(
                                (
                                    "Origin {} in CORS_ORIGIN_WHITELIST should "
                                    + "not have {}"
                                ).format(repr(origin), part),
                                id="corsheaders.E014",
                            )
                        )

    if not is_sequence(conf.CORS_ORIGIN_REGEX_WHITELIST, (str, re_type)):
        errors.append(
~~            checks.Error(
                (
                    "CORS_ORIGIN_REGEX_WHITELIST should be a sequence of "
                    + "strings and/or compiled regexes."
                ),
                id="corsheaders.E007",
            )
        )

    if not is_sequence(conf.CORS_EXPOSE_HEADERS, str):
        errors.append(
~~            checks.Error(
                "CORS_EXPOSE_HEADERS should be a sequence.", id="corsheaders.E008"
            )
        )

    if not isinstance(conf.CORS_URLS_REGEX, (str, re_type)):
        errors.append(
~~            checks.Error(
                "CORS_URLS_REGEX should be a string or regex.", id="corsheaders.E009"
            )
        )

    if not isinstance(conf.CORS_REPLACE_HTTPS_REFERER, bool):
        errors.append(
~~            checks.Error(
                "CORS_REPLACE_HTTPS_REFERER should be a bool.", id="corsheaders.E011"
            )
        )

    if hasattr(settings, "CORS_MODEL"):
        errors.append(
~~            checks.Error(
                (
                    "The CORS_MODEL setting has been removed - see "
                    + "django-cors-headers' HISTORY."
                ),
                id="corsheaders.E012",
            )
        )

    return errors


def is_sequence(thing, type_or_types):
    return isinstance(thing, Sequence) and all(
        isinstance(x, type_or_types) for x in thing
    )



## ... source file continues with no further checks examples...

```


## Example 3 from wagtail
[wagtail](https://github.com/wagtail/wagtail)
([project website](https://wagtail.io/)) is a fantastic
[Django](/django.html)-based CMS with code that is open source
under the
[BSD 3-Clause "New" or "Revised" License](https://github.com/wagtail/wagtail/blob/master/LICENSE).

[**wagtail / wagtail / snippets / tests.py**](https://github.com/wagtail/wagtail/blob/master/wagtail/snippets/tests.py)

```python
# tests.py
import json

from django.contrib.admin.utils import quote
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser, Permission
~~from django.core import checks
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.http import HttpRequest, HttpResponse
from django.test import RequestFactory, TestCase
from django.test.utils import override_settings
from django.urls import reverse
from taggit.models import Tag

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.admin.forms import WagtailAdminModelForm
from wagtail.core.models import Page
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import SNIPPET_MODELS, register_snippet
from wagtail.snippets.views.snippets import get_snippet_edit_handler
from wagtail.tests.snippets.forms import FancySnippetForm
from wagtail.tests.snippets.models import (
    AlphaSnippet, FancySnippet, FileUploadSnippet, RegisterDecorator, RegisterFunction,
    SearchableSnippet, StandardSnippet, StandardSnippetWithCustomPrimaryKey, ZuluSnippet)
from wagtail.tests.testapp.models import (
    Advert, AdvertWithCustomPrimaryKey, AdvertWithCustomUUIDPrimaryKey, AdvertWithTabbedInterface,
    SnippetChooserModel, SnippetChooserModelWithCustomPrimaryKey)
from wagtail.tests.utils import WagtailTestUtils


## ... source file abbreviated to get to checks examples ...


    def setUp(self):
        self.login()

    def get(self, pk, params=None):
        return self.client.get(reverse('wagtailsnippets:chosen',
                                       args=('tests', 'advertwithcustomuuidprimarykey', quote(pk))),
                               params or {})

    def test_choose_a_page(self):
        response = self.get(pk=AdvertWithCustomUUIDPrimaryKey.objects.all()[0].pk)
        response_json = json.loads(response.content.decode())
        self.assertEqual(response_json['step'], 'chosen')


class TestPanelConfigurationChecks(TestCase, WagtailTestUtils):

    def setUp(self):
        self.warning_id = 'wagtailadmin.W002'

        def get_checks_result():
~~            checks_result = checks.run_checks(tags=['panels'])
            return [
                warning for warning in
                checks_result if warning.id == self.warning_id]

        self.get_checks_result = get_checks_result

    def test_model_with_single_tabbed_panel_only(self):

        StandardSnippet.content_panels = [FieldPanel('text')]

~~        warning = checks.Warning(
            "StandardSnippet.content_panels will have no effect on snippets editing",
            hint="""Ensure that StandardSnippet uses `panels` instead of `content_panels`\
or set up an `edit_handler` if you want a tabbed editing interface.
There are no default tabs on non-Page models so there will be no\
 Content tab for the content_panels to render in.""",
            obj=StandardSnippet,
            id='wagtailadmin.W002',
        )

        checks_results = self.get_checks_result()

        self.assertEqual([warning], checks_results)

        delattr(StandardSnippet, 'content_panels')



## ... source file continues with no further checks examples...

```

