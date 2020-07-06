title: Flask Extensions, Plug-ins and Related Libraries
category: page
slug: flask-extensions-plug-ins-related-libraries
sortorder: 500020000
toc: False
sidebartitle: Flask Extensions
meta: Python code extensions and plug-in projects that show how to use the Flask web app framework.


[Flask](/flask.html) is a Python [web framework](/web-frameworks.html).

<a href="https://flask.palletsprojects.com/" style="border: none;"><img src="/img/logos/flask.jpg" width="100%" alt="Official Flask logo. Flask Artwork License." class="shot" style="margin: 20px 0 20px 0"></a>

Flask has a wide range of code libraries and extensions that make the
[web framework](/web-frameworks.html) go from a *micro*framework into 
a full-featured web application creation tool.

Flask's large ecosystem of extensions make it easier for developers to
build common web app features such as authentication, 
[database](/databases.html) operations and 
[APIs](/application-programming-interfaces.html) even though support
is not built into the core Flask [web framework](/web-frameworks.html).
This design is by choice in contrast to [Django](/django.html)'s 
"batteries-included" approach. Either framework's design decision 
is a viable approach depending on the needs and requirements of the
application you are building.

The following projects, ordered alphabetically, can be helpful both
as extensions added to your code base as well as example code for
building your own applications.


### Flask App Builder
[Flask-AppBuilder](https://github.com/dpgaspar/Flask-AppBuilder) 
([documentation](https://flask-appbuilder.readthedocs.io/en/latest/)
and
[example apps](https://github.com/dpgaspar/Flask-AppBuilder/tree/master/examples))
is a web application generator that uses Flask to automatically create
the code for database-driven applications based on parameters set
by the user. The generated applications include default security settings,
forms, and internationalization support.

Flask App Builder is provided under the
[BSD 3-Clause "New" or "Revised" license](https://github.com/dpgaspar/Flask-AppBuilder/blob/master/LICENSE).


### Flask-Ask
[Flask-Ask](https://github.com/johnwheeler/flask-ask) is an extension
for building Amazon Alexa skills using a familiar [Flask](/flask.html)
functions style of organization. There is a 
[starter tutorial](https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development)
that shows how to use the framework and the code
is provided as open source under the 
[Apache 2.0 license](https://github.com/johnwheeler/flask-ask/blob/master/LICENSE.txt).


### flask-base
[flask-base](https://github.com/hack4impact/flask-base) 
([project documentation](http://hack4impact.github.io/flask-base/))
is a boilerplate starter application that is pre-configured with 
[SQLAlchemy](/sqlalchemy.html), [Redis](/redis.html), user 
authentication and other features.

flask-base's code is open sourced 
[under the MIT license](https://github.com/hack4impact/flask-base/blob/master/LICENSE.md).


### flask-bootstrap
[flask-bootstrap](https://github.com/mbr/flask-bootstrap)
([PyPI package information](https://pypi.org/project/Flask-Bootstrap/))
makes it easier to use the [Bootstrap CSS framework](/bootstrap-css.html)
in your [Flask](/flask.html) applications with less boilerplate
code. The project was primarily created by
[Marc Brinkmann @mbr](https://github.com/mbr) and the source code is
open sourced under the
[Apache 2.0 license](https://github.com/mbr/flask-bootstrap/blob/master/LICENSE).


### Flask Debug-toolbar
[Flask Debug-toolbar](https://github.com/flask-debugtoolbar/flask-debugtoolbar)
([documentation](https://flask-debugtoolbar.readthedocs.io/en/latest/)
and
[PyPI page](https://pypi.org/project/Flask-DebugToolbar/))
is a [Flask](/flask.html) conversion of the popular 
[Django Debug Toolbar](https://github.com/jazzband/django-debug-toolbar)
project. This extension creates a sidebar with useful debugging
information when you are running a Flask application in development 
mode. The project is provided as open source under 
[this license](https://github.com/flask-debugtoolbar/flask-debugtoolbar/blob/master/LICENSE).


### Flask-HTTPAuth
[Flask-HTTPAuth](https://github.com/miguelgrinberg/Flask-HTTPAuth)
([documentation](https://flask-httpauth.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/Flask-HTTPAuth/))
is a [Flask](/flask.html) framework extension that creates
Basic and Digest HTTP authentication for routes. This project
is primarily built and maintained by 
[Miguel Grinberg](https://blog.miguelgrinberg.com/). It is provided
as open source under the 
[MIT license](https://github.com/miguelgrinberg/Flask-HTTPAuth/blob/master/LICENSE).


### Flask-Login
[Flask-Login](https://github.com/maxcountryman/flask-login)
([project documentation](https://flask-login.readthedocs.io/en/latest/)
and [PyPI package](https://pypi.org/project/Flask-Login/))
is a [Flask](/flask.html) extension that provides user session
management, which handles common tasks such as logging in
and out of a [web application](/web-development.html) and
managing associated user session data. Flask-Login is
open sourced under the
[MIT license](https://github.com/maxcountryman/flask-login/blob/master/LICENSE).


### flask-praetorian
[flask-praetorian](https://github.com/dusktreader/flask-praetorian)
([project documentation](https://flask-praetorian.readthedocs.io/en/latest/)
and
[PyPI package information](https://pypi.org/project/flask-praetorian/))
extends the [Flask](/flask.html) framework security model with JWT tokens,
which is particularly useful when using a front end 
[JavaScript](/javascript.html) framework such as [React](/react.html)
or [Angular](/angular.html). [PyJWT](https://pyjwt.readthedocs.io/en/latest/)
is used under the hood to ensure a solid JWT implementation.
This extension makes it much easier to add functionality that checks
user roles on URLs before allowing access to a resource. flask-praetorian
is open sourced under the 
[MIT license](https://github.com/dusktreader/flask-praetorian/blob/master/LICENSE.rst).


### Flask RESTX
[Flask RESTX](https://github.com/python-restx/flask-restx) is an
extension that makes it easier to build
[RESTful APIs](/application-programming-interfaces.html) into
your applications. Flask RESTX aims for minimal configuration to
get basic APIs running for existing applications and it exposes
endpoint documentation using [Swagger](https://swagger.io/).

Flask RESTX is provided as open source under the
[BSD 3-Clause license](https://github.com/python-restx/flask-restx/blob/master/LICENSE).


### Flask-Security-Too
[Flask-Security-Too](https://github.com/Flask-Middleware/flask-security/) 
([PyPi page](https://pypi.org/project/Flask-Security-Too/) and
[project documentation](https://flask-security-too.readthedocs.io/en/stable/))
is a maintained fork of the original 
[Flask-Security](https://github.com/mattupstate/flask-security) project that
makes it easier to add common security features to [Flask](/flask.html)
web applications. A few of the critical goals of the Flask-Security-Too
project are ensuring JavaScript client-based single-page applications (SPAs)
can work securely with Flask-based backends and that guidance by the
[OWASP](https://owasp.org/) organization is followed by default.

The Flask-Security-Too project is provided as open source under the
[MIT license](https://github.com/Flask-Middleware/flask-security/blob/master/LICENSE).


### Flask-SocketIO
[Flask-SocketIO](https://github.com/miguelgrinberg/Flask-SocketIO)
([PyPI package information](https://pypi.org/project/Flask-SocketIO/),
[official tutorial](https://blog.miguelgrinberg.com/post/easy-websockets-with-flask-and-gevent)
and
[project documentation](https://flask-socketio.readthedocs.io/en/latest/))
is a code library by [Miguel Grinberg](https://blog.miguelgrinberg.com/index)
that provides Socket.IO integration for [Flask](/flask.html) applications.
This extension makes it easier to add bi-directional communications on the 
web via the [WebSockets](/websockets.html) protocol.

The Flask-SocketIO project is open source under the 
[MIT license](https://github.com/miguelgrinberg/Flask-SocketIO/blob/master/LICENSE).


### Flask-User
[Flask-User](https://github.com/lingthio/Flask-User)
([PyPI information](https://pypi.org/project/Flask-User/)
and
[project documentation](https://flask-user.readthedocs.io/en/latest/))
is a [Flask](/flask.html) extension that makes it easier to add
custom user account management and authentication to the projects
you are building. The extension supports persistent data storage
through both [relational databases](/databases.html) and
[MongoDB](/mongodb.html). The project is provided as open source under
the [MIT license](https://github.com/lingthio/Flask-User/blob/master/LICENSE.txt).


### Flask-VueJs-Template
[Flask-VueJs-Template](https://github.com/gtalarico/flask-vuejs-template)
([demo site](https://flask-vuejs-template.herokuapp.com/))
is a minimal [Flask](/flask.html) boilerplate starter project that
combines Flask, [Vue.js](https://www.fullstackpython.com/vuejs.html),
and [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/).
The project provides some sensible defaults that are easy to continue
building on, and the source code is open source under the
[MIT license](https://github.com/gtalarico/flask-vuejs-template/blob/master/LICENSE.md).


### Flask-WTF
[Flask-WTF](https://github.com/lepture/flask-wtf)
([project documentation](https://flask-wtf.readthedocs.io/en/stable/)
and
[PyPI page](https://pypi.org/project/Flask-WTF/))
provides a bridge between [Flask](/flask.html) and the the 
[WTForms](https://wtforms.readthedocs.io/en/2.3.x/) form-handling library.
It makes it easier to use WTForms by reducing boilerplate code and 
shorter examples for common form operations as well as common security
practices such as [CSRF](/cross-site-request-forgery-csrf.html).

