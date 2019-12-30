title: django.contrib.auth.hashers make_password Python Code Examples
category: page
slug: django-contrib-auth-hashers-make-password-examples
sortorder: 500012210
toc: False
sidebartitle: django.contrib.auth.hashers make_password
meta: Python code examples for the Django function make_password from the django.contrib.auth.hashers module.


[Django](/django.html)'s
[make_password](https://docs.djangoproject.com/en/dev/topics/auth/passwords/#django.contrib.auth.hashers.make_password)
([source code](https://github.com/django/django/blob/master/django/contrib/auth/hashers.py))
function converts a plain-text password into a hash that is appropriate
for storing in a [persistent database](/databases.html).

You definitely do not want to try to roll your own encryption and hashing
functions for storing passwords when this function already exists.


## Example 1 from gadget-board
[gadget-board](https://github.com/mik4el/gadget-board) is a 
[Django](/django.html),
[Django REST Framework (DRF)](/django-rest-framework-drf.html) and
[Angular](/angular.html) web application that is open source under the 
[Apache2 license](https://github.com/mik4el/gadget-board/blob/master/LICENSE).

[**gadget-board / web / authentication / views.py**](https://github.com/mik4el/gadget-board/blob/master/web/authentication/views.py)

```python
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
~~from django.contrib.auth.hashers import make_password

from .models import Account
from .permissions import IsAccountOwner
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            # only logged in users can see accounts
            return (permissions.IsAuthenticated(),)  

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            if 'password' not in serializer.validated_data:
                return Response({
                    'error': 'Password required for creating account.'
                }, status=status.HTTP_400_BAD_REQUEST)

            account = Account.objects.\
                create_account(**serializer.validated_data)

            # add JWT token to response
            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(account)
            token = jwt_encode_handler(payload)

            serializer.validated_data['token'] = token

            return Response(serializer.validated_data, 
                            status=status.HTTP_201_CREATED)

        return Response({
            'error': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        # Hash password but passwords are not required
        if ('password' in self.request.data):
~~            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

    def perform_update(self, serializer):
        # Hash password but passwords are not required
        if ('password' in self.request.data):
~~            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()
```
