title: django.db DatabaseError Example Code
category: page
slug: django-db-databaseerror-examples
sortorder: 500011160
toc: False
sidebartitle: django.db DatabaseError
meta: Python example code for the DatabaseError class from the django.db module of the Django project.


DatabaseError is a class within the django.db module of the Django project.


## Example 1 from django-sql-explorer
[django-sql-explorer](https://github.com/groveco/django-sql-explorer)
([PyPI page](https://pypi.org/project/django-sql-explorer/0.2/)),
also referred to as "SQL Explorer",
is a code library for the [Django](/django.html) Admin that allows
approved, authenticated users to view and execute direct database SQL
queries. The tool keeps track of executed queries so users can share them
with each other, as well as export results to downloadable formats.
django-sql-explorer is provided as open source under the
[MIT license](https://github.com/groveco/django-sql-explorer/blob/master/LICENSE).

[**django-sql-explorer / explorer / tasks.py**](https://github.com/groveco/django-sql-explorer/blob/master/explorer/./tasks.py)

```python
# tasks.py
from datetime import date, datetime, timedelta
import random
import string

from django.core.mail import send_mail
from django.core.cache import cache
~~from django.db import DatabaseError

from explorer import app_settings
from explorer.exporters import get_exporter_class
from explorer.models import Query, QueryLog

if app_settings.ENABLE_TASKS:
    from celery import task
    from celery.utils.log import get_task_logger
    from explorer.utils import s3_upload
    logger = get_task_logger(__name__)
else:
    from explorer.utils import noop_decorator as task
    import logging
    logger = logging.getLogger(__name__)


@task
def execute_query(query_id, email_address):
    q = Query.objects.get(pk=query_id)
    send_mail('[SQL Explorer] Your query is running...',
              '%s is running and should be in your inbox soon!' % q.title,
              app_settings.FROM_EMAIL,
              [email_address])

    exporter = get_exporter_class('csv')(q)
    random_part = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
    try:
        url = s3_upload('%s.csv' % random_part, exporter.get_file_output())
        subj = '[SQL Explorer] Report "%s" is ready' % q.title
        msg = 'Download results:\n\r%s' % url
~~    except DatabaseError as e:
        subj = '[SQL Explorer] Error running report %s' % q.title
        msg = 'Error: %s\nPlease contact an administrator' %  e
        logger.warning('%s: %s' % (subj, e))
    send_mail(subj, msg, app_settings.FROM_EMAIL, [email_address])


@task
def snapshot_query(query_id):
    try:
        logger.info("Starting snapshot for query %s..." % query_id)
        q = Query.objects.get(pk=query_id)
        exporter = get_exporter_class('csv')(q)
        k = 'query-%s/snap-%s.csv' % (q.id, date.today().strftime('%Y%m%d-%H:%M:%S'))
        logger.info("Uploading snapshot for query %s as %s..." % (query_id, k))
        url = s3_upload(k, exporter.get_file_output())
        logger.info("Done uploading snapshot for query %s. URL: %s" % (query_id, url))
    except Exception as e:
        logger.warning("Failed to snapshot query %s (%s). Retrying..." % (query_id, e))
        snapshot_query.retry()


@task
def snapshot_queries():
    logger.info("Starting query snapshots...")


## ... source file continues with no further DatabaseError examples...

```

