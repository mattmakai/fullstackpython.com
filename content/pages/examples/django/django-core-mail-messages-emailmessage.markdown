title: django.core.mail.messages EmailMessage Example Code
category: page
slug: django-core-mail-messages-emailmessage-examples
sortorder: 500012515
toc: False
sidebartitle: django.core.mail.messages EmailMessage
meta: Python code examples for the EmailMessage function within the django.core.mail module of the Django project. 


The 
[EmailMessage](https://github.com/django/django/blob/master/django/core/mail/message.py)
class is contained with the 
[django.core.mail](https://github.com/django/django/tree/master/django/core/mail)
module within the [Django project](/django.html) code base. 


## Example 1 from django-emailmessagetemplate
[django-emailmessagetemplates](https://github.com/mcoconnor/django-emailmessagetemplates)
is a code library that makes it easier to add functionality for end users to 
customize email templates in a [Django](/django.html) application. The code
is available under the 
[BSD 3-Clause "New" or "Revised" License](https://github.com/mcoconnor/django-emailmessagetemplates/blob/master/LICENSE).

[**django-emailmessagetemplates / emailmessagetemplates / utils.py**](https://github.com/mcoconnor/django-emailmessagetemplates/blob/master/emailmessagetemplates/utils.py)

```python
import copy

from django.core.mail import get_connection
from django.conf import settings

~~from models import EmailMessageTemplate


def send_mail(name, related_object=None, context={}, from_email=None,
              recipient_list=[], fail_silently=False, auth_user=None,
               auth_password=None, connection=None):
    """
    Easy wrapper for sending a single templated message to a recipient list.  
    The template to use is retrieved from the database based on the name and 
    related_object (optional) fields.
    All members of the recipient list will see the other recipients in the 'To' 
    field.
    If auth_user is None, the EMAIL_HOST_USER setting is used.
    If auth_password is None, the EMAIL_HOST_PASSWORD setting is used.
    """

~~    template = EmailMessageTemplate.objects.get_template(name, related_object)

    connection = connection or get_connection(username=auth_user,
                                              password=auth_password,
                                              fail_silently=fail_silently)

~~    template.context=context
~~    template.from_email=from_email
~~    template.to=recipient_list
~~    template.connection=connection

~~    return template.send()
```
