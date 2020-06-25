title: django.core mail code examples
category: page
slug: django-core-mail-examples
sortorder: 500011081
toc: False
sidebartitle: django.core mail
meta: Python example code for the mail function from the django.core module of the Django project.


mail is a function within the django.core module of the Django project.


## Example 1 from django-allauth
[django-allauth](https://github.com/pennersr/django-allauth)
([project website](https://www.intenct.nl/projects/django-allauth/)) is a
[Django](/django.html) library for easily adding local and social authentication
flows to Django projects. It is open source under the
[MIT License](https://github.com/pennersr/django-allauth/blob/master/LICENSE).
         

[**django-allauth / allauth / account / tests.py**](https://github.com/pennersr/django-allauth/blob/master/allauth/account/tests.py)

```python
# tests.py
from __future__ import absolute_import

import json
import uuid
from datetime import timedelta

from django import forms
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.contrib.sites.models import Site
~~from django.core import mail, validators
from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpResponseRedirect
from django.template import Context, Template
from django.test.client import Client, RequestFactory
from django.test.utils import override_settings
from django.urls import reverse
from django.utils.timezone import now

from allauth.account.forms import BaseSignupForm, ResetPasswordForm, SignupForm
from allauth.account.models import (
    EmailAddress,
    EmailConfirmation,
    EmailConfirmationHMAC,
)
from allauth.tests import Mock, TestCase, patch
from allauth.utils import get_user_model, get_username_max_length

from . import app_settings
from .adapter import get_adapter
from .auth_backends import AuthenticationBackend
from .signals import user_logged_in, user_logged_out
from .utils import (
    filter_users_by_username,


## ... source file abbreviated to get to mail examples ...



    def _password_set_or_change_redirect(self, urlname, usable_password):
        self._create_user_and_login(usable_password)
        return self.client.get(reverse(urlname))

    def test_ajax_password_change(self):
        self._create_user_and_login()
        resp = self.client.post(
            reverse('account_change_password'),
            data={'oldpassword': 'doe',
                  'password1': 'AbCdEf!123',
                  'password2': 'AbCdEf!123456'},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(resp['content-type'], 'application/json')
        data = json.loads(resp.content.decode('utf8'))
        assert ('same password' in
                data['form']['fields']['password2']['errors'][0])

    def test_password_forgotten_username_hint(self):
        user = self._request_new_password()
~~        body = mail.outbox[0].body
        assert user.username in body

    @override_settings(
        ACCOUNT_AUTHENTICATION_METHOD=app_settings.AuthenticationMethod.EMAIL)
    def test_password_forgotten_no_username_hint(self):
        user = self._request_new_password()
~~        body = mail.outbox[0].body
        assert user.username not in body

    def _request_new_password(self):
        user = get_user_model().objects.create(
            username='john', email="john@example.org", is_active=True)
        user.set_password('doe')
        user.save()
        self.client.post(
            reverse('account_reset_password'),
            data={'email': 'john@example.org'})
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, ["john@example.org"])
        return user

    def test_password_reset_flow_with_empty_session(self):
        self._request_new_password()
~~        body = mail.outbox[0].body
        self.assertGreater(body.find('https://'), 0)

        url = body[body.find('/password/reset/'):].split()[0]
        resp = self.client.get(url)

        reset_pass_url = resp.url

        resp = self.client_class().get(reset_pass_url)

        self.assertTemplateUsed(
            resp,
            'account/password_reset_from_key.%s' %
            app_settings.TEMPLATE_EXTENSION)

        self.assertTrue(resp.context_data['token_fail'])

    def test_password_reset_flow(self):
        user = self._request_new_password()
~~        body = mail.outbox[0].body
        self.assertGreater(body.find('https://'), 0)

        url = body[body.find('/password/reset/'):].split()[0]
        resp = self.client.get(url)
        url = resp.url
        resp = self.client.get(url)
        self.assertTemplateUsed(
            resp,
            'account/password_reset_from_key.%s' %
            app_settings.TEMPLATE_EXTENSION)
        self.assertFalse('token_fail' in resp.context_data)

        resp = self.client.post(url,
                                {'password1': 'newpass123',
                                 'password2': 'newpass123'})
        self.assertRedirects(resp,
                             reverse('account_reset_password_from_key_done'))

        user = get_user_model().objects.get(pk=user.pk)
        self.assertTrue(user.check_password('newpass123'))

        resp = self.client.post(url,
                                {'password1': 'newpass123',
                                 'password2': 'newpass123'})


## ... source file abbreviated to get to mail examples ...


            app_settings.TEMPLATE_EXTENSION)
        self.assertTrue(resp.context_data['token_fail'])

        response = self.client.get(url)
        self.assertTemplateUsed(
            response,
            'account/password_reset_from_key.%s' %
            app_settings.TEMPLATE_EXTENSION)
        self.assertTrue(response.context_data['token_fail'])

        response = self.client.post(url,
                                    {'password1': 'newpass123',
                                     'password2': 'newpass123'},
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.content.decode('utf8'))
        assert 'invalid' in data['form']['errors'][0]

    def test_password_reset_flow_with_email_changed(self):
        user = self._request_new_password()
~~        body = mail.outbox[0].body
        self.assertGreater(body.find('https://'), 0)
        EmailAddress.objects.create(
            user=user,
            email='other@email.org')
        url = body[body.find('/password/reset/'):].split()[0]
        resp = self.client.get(url)
        self.assertTemplateUsed(
            resp,
            'account/password_reset_from_key.%s' %
            app_settings.TEMPLATE_EXTENSION)
        self.assertTrue('token_fail' in resp.context_data)

    @override_settings(ACCOUNT_LOGIN_ON_PASSWORD_RESET=True)
    def test_password_reset_ACCOUNT_LOGIN_ON_PASSWORD_RESET(self):
        user = self._request_new_password()
~~        body = mail.outbox[0].body
        url = body[body.find('/password/reset/'):].split()[0]
        resp = self.client.get(url)
        resp = self.client.post(
            resp.url,
            {'password1': 'newpass123',
             'password2': 'newpass123'})
        self.assertTrue(user.is_authenticated)
        self.assertRedirects(resp, '/confirm-email/')

    @override_settings(ACCOUNT_EMAIL_CONFIRMATION_HMAC=False)
    def test_email_verification_mandatory(self):
        c = Client()
        resp = c.post(reverse('account_signup'),
                      {'username': 'johndoe',
                       'email': 'john@example.com',
                       'password1': 'johndoe',
                       'password2': 'johndoe'},
                      follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(mail.outbox[0].to, ['john@example.com'])
        self.assertGreater(mail.outbox[0].body.find('https://'), 0)
        self.assertEqual(len(mail.outbox), 1)
        self.assertTemplateUsed(
            resp,


## ... source file continues with no further mail examples...

```


## Example 2 from django-cms
[django-cms](https://github.com/divio/django-cms)
([project website](https://www.django-cms.org/en/)) is a Python-based
content management system (CMS) [library](https://pypi.org/project/django-cms/)
for use with Django web apps that is open sourced under the
[BSD 3-Clause "New"](https://github.com/divio/django-cms/blob/develop/LICENSE)
license.

[**django-cms / cms / tests / test_mail.py**](https://github.com/divio/django-cms/blob/develop/cms/tests/test_mail.py)

```python
# test_mail.py
from django.contrib.auth import get_user_model
~~from django.core import mail

from cms.api import create_page_user
from cms.test_utils.testcases import CMSTestCase
from cms.utils.mail import mail_page_user_change


class MailTestCase(CMSTestCase):
    def setUp(self):
~~        mail.outbox = [] # reset outbox

    def test_mail_page_user_change(self):
        user = get_user_model().objects.create_superuser("username", "username@django-cms.org", "username")
        user = create_page_user(user, user, grant_all=True)
        mail_page_user_change(user)
        self.assertEqual(len(mail.outbox), 1)



## ... source file continues with no further mail examples...

```


## Example 3 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / tests / test_tasks.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/tests/test_tasks.py)

```python
# test_tasks.py
from django.test import TestCase
from explorer.app_settings import EXPLORER_DEFAULT_CONNECTION as CONN
from explorer.tasks import execute_query, snapshot_queries, truncate_querylogs, build_schema_cache_async
from explorer.tests.factories import SimpleQueryFactory
~~from django.core import mail
from mock import Mock, patch
from six import StringIO
from explorer.models import QueryLog
from datetime import datetime, timedelta


class TestTasks(TestCase):

    @patch('explorer.tasks.s3_upload')
    def test_async_results(self, mocked_upload):
        mocked_upload.return_value = 'http://s3.com/your-file.csv'

        q = SimpleQueryFactory(sql='select 1 "a", 2 "b", 3 "c";', title="testquery")
        execute_query(q.id, 'cc@epantry.com')

        output = StringIO()
        output.write('a,b,c\r\n1,2,3\r\n')

        self.assertEqual(len(mail.outbox), 2)
~~        self.assertIn('[SQL Explorer] Your query is running', mail.outbox[0].subject)
~~        self.assertIn('[SQL Explorer] Report ', mail.outbox[1].subject)
        self.assertEqual(mocked_upload.call_args[0][1].getvalue(), output.getvalue())
        self.assertEqual(mocked_upload.call_count, 1)

    @patch('explorer.tasks.s3_upload')
    def test_async_results_fails_with_message(self, mocked_upload):
        mocked_upload.return_value = 'http://s3.com/your-file.csv'

        q = SimpleQueryFactory(sql='select x from foo;', title="testquery")
        execute_query(q.id, 'cc@epantry.com')

        output = StringIO()
        output.write('a,b,c\r\n1,2,3\r\n')

        self.assertEqual(len(mail.outbox), 2)
~~        self.assertIn('[SQL Explorer] Error ', mail.outbox[1].subject)
        self.assertEqual(mocked_upload.call_count, 0)

    @patch('explorer.tasks.s3_upload')
    def test_snapshots(self, mocked_upload):
        mocked_upload.return_value = 'http://s3.com/your-file.csv'

        SimpleQueryFactory(snapshot=True)
        SimpleQueryFactory(snapshot=True)
        SimpleQueryFactory(snapshot=True)
        SimpleQueryFactory(snapshot=False)

        snapshot_queries()
        self.assertEqual(mocked_upload.call_count, 3)

    def test_truncating_querylogs(self):
        QueryLog(sql='foo').save()
        QueryLog.objects.filter(sql='foo').update(run_at=datetime.now() - timedelta(days=30))
        QueryLog(sql='bar').save()
        QueryLog.objects.filter(sql='bar').update(run_at=datetime.now() - timedelta(days=29))
        truncate_querylogs(30)
        self.assertEqual(QueryLog.objects.count(), 1)

    @patch('explorer.schema.build_schema_info')
    def test_build_schema_cache_async(self, mocked_build):


## ... source file continues with no further mail examples...

```

