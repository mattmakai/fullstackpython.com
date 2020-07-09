title: django.utils.timezone timedelta Example Code
category: page
slug: django-utils-timezone-timedelta-examples
sortorder: 500011497
toc: False
sidebartitle: django.utils.timezone timedelta
meta: Python example code for the timedelta callable from the django.utils.timezone module of the Django project.


timedelta is a callable within the django.utils.timezone module of the Django project.


## Example 1 from django-axes
[django-axes](https://github.com/jazzband/django-axes/)
([project documentation](https://django-axes.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-axes/)
is a code library for [Django](/django.html) projects to track failed
login attempts against a web application. The goal of the project is
to make it easier for you to stop people and scripts from hacking your
Django-powered website.

The code for django-axes is
[open source under the MIT license](https://github.com/jazzband/django-axes/blob/master/LICENSE)
and maintained by the group of developers known as
[Jazzband](https://jazzband.co/).

[**django-axes / axes / tests / test_handlers.py**](https://github.com/jazzband/django-axes/blob/master/axes/tests/test_handlers.py)

```python
# test_handlers.py
from unittest.mock import MagicMock, patch

from django.test import override_settings
from django.urls import reverse
from django.utils import timezone
~~from django.utils.timezone import timedelta

from axes.conf import settings
from axes.handlers.proxy import AxesProxyHandler
from axes.helpers import get_client_str
from axes.models import AccessAttempt, AccessLog
from axes.tests.base import AxesTestCase


@override_settings(AXES_HANDLER="axes.handlers.base.AxesHandler")
class AxesHandlerTestCase(AxesTestCase):
    def test_base_handler_reset_attempts_raises(self):
        with self.assertRaises(NotImplementedError):
            AxesProxyHandler.reset_attempts()

    def test_base_handler_reset_logs_raises(self):
        with self.assertRaises(NotImplementedError):
            AxesProxyHandler.reset_logs()

    def test_base_handler_raises_on_undefined_is_allowed_to_authenticate(self):
        with self.assertRaises(NotImplementedError):
            AxesProxyHandler.is_allowed(self.request, {})

    @override_settings(AXES_IP_BLACKLIST=["127.0.0.1"])
    def test_is_allowed_with_blacklisted_ip_address(self):


## ... source file abbreviated to get to timedelta examples ...



class AxesHandlerBaseTestCase(AxesTestCase):
    def check_whitelist(self, log):
        with override_settings(
            AXES_NEVER_LOCKOUT_WHITELIST=True, AXES_IP_WHITELIST=[self.ip_address]
        ):
            AxesProxyHandler.user_login_failed(
                sender=None, request=self.request, credentials=self.credentials
            )
            client_str = get_client_str(
                self.username, self.ip_address, self.user_agent, self.path_info
            )
            log.info.assert_called_with(
                "AXES: Login failed from whitelisted client %s.", client_str
            )

    def check_empty_request(self, log, handler):
        AxesProxyHandler.user_login_failed(sender=None, credentials={}, request=None)
        log.error.assert_called_with(
            f"AXES: {handler}.user_login_failed does not function without a request."
        )


@override_settings(
    AXES_HANDLER="axes.handlers.database.AxesDatabaseHandler",
~~    AXES_COOLOFF_TIME=timedelta(seconds=1),
    AXES_RESET_ON_SUCCESS=True,
)
class AxesDatabaseHandlerTestCase(AxesHandlerBaseTestCase):
    def test_handler_reset_attempts(self):
        self.create_attempt()
        self.assertEqual(1, AxesProxyHandler.reset_attempts())
        self.assertFalse(AccessAttempt.objects.count())

    def test_handler_reset_logs(self):
        self.create_log()
        self.assertEqual(1, AxesProxyHandler.reset_logs())
        self.assertFalse(AccessLog.objects.count())

    def test_handler_reset_logs_older_than_42_days(self):
        self.create_log()

        then = timezone.now() - timezone.timedelta(days=90)
        with patch("django.utils.timezone.now", return_value=then):
            self.create_log()

        self.assertEqual(AccessLog.objects.count(), 2)
        self.assertEqual(1, AxesProxyHandler.reset_logs(age_days=42))
        self.assertEqual(AccessLog.objects.count(), 1)



## ... source file abbreviated to get to timedelta examples ...


            usernames,
        ) in configurations:
            with self.settings(**overrides):
                with self.subTest(
                    total_attempts_count=total_attempts_count,
                    failures_since_start=failures_since_start,
                    settings=overrides,
                ):
                    self.login(username=usernames[0])
                    attempt = AccessAttempt.objects.get(username=usernames[0])
                    self.assertEqual(1, attempt.failures_since_start)

                    self.login(username=usernames[1])
                    attempt = AccessAttempt.objects.get(username=usernames[1])
                    self.assertEqual(failures_since_start, attempt.failures_since_start)

                    self.assertEqual(
                        total_attempts_count, AccessAttempt.objects.count()
                    )

            AccessAttempt.objects.all().delete()


@override_settings(
    AXES_HANDLER="axes.handlers.cache.AxesCacheHandler",
~~    AXES_COOLOFF_TIME=timedelta(seconds=1),
)
class AxesCacheHandlerTestCase(AxesHandlerBaseTestCase):
    @override_settings(AXES_RESET_ON_SUCCESS=True)
    def test_handler(self):
        self.check_handler()

    @override_settings(AXES_RESET_ON_SUCCESS=False)
    def test_handler_without_reset(self):
        self.check_handler()

    @override_settings(AXES_LOCK_OUT_AT_FAILURE=False)
    def test_handler_without_lockout(self):
        self.check_handler()

    @patch("axes.handlers.cache.log")
    def test_empty_request(self, log):
        self.check_empty_request(log, "AxesCacheHandler")

    @patch("axes.handlers.cache.log")
    def test_whitelist(self, log):
        self.check_whitelist(log)


@override_settings(AXES_HANDLER="axes.handlers.dummy.AxesDummyHandler")


## ... source file continues with no further timedelta examples...

```

