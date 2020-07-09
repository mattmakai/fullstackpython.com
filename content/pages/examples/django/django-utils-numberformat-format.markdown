title: django.utils.numberformat format Example Code
category: page
slug: django-utils-numberformat-format-examples
sortorder: 500011483
toc: False
sidebartitle: django.utils.numberformat format
meta: Python example code for the format callable from the django.utils.numberformat module of the Django project.


format is a callable within the django.utils.numberformat module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / tests / test_placeholder.py**](https://github.com/divio/django-cms/blob/develop/cms/tests/test_placeholder.py)

```python
# test_placeholder.py
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.core.exceptions import ImproperlyConfigured
from django.template import TemplateSyntaxError, Template
from django.template.loader import get_template
from django.test import TestCase
from django.test.utils import override_settings
from django.utils.encoding import force_text
~~from django.utils.numberformat import format
from sekizai.context import SekizaiContext

from cms import constants
from cms.api import add_plugin, create_page, create_title
from cms.exceptions import DuplicatePlaceholderWarning
from cms.models.fields import PlaceholderField
from cms.models.placeholdermodel import Placeholder
from cms.models.pluginmodel import CMSPlugin
from cms.plugin_pool import plugin_pool
from cms.tests.test_toolbar import ToolbarTestBase
from cms.test_utils.fixtures.fakemlng import FakemlngFixtures
from cms.test_utils.project.fakemlng.models import Translations
from cms.test_utils.project.placeholderapp.models import (
    DynamicPlaceholderSlotExample,
    Example1,
    TwoPlaceholderExample,
)
from cms.test_utils.project.sampleapp.models import Category
from cms.test_utils.testcases import CMSTestCase, TransactionCMSTestCase
from cms.test_utils.util.mock import AttributeObject
from cms.toolbar.toolbar import CMSToolbar
from cms.toolbar.utils import get_toolbar_from_request
from cms.utils.compat.tests import UnittestCompatMixin
from cms.utils.conf import get_cms_setting


## ... source file abbreviated to get to format examples ...


            self.assertEqual(plugins[0].plugin_type, 'TextPlugin')
            self.assertEqual(plugins[1].plugin_type, 'LinkPlugin')
            self.assertEqual(plugins[2].plugin_type, 'LinkPlugin')
            self.assertTrue(plugins[1].parent == plugins[2].parent and plugins[1].parent == plugins[0])

    def test_placeholder_pk_thousands_format(self):
        page = create_page("page", "nav_playground.html", "en", published=True)
        for placeholder in page.placeholders.all():
            page.placeholders.remove(placeholder)
            placeholder.pk += 1000
            placeholder.save()
            page.placeholders.add(placeholder)
        page.reload()
        for placeholder in page.placeholders.all():
            add_plugin(placeholder, "TextPlugin", "en", body="body")
        with self.settings(USE_THOUSAND_SEPARATOR=True, USE_L10N=True):
            user = self.get_superuser()
            self.client.login(username=getattr(user, get_user_model().USERNAME_FIELD),
                              password=getattr(user, get_user_model().USERNAME_FIELD))
            endpoint = page.get_absolute_url() + '?' + get_cms_setting('CMS_TOOLBAR_URL__EDIT_ON')
            response = self.client.get(endpoint)
            for placeholder in page.placeholders.all():
                self.assertContains(
                    response, '"placeholder_id": "%s"' % placeholder.pk)
                self.assertNotContains(
~~                    response, '"placeholder_id": "%s"' % format(
                        placeholder.pk, ".", grouping=3, thousand_sep=","))
                self.assertNotContains(
~~                    response, '"plugin_id": "%s"' % format(
                        placeholder.pk, ".", grouping=3, thousand_sep=","))
                self.assertNotContains(
~~                    response, '"clipboard": "%s"' % format(
                        response.context['request'].toolbar.clipboard.pk, ".",
                        grouping=3, thousand_sep=","))

    def test_placeholder_languages_model(self):
        avail_langs = set([u'en', u'de', u'fr'])
        ex = Example1(
            char_1='one',
            char_2='two',
            char_3='tree',
            char_4='four'
        )
        ex.save()
        for lang in avail_langs:
            add_plugin(ex.placeholder, u"EmptyPlugin", lang)
        ex = Example1.objects.get(pk=ex.pk)
        langs = [lang['code'] for lang in ex.placeholder.get_filled_languages()]
        self.assertEqual(avail_langs, set(langs))

    def test_placeholder_languages_page(self):
        avail_langs = set([u'en', u'de', u'fr'])
        page = create_page('test page', 'col_two.html', u'en')
        for lang in avail_langs:
            if lang != u'en':
                create_title(lang, 'test page %s' % lang, page)


## ... source file continues with no further format examples...

```

