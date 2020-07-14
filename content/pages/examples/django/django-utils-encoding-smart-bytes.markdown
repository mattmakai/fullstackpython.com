title: django.utils.encoding smart_bytes Example Code
category: page
slug: django-utils-encoding-smart-bytes-examples
sortorder: 500011447
toc: False
sidebartitle: django.utils.encoding smart_bytes
meta: Python example code for the smart_bytes callable from the django.utils.encoding module of the Django project.


smart_bytes is a callable within the django.utils.encoding module of the Django project.


## Example 1 from django-pipeline
[django-pipeline](https://github.com/jazzband/django-pipeline)
([project documentation](https://django-pipeline.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/django-pipeline/))
is a code library for handling and compressing
[static content assets](/static-content.html) when handling requests in
[Django](/django.html) web applications.

The django-pipeline project is open sourced under the
[MIT License](https://github.com/jazzband/django-pipeline/blob/master/LICENSE)
and it is maintained by the developer community group
[Jazzband](https://jazzband.co/).

[**django-pipeline / pipeline / compressors / __init__.py**](https://github.com/jazzband/django-pipeline/blob/master/pipeline/compressors/__init__.py)

```python
# __init__.py
import base64
import os
import posixpath
import re
import subprocess

from itertools import takewhile

from django.contrib.staticfiles.storage import staticfiles_storage
~~from django.utils.encoding import smart_bytes, force_text

from pipeline.conf import settings
from pipeline.exceptions import CompressorError
from pipeline.utils import to_class, relpath, set_std_streams_blocking

URL_DETECTOR = r"""url\((['"]?)\s*(.*?)\1\)"""
URL_REPLACER = r"""url\(__EMBED__(.+?)(\?\d+)?\)"""
NON_REWRITABLE_URL = re.compile(r'^(#|http:|https:|data:|//)')

DEFAULT_TEMPLATE_FUNC = "template"
TEMPLATE_FUNC = r"""var template = function(str){var fn = new Function('obj', 'var __p=[],print=function(){__p.push.apply(__p,arguments);};with(obj||{}){__p.push(\''+str.replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/<%=([\s\S]+?)%>/g,function(match,code){return "',"+code.replace(/\\'/g, "'")+",'";}).replace(/<%([\s\S]+?)%>/g,function(match,code){return "');"+code.replace(/\\'/g, "'").replace(/[\r\n\t]/g,' ')+"__p.push('";}).replace(/\r/g,'\\r').replace(/\n/g,'\\n').replace(/\t/g,'\\t')+"');}return __p.join('');");return fn;};"""

MIME_TYPES = {
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.tif': 'image/tiff',
    '.tiff': 'image/tiff',
    '.ttf': 'font/truetype',
    '.otf': 'font/opentype',
    '.woff': 'font/woff'
}
EMBED_EXTS = MIME_TYPES.keys()


## ... source file abbreviated to get to smart_bytes examples ...




class CompressorBase(object):
    def __init__(self, verbose):
        self.verbose = verbose

    def filter_css(self, css):
        raise NotImplementedError

    def filter_js(self, js):
        raise NotImplementedError


class SubProcessCompressor(CompressorBase):
    def execute_command(self, command, content):
        argument_list = []
        for flattening_arg in command:
            if isinstance(flattening_arg, (str,)):
                argument_list.append(flattening_arg)
            else:
                argument_list.extend(flattening_arg)

        pipe = subprocess.Popen(argument_list, stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        if content:
~~            content = smart_bytes(content)
        stdout, stderr = pipe.communicate(content)
        set_std_streams_blocking()
        if stderr.strip() and pipe.returncode != 0:
            raise CompressorError(stderr)
        elif self.verbose:
            print(stderr)
        return force_text(stdout)


class NoopCompressor(CompressorBase):
    def compress_js(self, js):
        return js

    def compress_css(self, css):
        return css



## ... source file continues with no further smart_bytes examples...

```

