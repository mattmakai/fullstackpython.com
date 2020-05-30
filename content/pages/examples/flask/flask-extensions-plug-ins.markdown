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


### flask-base
[flask-base](https://github.com/hack4impact/flask-base) 
([project documentation](http://hack4impact.github.io/flask-base/))
is a boilerplate starter application that is pre-configured with 
[SQLAlchemy](/sqlalchemy.html), [Redis](/redis.html), user 
authentication and other features.

flask-base's code is open sourced 
[under the MIT license](https://github.com/hack4impact/flask-base/blob/master/LICENSE.md).


### Flask RESTX
[Flask RESTX](https://github.com/python-restx/flask-restx) is an
extension that makes it easier to build
[RESTful APIs](/application-programming-interfaces.html) into
your applications. Flask RESTX aims for minimal configuration to
get basic APIs running for existing applications and it exposes
endpoint documentation using [Swagger](https://swagger.io/).

Flask RESTX is provided as open source under the
[BSD  3-Clause license](https://github.com/python-restx/flask-restx/blob/master/LICENSE).


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

