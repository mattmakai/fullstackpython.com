title: django.template.base Template Example Code
category: page
slug: django-template-base-template-examples
sortorder: 500011368
toc: False
sidebartitle: django.template.base Template
meta: Python example code for the Template class from the django.template.base module of the Django project.


Template is a class within the django.template.base module of the Django project.


## Example 1 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / tests / test_static_placeholder.py**](https://github.com/divio/django-cms/blob/develop/cms/tests/test_static_placeholder.py)

```python
# test_static_placeholder.py

from django.contrib.admin.sites import site
from django.template import Context
~~from django.template.base import Template

from six import text_type

from cms.api import add_plugin
from cms.models import StaticPlaceholder, Placeholder, UserSettings
from cms.tests.test_plugins import PluginsTestBaseCase
from cms.utils.urlutils import admin_reverse


class StaticPlaceholderTestCase(PluginsTestBaseCase):
    @property
    def admin_class(self):
        return site._registry[StaticPlaceholder]

    def fill_placeholder(self, placeholder=None):
        if placeholder is None:
            placeholder = Placeholder(slot=u"some_slot")
            placeholder.save()  # a good idea, if not strictly necessary


        plugin_1 = add_plugin(placeholder, u"TextPlugin", u"en",
                              body=u"01",
        )
        plugin_1.save()


        plugin_2 = add_plugin(placeholder, u"TextPlugin", u"en",
                              body=u"02",
        )
        plugin_1 = self.reload(plugin_1)
        plugin_2.parent = plugin_1
        plugin_2.save()
        return placeholder

    def get_admin(self):
        usr = self._create_user("admin", True, True)
        return usr

    def test_template_creation(self):
        self.assertObjectDoesNotExist(StaticPlaceholder.objects.all(), code='foobar')
        self.assertObjectDoesNotExist(Placeholder.objects.all(), slot='foobar')
~~        t = Template('{% load cms_tags %}{% static_placeholder "foobar" %}')
        t.render(self.get_context('/'))
        self.assertObjectExist(StaticPlaceholder.objects.all(), code='foobar',
                               creation_method=StaticPlaceholder.CREATION_BY_TEMPLATE)
        self.assertEqual(Placeholder.objects.filter(slot='foobar').count(), 2)

    def test_empty(self):
        self.assertObjectDoesNotExist(StaticPlaceholder.objects.all(), code='foobar')
        self.assertObjectDoesNotExist(Placeholder.objects.all(), slot='foobar')
~~        t = Template('{% load cms_tags %}{% static_placeholder "foobar" or %}No Content{% endstatic_placeholder %}')
        rendered = t.render(self.get_context('/'))
        self.assertIn("No Content", rendered)

~~        t = Template('{% load cms_tags %}{% static_placeholder "" %}')
        rendered = t.render(self.get_context('/'))
        self.assertEqual("", rendered)

~~        t = Template('{% load cms_tags %}{% static_placeholder code or %}No Content{% endstatic_placeholder %}')
        rendered = t.render(Context({'code': StaticPlaceholder.objects.all()[0]}))
        self.assertIn("No Content", rendered)

        for p in Placeholder.objects.all():
            add_plugin(p, 'TextPlugin', 'en', body='test')
~~        t = Template('{% load cms_tags %}{% static_placeholder "foobar" or %}No Content{% endstatic_placeholder %}')
        rendered = t.render(self.get_context('/'))
        self.assertNotIn("No Content", rendered)
        self.assertEqual(StaticPlaceholder.objects.filter(site_id__isnull=True, code='foobar').count(), 1)

    def test_local(self):
        self.assertObjectDoesNotExist(StaticPlaceholder.objects.all(), code='foobar')
        self.assertObjectDoesNotExist(Placeholder.objects.all(), slot='foobar')
~~        t = Template('{% load cms_tags %}{% static_placeholder "foobar" site or %}No Content{% endstatic_placeholder %}')
        rendered = t.render(self.get_context('/'))
        self.assertIn("No Content", rendered)
        for p in Placeholder.objects.all():
            add_plugin(p, 'TextPlugin', 'en', body='test')
        rendered = t.render(self.get_context('/'))
        self.assertNotIn("No Content", rendered)
        self.assertEqual(StaticPlaceholder.objects.filter(site_id__isnull=False, code='foobar').count(), 1)

    def test_publish_stack(self):
        static_placeholder = StaticPlaceholder.objects.create(name='foo', code='bar', site_id=1)
        self.fill_placeholder(static_placeholder.draft)
        static_placeholder.dirty = True
        static_placeholder.save()
        self.assertEqual(static_placeholder.draft.cmsplugin_set.all().count(), 2)
        self.assertEqual(static_placeholder.public.cmsplugin_set.all().count(), 0)
        with self.login_user_context(self.get_superuser()):
            response = self.client.post('%s?statics=%s' % (admin_reverse("cms_page_publish_page", args=[1, 'en']), static_placeholder.pk))
            self.assertEqual(response.status_code, 302)

    def test_permissions(self):
        static_placeholder = StaticPlaceholder.objects.create(name='foo', code='bar', site_id=1)
        request = self.get_request()

        request.user = self._create_user('user_a', is_staff=True, is_superuser=False, permissions=['change_staticplaceholder'])


## ... source file continues with no further Template examples...

```

