title: sqlalchemy.orm.attributes flag_modified Example Code
category: page
slug: sqlalchemy-orm-attributes-flag-modified-examples
sortorder: 500031078
toc: False
sidebartitle: sqlalchemy.orm.attributes flag_modified
meta: Python example code that shows how to use the flag_modified callable from the sqlalchemy.orm.attributes module of the SQLAlchemy project.


`flag_modified` is a callable within the `sqlalchemy.orm.attributes` module of the SQLAlchemy project.

<a href="/sqlalchemy-orm-attributes-instrumentedattribute-examples.html">InstrumentedAttribute</a>
and
<a href="/sqlalchemy-orm-attributes-queryableattribute-examples.html">QueryableAttribute</a>
are a couple of other callables within the `sqlalchemy.orm.attributes` package that also have code examples.

## Example 1 from indico
[indico](https://github.com/indico/indico)
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management that is
powered by [SQLAlchemy](/sqlalchemy.html) on the backend. The code
for this project is open sourced under the
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).

[**indico / indico / core / emails.py**](https://github.com/indico/indico/blob/master/indico/core/emails.py)

```python
# emails.py

from __future__ import absolute_import, unicode_literals

import cPickle
import os
import tempfile
from datetime import date

import click
from celery.exceptions import MaxRetriesExceededError, Retry
~~from sqlalchemy.orm.attributes import flag_modified

from indico.core.celery import celery
from indico.core.config import config
from indico.core.db import db
from indico.core.logger import Logger
from indico.util.date_time import now_utc
from indico.util.emails.backend import EmailBackend
from indico.util.emails.message import EmailMessage
from indico.util.string import truncate


logger = Logger.get('emails')
MAX_TRIES = 10
DELAYS = [30, 60, 120, 300, 600, 1800, 3600, 3600, 7200]


@celery.task(name='send_email', bind=True, max_retries=None)
def send_email_task(task, email, log_entry=None):
    attempt = task.request.retries + 1
    try:
        do_send_email(email, log_entry, _from_task=True)
    except Exception as exc:
        delay = (DELAYS + [0])[task.request.retries] if not config.DEBUG else 1
        try:


## ... source file abbreviated to get to flag_modified examples ...


            db.session.commit()


def do_send_email(email, log_entry=None, _from_task=False):
    with EmailBackend(timeout=config.SMTP_TIMEOUT) as conn:
        msg = EmailMessage(subject=email['subject'], body=email['body'], from_email=email['from'],
                           to=email['to'], cc=email['cc'], bcc=email['bcc'], reply_to=email['reply_to'],
                           attachments=email['attachments'], connection=conn)
        if not msg.to:
            msg.extra_headers['To'] = 'Undisclosed-recipients:;'
        if email['html']:
            msg.content_subtype = 'html'
        msg.send()
    if not _from_task:
        logger.info('Sent email "%s"', truncate(email['subject'], 100))
    if log_entry:
        update_email_log_state(log_entry)


def update_email_log_state(log_entry, failed=False):
    if failed:
        log_entry.data['state'] = 'failed'
    else:
        log_entry.data['state'] = 'sent'
        log_entry.data['sent_dt'] = now_utc(False).isoformat()
~~    flag_modified(log_entry, 'data')


def store_failed_email(email, log_entry=None):
    prefix = 'failed-email-{}-'.format(date.today().isoformat())
    fd, name = tempfile.mkstemp(prefix=prefix, dir=config.TEMP_DIR)
    with os.fdopen(fd, 'wb') as f:
        cPickle.dump((email, log_entry.id if log_entry else None), f)
    return name


def resend_failed_email(path):
    from indico.modules.events.logs import EventLogEntry
    with open(path, 'rb') as f:
        email, log_entry_id = cPickle.load(f)
    log_entry = EventLogEntry.get(log_entry_id) if log_entry_id is not None else None
    do_send_email(email, log_entry)
    db.session.commit()
    os.remove(path)
    return email


def resend_failed_emails_cmd(paths):
    for path in paths:
        email = resend_failed_email(path)


## ... source file continues with no further flag_modified examples...

```

