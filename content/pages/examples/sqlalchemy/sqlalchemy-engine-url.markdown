title: sqlalchemy.engine url Example Code
category: page
slug: sqlalchemy-engine-url-examples
sortorder: 500031025
toc: False
sidebartitle: sqlalchemy.engine url
meta: Python example code that shows how to use the url callable from the sqlalchemy.engine module of the SQLAlchemy project.


`url` is a callable within the `sqlalchemy.engine` module of the SQLAlchemy project.

<a href="/sqlalchemy-engine-connection-examples.html">Connection</a>,
<a href="/sqlalchemy-engine-engine-examples.html">Engine</a>,
<a href="/sqlalchemy-engine-create-engine-examples.html">create_engine</a>,
and <a href="/sqlalchemy-engine-default-examples.html">default</a>
are several other callables with code examples from the same `sqlalchemy.engine` package.

## Example 1 from alembic
[Alembic](https://github.com/sqlalchemy/alembic)
([project documentation](https://alembic.sqlalchemy.org/) and
[PyPI page](https://pypi.org/project/alembic/))
is a data migrations tool used with [SQLAlchemy](/sqlalchemy.html) to make
database schema changes. The Alembic project is open sourced under the
[MIT license](https://github.com/sqlalchemy/alembic/blob/master/LICENSE).

[**alembic / alembic / util / messaging.py**](https://github.com/sqlalchemy/alembic/blob/master/alembic/util/messaging.py)

```python
# messaging.py
import logging
import sys
import textwrap
import warnings

~~from sqlalchemy.engine import url

from .compat import binary_type
from .compat import collections_abc
from .compat import py27
from .compat import string_types

log = logging.getLogger(__name__)

if py27:
    logging.getLogger("alembic").addHandler(logging.NullHandler())


try:
    import fcntl
    import termios
    import struct

    ioctl = fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack("HHHH", 0, 0, 0, 0))
    _h, TERMWIDTH, _hp, _wp = struct.unpack("HHHH", ioctl)
    if TERMWIDTH <= 0:  # can occur if running in emacs pseudo-tty
        TERMWIDTH = None
except (ImportError, IOError):
    TERMWIDTH = None



## ... source file abbreviated to get to url examples ...


        try:
            stream.write(t)
        except IOError:
            break


def status(_statmsg, fn, *arg, **kw):
    newline = kw.pop("newline", False)
    msg(_statmsg + " ...", newline, True)
    try:
        ret = fn(*arg, **kw)
        write_outstream(sys.stdout, "  done\n")
        return ret
    except:
        write_outstream(sys.stdout, "  FAILED\n")
        raise


def err(message):
    log.error(message)
    msg("FAILED: %s" % message)
    sys.exit(-1)


def obfuscate_url_pw(u):
~~    u = url.make_url(u)
    if u.password:
        u.password = "XXXXX"
    return str(u)


def warn(msg, stacklevel=2):
    warnings.warn(msg, UserWarning, stacklevel=stacklevel)


def msg(msg, newline=True, flush=False):
    if TERMWIDTH is None:
        write_outstream(sys.stdout, msg)
        if newline:
            write_outstream(sys.stdout, "\n")
    else:
        lines = textwrap.wrap(msg, TERMWIDTH)
        if len(lines) > 1:
            for line in lines[0:-1]:
                write_outstream(sys.stdout, "  ", line, "\n")
        write_outstream(sys.stdout, "  ", lines[-1], ("\n" if newline else ""))
    if flush:
        sys.stdout.flush()




## ... source file continues with no further url examples...

```


## Example 2 from GINO
[GINO](https://github.com/fantix/gino)
([project documentation](https://python-gino.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/gino/))
is an [object-relational mapper (ORM)](/object-relational-mappers-orms.html)
built on SQLAlchemy that is non-blocking and therefore designed to work properly
with asynchronously-run code, for example, an application written with
[asyncio](https://docs.python.org/3/library/asyncio.html).

GINO is open sourced under the [BSD License](https://github.com/python-gino/gino/blob/master/LICENSE).

[**GINO / src/gino / strategies.py**](https://github.com/python-gino/gino/blob/master/src/gino/./strategies.py)

```python
# strategies.py
import asyncio
from copy import copy

~~from sqlalchemy.engine import url
from sqlalchemy import util
from sqlalchemy.engine.strategies import EngineStrategy

from .engine import GinoEngine


class GinoStrategy(EngineStrategy):

    name = "gino"
    engine_cls = GinoEngine

    async def create(self, name_or_url, loop=None, **kwargs):
        engine_cls = self.engine_cls
~~        u = url.make_url(name_or_url)
        if loop is None:
            loop = asyncio.get_event_loop()
        if u.drivername in {"postgresql", "postgres"}:
            u = copy(u)
            u.drivername = "postgresql+asyncpg"

        dialect_cls = u.get_dialect()

        pop_kwarg = kwargs.pop

        dialect_args = {}
        for k in util.get_cls_kwargs(dialect_cls).union(
            getattr(dialect_cls, "init_kwargs", set())
        ):
            if k in kwargs:
                dialect_args[k] = pop_kwarg(k)

        kwargs.pop("module", None)  # unused
        dbapi_args = {}
        for k in util.get_func_kwargs(dialect_cls.dbapi):
            if k in kwargs:
                dbapi_args[k] = pop_kwarg(k)
        dbapi = dialect_cls.dbapi(**dbapi_args)
        dialect_args["dbapi"] = dbapi


## ... source file continues with no further url examples...

```

