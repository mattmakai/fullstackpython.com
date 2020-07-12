title: django.template.base token_kwargs Example Code
category: page
slug: django-template-base-token-kwargs-examples
sortorder: 500011375
toc: False
sidebartitle: django.template.base token_kwargs
meta: Python example code for the token_kwargs callable from the django.template.base module of the Django project.


token_kwargs is a callable within the django.template.base module of the Django project.


## Example 1 from django-floppyforms
[django-floppyforms](https://github.com/jazzband/django-floppyforms)
([project documentation](https://django-floppyforms.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/django-floppyforms/))
is a [Django](/django.html) code library for better control
over rendering HTML forms in your [templates](/template-engines.html).

The django-floppyforms code is provided as
[open source](https://github.com/jazzband/django-floppyforms/blob/master/LICENSE)
and maintained by the collaborative developer community group
[Jazzband](https://jazzband.co/).

[**django-floppyforms / floppyforms / templatetags / floppyforms.py**](https://github.com/jazzband/django-floppyforms/blob/master/floppyforms/templatetags/floppyforms.py)

```python
# floppyforms.py
from collections import defaultdict
from contextlib import contextmanager

import django
from django.conf import settings
from django.template import (Library, Node, Variable,
                             TemplateSyntaxError, VariableDoesNotExist)
~~from django.template.base import token_kwargs
from django.utils.functional import empty

from ..compat import get_template


from django.forms.utils import ErrorList


register = Library()


def is_formset(var):
    significant_attributes = ('forms', 'management_form')
    return all(hasattr(var, attr) for attr in significant_attributes)


def is_form(var):
    significant_attributes = ('is_bound', 'data', 'fields')
    return all(hasattr(var, attr) for attr in significant_attributes)


def is_bound_field(var):
    significant_attributes = ('as_widget', 'as_hidden', 'is_hidden')
    return all(hasattr(var, attr) for attr in significant_attributes)


## ... source file abbreviated to get to token_kwargs examples ...



    @classmethod
    def parse_using(cls, tagname, parser, bits, options):
        if bits:
            if bits[0] == 'using':
                bits.pop(0)
                if len(bits):
                    if bits[0] in ('with', 'only'):
                        raise TemplateSyntaxError(
                            '%s: you must provide one template after '
                            '"using" and before "with" or "only".' %
                            tagname)
                    options['using'] = Variable(bits.pop(0))
                else:
                    raise TemplateSyntaxError('%s: expected a template name '
                                              'after "using".' % tagname)
            elif not cls.optional_using_parameter:
                raise TemplateSyntaxError('Unknown argument for %s tag: %r.' %
                                          (tagname, bits[0]))

    @classmethod
    def parse_with(cls, tagname, parser, bits, options):
        if bits:
            if bits[0] == 'with':
                bits.pop(0)
~~                arguments = token_kwargs(bits, parser, support_legacy=False)
                if not arguments:
                    raise TemplateSyntaxError('"with" in %s tag needs at '
                                              'least one keyword argument.' %
                                              tagname)
                options['with'] = arguments
            elif bits[0] not in ('only',) and not cls.optional_with_parameter:
                raise TemplateSyntaxError('Unknown argument for %s tag: %r.' %
                                          (tagname, bits[0]))

        if bits:
            if cls.accept_only_parameter and bits[0] == 'only':
                bits.pop(0)
                options['only'] = True

    @classmethod
    def parse_for(cls, tagname, parser, bits, options):
        if bits:
            if bits[0] == 'for':
                bits.pop(0)
                if len(bits):
                    options['for'] = Variable(bits.pop(0))
                else:
                    raise TemplateSyntaxError('%s: expected an argument '
                                              'after "for".' % tagname)


## ... source file continues with no further token_kwargs examples...

```

