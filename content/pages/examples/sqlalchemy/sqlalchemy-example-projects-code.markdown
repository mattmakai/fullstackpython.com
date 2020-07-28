title: SQLAlchemy Example Projects and Code
category: page
slug: sqlalchemy-code-examples
sortorder: 500030001
toc: False
sidebartitle: SQLAlchemy Example Code
meta: Python example projects and code that show how to use the SQLAlchemy object-relational mapper (ORM).


## Example Open Source Projects
The following open source projects can serve as example code for you as
you build your own applications with SQLAlchemy.


### databases
[databases](https://github.com/encode/databases) 
([project homepage](https://www.encode.io/databases/)
and
[PyPI page](https://pypi.org/project/databases/) provides 
[asyncio](https://docs.python.org/3/library/asyncio.html) support
with an [SQLALchemy](/sqlalchemy.html) Core interface for common 
[relational databases](/databases.html) such as [MySQL](/mysql.html), 
[PostgreSQL](/postgresql.html) and [SQLite](/sqlite.html). This is
handy for integrating with asynchronous I/O 
[web frameworks](/web-frameworks.html) like [Sanic](/sanic.html).
The project is open sourced under the 
[BSD 3-Clause "New" or "Revised" License](https://github.com/encode/databases/blob/master/LICENSE.md).


### CTFd
[CTFd](https://github.com/CTFd/CTFd)
([homepage](https://ctfd.io/)) is a
[capture the flag (CTF) hacking web app](https://cybersecurity.att.com/blogs/security-essentials/capture-the-flag-ctf-what-is-it-for-a-newbie)
built with [SQLAlchemy](/sqlalchemy.html) and [Flask](/flask.html).
The application can be used as-is to run CTF events, or the code can be
modified for custom rules on hacking scenarios. CTFd is open sourced under the                                                      
[Apache License 2.0](https://github.com/CTFd/CTFd/blob/master/LICENSE).


### indico
[indico](https://github.com/indico/indico) 
([project website](https://getindico.io/),
[documentation](https://docs.getindico.io/en/stable/installation/)
and [sandbox demo](https://sandbox.getindico.io/))
is a [Flask](/flask.html)-based web app for event management that is
powered by [SQLAlchemy](/sqlalchemy.html) on the backend. The code 
for this project is open sourced under the 
[MIT license](https://github.com/indico/indico/blob/master/LICENSE).


### sandman2
[sandman2](https://github.com/jeffknupp/sandman2)
([project documentation](https://sandman2.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/sandman2/))
is a code library for automatically generating 
[RESTful APIs](/application-programming-interfaces.html) from
existing database schemas. This approach is handy for solving 
straightforward situations where you want to put an abstraction
layer between one or more applications and your 
[relational database](/databases.html) to prevent or reduce
direct database access.

The sandman2 project is provided under the 
[Apache License 2.0](https://github.com/jeffknupp/sandman2/blob/master/LICENSE).


