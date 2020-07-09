title: django.utils dateformat Example Code
category: page
slug: django-utils-dateformat-examples
sortorder: 500011415
toc: False
sidebartitle: django.utils dateformat
meta: Python example code for the dateformat callable from the django.utils module of the Django project.


dateformat is a callable within the django.utils module of the Django project.


## Example 1 from AuditLog
[Auditlog](https://github.com/jjkester/django-auditlog)
([project documentation](https://django-auditlog.readthedocs.io/en/latest/))
is a [Django](/django.html) app that logs changes to Python objects,
similar to the Django admin's logs but with more details and
output formats. Auditlog's source code is provided as open source under the
[MIT license](https://github.com/jjkester/django-auditlog/blob/master/LICENSE).

[**AuditLog / src / auditlog_tests / tests.py**](https://github.com/jjkester/django-auditlog/blob/master/src/auditlog_tests/tests.py)

```python
# tests.py
import datetime
import django
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User, AnonymousUser
from django.core.exceptions import ValidationError
from django.db.models.signals import pre_save
from django.http import HttpResponse
from django.test import TestCase, RequestFactory
~~from django.utils import dateformat, formats, timezone
from dateutil.tz import gettz

from auditlog.middleware import AuditlogMiddleware
from auditlog.models import LogEntry
from auditlog.registry import auditlog
from auditlog_tests.models import SimpleModel, AltPrimaryKeyModel, UUIDPrimaryKeyModel, \
    ProxyModel, SimpleIncludeModel, SimpleExcludeModel, SimpleMappingModel, RelatedModel, \
    ManyRelatedModel, AdditionalDataIncludedModel, DateTimeFieldModel, ChoicesFieldModel, \
    CharfieldTextfieldModel, PostgresArrayFieldModel, NoDeleteHistoryModel
from auditlog import compat


class SimpleModelTest(TestCase):
    def setUp(self):
        self.obj = SimpleModel.objects.create(text='I am not difficult.')

    def test_create(self):
        obj = self.obj

        self.assertTrue(obj.history.count() == 1, msg="There is one log entry")

        try:
            history = obj.history.get()
        except obj.history.DoesNotExist:


## ... source file abbreviated to get to dateformat examples ...



        self.assertTrue(dtm.history.count() == 2, msg="There are two log entries")

    def test_model_with_different_time_and_timezone(self):
        timestamp = datetime.datetime(2017, 1, 10, 12, 0, tzinfo=timezone.utc)
        date = datetime.date(2017, 1, 10)
        time = datetime.time(12, 0)
        dtm = DateTimeFieldModel(label='DateTimeField model', timestamp=timestamp, date=date, time=time, naive_dt=self.now)
        dtm.save()
        self.assertTrue(dtm.history.count() == 1, msg="There is one log entry")

        timestamp = datetime.datetime(2017, 1, 10, 14, 0, tzinfo=self.utc_plus_one)
        dtm.timestamp = timestamp
        dtm.save()

        self.assertTrue(dtm.history.count() == 2, msg="There are two log entries")

    def test_changes_display_dict_datetime(self):
        timestamp = datetime.datetime(2017, 1, 10, 15, 0, tzinfo=timezone.utc)
        date = datetime.date(2017, 1, 10)
        time = datetime.time(12, 0)
        dtm = DateTimeFieldModel(label='DateTimeField model', timestamp=timestamp, date=date, time=time, naive_dt=self.now)
        dtm.save()
        localized_timestamp = timestamp.astimezone(gettz(settings.TIME_ZONE))
        self.assertTrue(dtm.history.latest().changes_display_dict["timestamp"][1] == \
~~                        dateformat.format(localized_timestamp, settings.DATETIME_FORMAT),
                        msg=("The datetime should be formatted according to Django's settings for"
                             " DATETIME_FORMAT"))
        timestamp = timezone.now()
        dtm.timestamp = timestamp
        dtm.save()
        localized_timestamp = timestamp.astimezone(gettz(settings.TIME_ZONE))
        self.assertTrue(dtm.history.latest().changes_display_dict["timestamp"][1] == \
~~                        dateformat.format(localized_timestamp, settings.DATETIME_FORMAT),
                        msg=("The datetime should be formatted according to Django's settings for"
                             " DATETIME_FORMAT"))

        with self.settings(USE_L10N=True, LANGUAGE_CODE='en-GB'):
            self.assertTrue(dtm.history.latest().changes_display_dict["timestamp"][1] == \
                        formats.localize(localized_timestamp),
                        msg=("The datetime should be formatted according to Django's settings for"
                             " USE_L10N is True with a different LANGUAGE_CODE."))


    def test_changes_display_dict_date(self):
        timestamp = datetime.datetime(2017, 1, 10, 15, 0, tzinfo=timezone.utc)
        date = datetime.date(2017, 1, 10)
        time = datetime.time(12, 0)
        dtm = DateTimeFieldModel(label='DateTimeField model', timestamp=timestamp, date=date, time=time, naive_dt=self.now)
        dtm.save()
        self.assertTrue(dtm.history.latest().changes_display_dict["date"][1] == \
~~                        dateformat.format(date, settings.DATE_FORMAT),
                        msg=("The date should be formatted according to Django's settings for"
                             " DATE_FORMAT unless USE_L10N is True."))
        date = datetime.date(2017, 1, 11)
        dtm.date = date
        dtm.save()
        self.assertTrue(dtm.history.latest().changes_display_dict["date"][1] == \
~~                        dateformat.format(date, settings.DATE_FORMAT),
                        msg=("The date should be formatted according to Django's settings for"
                             " DATE_FORMAT unless USE_L10N is True."))

        with self.settings(USE_L10N=True, LANGUAGE_CODE='en-GB'):
            self.assertTrue(dtm.history.latest().changes_display_dict["date"][1] == \
                        formats.localize(date),
                        msg=("The date should be formatted according to Django's settings for"
                             " USE_L10N is True with a different LANGUAGE_CODE."))

    def test_changes_display_dict_time(self):
        timestamp = datetime.datetime(2017, 1, 10, 15, 0, tzinfo=timezone.utc)
        date = datetime.date(2017, 1, 10)
        time = datetime.time(12, 0)
        dtm = DateTimeFieldModel(label='DateTimeField model', timestamp=timestamp, date=date, time=time, naive_dt=self.now)
        dtm.save()
        self.assertTrue(dtm.history.latest().changes_display_dict["time"][1] == \
~~                        dateformat.format(time, settings.TIME_FORMAT),
                        msg=("The time should be formatted according to Django's settings for"
                             " TIME_FORMAT unless USE_L10N is True."))
        time = datetime.time(6, 0)
        dtm.time = time
        dtm.save()
        self.assertTrue(dtm.history.latest().changes_display_dict["time"][1] == \
~~                        dateformat.format(time, settings.TIME_FORMAT),
                        msg=("The time should be formatted according to Django's settings for"
                             " TIME_FORMAT unless USE_L10N is True."))

        with self.settings(USE_L10N=True, LANGUAGE_CODE='en-GB'):
            self.assertTrue(dtm.history.latest().changes_display_dict["time"][1] == \
                        formats.localize(time),
                        msg=("The time should be formatted according to Django's settings for"
                             " USE_L10N is True with a different LANGUAGE_CODE."))

    def test_update_naive_dt(self):
        timestamp = datetime.datetime(2017, 1, 10, 15, 0, tzinfo=timezone.utc)
        date = datetime.date(2017, 1, 10)
        time = datetime.time(12, 0)
        dtm = DateTimeFieldModel(label='DateTimeField model', timestamp=timestamp, date=date, time=time, naive_dt=self.now)
        dtm.save()

        dtm.naive_dt = timezone.make_naive(timezone.now(), timezone=timezone.utc)
        dtm.save()


class UnregisterTest(TestCase):
    def setUp(self):
        auditlog.unregister(SimpleModel)
        self.obj = SimpleModel.objects.create(text='No history')


## ... source file continues with no further dateformat examples...

```

