title: Changelog 
category: page
slug: change-log
sortorder: 0700
toc: True
sidebartitle: Changelog
meta: The changelog page explains what is new on Full Stack Python.


Here are the high-level changes to Full Stack Python in reverse 
chronological order since its inception in December 2012. You can 
view commit-level changes via the 
[source repository's commit log](https://github.com/mattmakai/fullstackpython.com/commits/) 
on GitHub.

## 2020
### August
* New blog posts on
  [How to Transcribe Speech Recordings into Text with Python](/blog/transcribe-recordings-speech-text-assemblyai.html)
  and
  [Using Sentry to Handle Python Exceptions in Django Projects](/blog/sentry-handle-exceptions-django-projects.html).
* Added new [GPT-3 page](/gpt-3.html).
* Updated [debugging](/debugging.html) page with some additional descriptions.

### July
* Updated [webhooks](/webhooks.html) page with additional resources.
* New blog posts:
    * [Tracking Daily User Data in Django with django-user-visit](/blog/track-daily-user-data-django-user-visit.html)
    * [Quickly Use Bootstrap 4 in a Django Template with a CDN](/blog/bootstrap-4-django-template.html)
    * [How to report errors in Flask web apps with Sentry](/blog/report-errors-flask-web-apps-sentry.html)

### June
* Added new example code for [Django](/django.html) modules:
    * [django.contrib.admin.helpers](/django-contrib-admin-helpers-examples.html)
      [ActionForm](/django-contrib-admin-helpers-actionform-examples.html),
      and
      [AdminForm](/django-contrib-admin-helpers-adminform-examples.html)
    * django.contrib.admin.options 
      [IS_POPUP_VAR](/django-contrib-admin-options-is-popup-var-examples.html),
      [IncorrectLookupParameters](/django-contrib-admin-options-incorrectlookupparameters-examples.html),
      [ModelAdmin](/django-contrib-admin-options-modeladmin-examples.html),
      and
      [csrf_protect_m](/django-contrib-admin-options-csrf-protect-m-examples.html)
    * django.contrib.admin.sites
      [NotRegistered](/django-contrib-admin-sites-notregistered-examples.html)
      and
      [site](/django-contrib-admin-sites-site-examples.html)
    * django.core
      [cache](/django-core-cache-examples.html),
      [checks](/django-core-checks-examples.html),
      [exceptions](/django-core-exceptions-examples.html),
      [mail](/django-core-mail-examples.html),
      [management](/django-core-management-examples.html),
      [serializers](/django-core-serializers-examples.html),
      [signals](/django-core-signals-examples.html),
      [signing](/django-core-signing-examples.html),
      and
      [validators](/django-core-validators-examples.html)
    * django.utils.translation 
      [LANGUAGE_SESSION_KEY](/django-utils-translation-language-session-key-examples.html),
      [activate](/django-utils-translation-activate-examples.html),
      [deactivate_all](/django-utils-translation-deactivate-all-examples.html),
      [get_language](/django-utils-translation-get-language-examples.html),
      [get_language_from_request](/django-utils-translation-get-language-from-request-examples.html),
      [gettext](/django-utils-translation-gettext-examples.html),
      [gettext_lazy](/django-utils-translation-gettext-lazy-examples.html),
      [ngettext](/django-utils-translation-ngettext-examples.html),
      [override](/django-utils-translation-override-examples.html),
      [pgettext](/django-utils-translation-pgettext-examples.html),
      [pgettext_lazy](/django-utils-translation-pgettext-lazy-examples.html),
      [ugettext](/django-utils-translation-ugettext-examples.html),
      [ugettext_lazy](/django-utils-translation-ugettext-lazy-examples.html),
      [ungettex](/django-utils-translation-ungettext-examples.html),
      and
      [ungettext_lazy](/django-utils-translation-ungettext-lazy-examples.html)
* Added new example code pages for Flask modules:
    * flask.blueprints [Blueprint](/flask-blueprints-blueprint-examples.html)
    * flask.ctx [after_this_request](/flask-ctx-after-this-request-examples.html),
      [has_app_context](/flask-ctx-has-app-context-examples.html) and
      [has_request_context](/flask-ctx-has-request-context-examples.html)
    * flask.globals [current_app](/flask-globals-current-app-examples.html)
    * flask.helpers [send_file](flask-helpers-send-file-examples.html)
    * flask.json [JSONEncoder](/flask-json-jsonencoder-examples.html)
    * flask.sessions [BadSignature](/flask-sessions-badsignature-examples.html)
      and
      [SessionMixin](/flask-sessions-sessionmixin-examples.html)

### May
* Added new example code pages for Flask modules:
    * flask.cli [FlaskGroup](/flask-cli-flaskgroup-examples.html),
      [ScriptInfo](/flask-cli-scriptinfo-examples.html), and
      [with_appcontext](/flask-cli-with-appcontext-examples.html)
    * flask.globals [request](/flask-globals-request-examples.html) and
      [session](/flask-globals-session-examples.html)
    * flask.helpers [flask](/flask-helpers-flash-examples.html),
      [make_response](/flask-helpers-make-response-examples.html), and
      [url_for](/flask-helpers-url-for-examples.html)
    * flask.sessions [SessionInterface](/flask-sessions-sessioninterface-examples.html)
    * flask.signals [Namespace](/flask-signals-namespace-examples.html)
    * flask.templating 
      [render_template](/flask-templating-render-template-examples.html)
    * flask.views
      [MethodView](/flask-views-methodview-examples.html),
      [View](/flask-views-view-examples.html), and
      [http_method_funcs](/flask-views-http-method-funcs-examples.html)
* New blog post on 
  [Reporting Exceptions in Python Scripts with Sentry](/blog/report-exceptions-python-scripts-sentry.html).
* Tweaked some CSS for the site.
* Added a new page with the start of 
  [pandas example code and projects](/pandas-code-examples.html).

### April
* Merge [PR #233](https://github.com/mattmakai/fullstackpython.com/pull/233) and 
  [PR #235](https://github.com/mattmakai/fullstackpython.com/pull/235) for new 
  [Celery](/celery.html) and [podcast](/best-python-podcasts.html) resources.
* Updated the [web design](/web-design.html) page with new resources.

### March
* Added another new blog post on
  [Exporting pandas DataFrames into SQLite with SQLAlchemy](/blog/export-pandas-dataframes-sqlite-sqlalchemy.html).
* Added new blog post tutorial on 
  [Learning pandas by Exploring COVID-19 Data](/blog/learn-pandas-basic-commands-explore-covid-19-data.html).
* New [web design](/web-design.html) and 
  [web development](/web-development.html) resources.
* Added new blog post on 
  [The Best Resources for Developers to Learn Finance](/blog/best-resources-developers-learn-finance.html).

### February
* New [CSS](/cascading-style-sheets.html), [task queue](/task-queues.html)
  and [uWSGI](/uwsgi.html) resources.
* Added new Django code example pages:
    * [django.forms DateField](/django-db-models-datefield-examples.html)
    * [django.forms DateTimeField](/django-db-models-datetimefield-examples.html)
    * [django.forms TypedChoiceField](/django-db-models-typedchoicefield-examples.html)

### January
* Added new Django code example pages:
    * [django.db.models SmallIntegerField](/django-db-models-smallintegerfield-examples.html)
    * [django.urls.exceptions Resolver404](/django-urls-exceptions-resolver404-examples.html)
* Added starter pages for the remaining topics in the table of contents
  that were previously missing. Still working on adding more resources and
  descriptions to each page:
    * [Datadog](/datadog.html)
    * [GoCD](/gocd-continuous-integration.html)
    * [Salt](/salt.html)
    * [Sentry](/sentry.html)
* Happy New Year (and decade) to my fellow Python developers!


## 2019
### December
* 7 years of Full Stack Python as of December 23, 2019!
* Cleaned a bunch of dead links out thanks to 
  [PR #225](https://github.com/mattmakai/fullstackpython.com/pull/225).
* Merged [PR #224](https://github.com/mattmakai/fullstackpython.com/pull/224)
  with information and resources on the Masonite web framework for the
  [other web frameworks](/other-web-frameworks.html) page.
* Updated the [RQ](/redis-queue-rq.html) page with a couple of new fresh
  resources.
* Added new Django code example pages:
    * [django.db.models GenericIPAddressField](/django-db-models-genericipaddressfield-examples.html)
    * [django.db.models ImageField](/django-db-models-imagefield-examples.html)
    * [django.db.models PositiveIntegerField](/django-db-models-positiveintegerfield-examples.html)
    * [django.db.models PositiveSmallIntegerField](/django-db-models-positiveintegerfield-examples.html)
    * [django.db.models.related ForeignKey](/django-db-models-related-foreignkey-examples.html)
    * [django.forms EmailField](/django-forms-emailfield-examples.html)
    * [django.forms IntegerField](/django-forms-integerfield-examples.html)

### November
* Added new resources to [RQ](/redis-queue-rq.html), [Sanic](/sanic.html)
  and [networking](/networking.html) pages.
* Added new Django code example pages:
    * [django.forms BooleanField](/django-forms-booleanfield-examples.html)
    * [django.forms CharField](/django-forms-charfield-examples.html)
    * [django.forms ChoiceField](/django-forms-choicefield-examples.html)

### October
* Removed a bunch of outdated content from the 
  [best Python resources](/best-python-resources.html) page and
  added some nice new links to the mix.
* Published a new blog post tutorial on the 
  [String Data Type in Python 3](/blog/python-basic-data-types-strings.html).
* Added new Django code example pages:
    * [django.db.models FileField](/django-db-models-filefield-examples.html)
    * [django.db.models SlugField](/django-db-models-slugfield-examples.html)
* Updated code examples on the following pages:
    * [django.db.models TextField](/django-db-models-textfield-examples.html)
* Rewrote some parts of the [Python 2 or 3](/python-2-or-3.html) page to
  make it more clear that 3 is now the mandatory way to get started.
* Updated [best videos](/best-python-videos.html) page with new EuroPython links.

### September
* Added new Django code example pages:
    * [django.apps.config AppConfig](/django-apps-config-appconfig-examples.html)
    * [django.contrib.admin.sites register](/django-contrib-admin-sites-register-examples.html)
    * [django.db OperationalError](/django-db-operationalerror-examples.html)
    * [django.db.models AutoField](/django-db-models-autofield-examples.html)
    * [django.db.models DateField](/django-db-models-datefield-examples.html)
    * [django.db.models IntegerField](/django-db-models-integerfield-examples.html)
    * [django.http HttpResponse](/django-http-httpresponse-examples.html)
    * [django.http HttpResponseBadRequest](/django-http-httpresponsebadrequest-examples.html)
    * [django.http HttpResponseForbidden](/django-http-httpresponseforbidden-examples.html)
    * [django.http HttpResponseNotModified](/django-http-httpresponsenotmodified-examples.html)
    * [django.http HttpResponseRedirect](/django-http-httpresponseredirect-examples.html)
    * [django.template.response TemplateResponse](/django-template-response-templateresponse-examples.html)
    * [django.template.response SimpleTemplateResponse](/django-template-response-simpletemplateresponse-examples.html)
    * [django.urls reverse_lazy](/django-urls-reverse-lazy-examples.html)

### August
* Added stub page for [mod_wsgi](/mod-wsgi.html).
* Merged [PR #215](https://github.com/mattmakai/fullstackpython.com/pull/215)
  to fix a typo on the [serverless](/serverless.html) page. Thanks 
  [Kyle](https://github.com/kylekizirian)!
* Added new [Flask](/flask-code-examples.html) code examples:
    * [flask request](/flask-request-examples.html)
    * [flask redirect](/flask-redirect-examples.html)
* Added new [Django](/django-code-examples.html) code examples pages:
    * [django.contrib.auth get_user_model](/django-contrib-auth-get-user-model-examples.html)
    * [django.contrib.auth.decorators login_required](/django-contrib-auth-decorators-login-required-examples.html)
    * [django.contrib.auth.hashers make_password](/django-contrib-auth-hashers-make-password-examples.html)
    * [django.http Http404](/django-http-http404-examples.html)
    * [django.http.responses HttpResponsePermanentRedirect](/django-http-responses-httpresponsepermanentredirect-examples.html)
    * [django.urls.exceptions NoReverseMatch](/django-urls-exceptions-noreversematch-examples.html)
* Updated code examples on the following pages:
    * [django.contrib admin](/django-contrib-admin-examples.html)
    * [django.db.models DateTimeField](/django-db-models-datetimefield-examples.html)
    * [django.utils timezone](/django-utils-timezone-examples.html)

### July
* Pushed the [3000th commit](https://github.com/mattmakai/fullstackpython.com/commit/180051047a582b9154874b15dccb315600f23300)
  to Full Stack Python, a bit over 3 years after the
  [2000th commit](https://github.com/mattmakai/fullstackpython.com/commit/3baed0aa82e1b3b7fa0a337e91998018d62a0f23) 
  and 5ish years after the
  [1000th commit](https://github.com/mattmakai/fullstackpython.com/commit/2fc711b44ffed89c9855f4f999d4c1df076bc44d). Here's to the next 1,000 commits!
<img src="/img/visuals/3000th-commit.png" width="100%" alt="Screenshot of 3000th commit to Full Stack Python." class="shot rnd outl" />
* New blog post with slides and a loose transcript of my latest talk on
  [Developer-led sales for tech startups](/blog/developer-led-sales-startups.html).

### June
* Added a new page for 
  [Django BaseCommand code examples](/django-core-management-base-basecommand-examples.html).
* Started new open source code examples series, beginning with 
  [url](/django-conf-urls-url-examples.html)
  and [path](/django-urls-path-examples.html) functions.

### May
* Added new [data visualization](/data-visualization.html), 
  [web design](/web-design.html) and [pandas](/pandas.html) resources.
* Updated the subnav with a link to 
  [deploypython.com](https://www.deploypython.com/)
  and added a bunch of new resources across pages on the site.
* Rearrange parts of the [app dependencies](/application-dependencies.html)
  page to make it easier to read.
* Fix typos and broken internal links on site.

### April
* Added new [web frameworks](/web-frameworks.html), [d3.js](/d3-js.html)
  and [Django REST framework](/django-rest-framework-drf.html) resources.
* New [Stripe API](/stripe.html) resources.

### March
* Added new resources across the site and merged 
  [PR #206](https://github.com/mattmakai/fullstackpython.com/pull/206)
  with a new [Heroku](/heroku.html) page link.
* New resources on the [web analytics](/web-analytics.html) page.

### February
* Added a ton of resources on the [Kubernetes](/kubernetes.html) page.
* Removed many broken links thanks to 
  [pull request #205](https://github.com/mattmakai/fullstackpython.com/pull/205). 
  Thanks again [Sam](https://github.com/huangsam)!
* Add [uWSGI](/uwsgi.html) page with a few initial resources.
* Updated the [Neo4j](/neo4j.html) and [microservices](/microservices.html)
  pages with more resources.
* Added a bunch more [bots](/bots.html) resources.
* New [data](/data.html) and [data analysis](/data-analysis.html) resources
  added.
* Refreshed the [relational databases](/databases.html) page with new 
  resources and removed some out-of-date ones.

### January
* Merged [PR #202](https://github.com/mattmakai/fullstackpython.com/pull/202)
  to fix a typo on the [web frameworks](/web-frameworks.html) page.
* Updated the [source control](/source-control.html) page with more 
  resources.
* Added new post on the 
  [Introduction to Ansible video course launch](/blog/introduction-ansible-videos-released.html).
* Cleaned up a bunch of broken links thanks to 
  [pull request #198](https://github.com/mattmakai/fullstackpython.com/pull/198).
  Thanks again [Sam](https://github.com/huangsam)!
* Added new [MongoDB](/mongodb.html) resources.
* Updated the [Docker](/docker.html) page with new resources, removed old ones and
  added new descriptions to sections.
* Happy New Year!


## 2018
### December
* Added a ton of new resources and descriptions on the 
  [Cassandra](/apache-cassandra.html) page.
* 6 years of Full Stack Python as of December 23, 2018!
* Updated [SQLAlchemy](/sqlalchemy.html), [NoSQL](/no-sql-datastore.html),
  [MongoDB](/mongodb.html) and [Slack API](/slack.html) pages with
  new descriptions and resources.
* Updated the [serverless](/serverless.html), 
  [operating systems](/operating-systems.html) and
  [HTTPS](/https.html) pages with a bunch of new resources.

### November
* Updated the [logging](/logging.html), [Redis](/redis.html) and
  [PaaS](/platform-as-a-service.html) pages with a bunch of new resources.
* Updated the [web design](/web-design.html) page with new resources.
* Updated the [data visualization](/data-visualization.html) page with
  new resources.

### October
* Added new blog post on
  [Adding Okta Authentication to an Existing Flask Web App](/blog/okta-user-auth-existing-flask-web-app.html).
* Sent out a 
  [quick email newsletter update](/blog/fresh-tutorials-october-2018.html)
  about new recent tutorials on the blog.
* Added a bunch of new [testing](/testing.html) page resources.
* Published new post on 
  [How to Provision Ubuntu 18.04 LTS Linux Servers on DigitalOcean](/blog/provision-ubuntu-1804-linux-servers-digitalocean.html).
* Published a new blog post showing
  [How to Add User Authentication to Flask Apps with Okta](/blog/add-user-authentication-flask-apps-okta.html).
* Merge [PR #189](https://github.com/mattmakai/fullstackpython.com/pull/189)
  to help readers figure out how to get around some security warning issues
  that could come up in the 
  [Slack bot tutorial](/blog/build-first-slack-bot-python.html).
* Added even more new [debugging](/debugging.html) tutorials and split
  pdb tutorials into their own section.

### September
* A ton of new tools and links on the [debugging](/debugging.html) page.
* Added a starter [Django REST Framework](/django-rest-framework-drf.html) 
  page.
* New [web app security](/web-application-security.html), 
  [task queue](/task-queues.html) and [WebRTC](/webrtc.html) resources.
* Added a bunch of new resources across the site and removed a few out of
  date ones as well.
* Added initial pages for [WebRTC](/webrtc.html) and JavaScript frameworks.
  More resources coming to those pages soon.

### August
* Merged [PR #184](https://github.com/mattmakai/fullstackpython.com/pull/184)
  to remove link rot issues. Thanks again [Sam](https://github.com/huangsam)!
* New [RQ](/redis-queue-rq.html) and [code metrics](/code-metrics.html)
  resources.
* Updated the [Celery](/celery.html) page with a ton of new great
  resources and broke them into new subsections for general resources,
  frameworks and deployments.
* Tons of new [code metrics](/code-metrics.html), [Lektor](/lektor.html),
  [Pyramid](/pyramid.html) and [Sanic](/sanic.html) resources.
* Added new [Git](/git.html) and [Jinja](/jinja2.html) resources.
* Merged 
  [PR #182](https://github.com/mattmakai/fullstackpython.com/pull/182) 
  that updated the 
  [Ubuntu SSH Keys post](/blog/ssh-keys-ubuntu-linux.html)
  with the `-o` flag that mitigates an encryption vulnerability.
* Fixed 
  [issue #181](https://github.com/mattmakai/fullstackpython.com/issues/181)
  that identified a broken link on the [Twilio](/twilio.html) page.
* New [Markdown](/markdown.html) resources.

### July
* Added a bunch of new [PyCharm](/pycharm.html) resources.
* Merged [PR #177](https://github.com/mattmakai/fullstackpython.com/pull/177)
  that adds a new [Docker](/docker.html) Swarm tutorial.
* Merged [PR #176](https://github.com/mattmakai/fullstackpython.com/pull/176)
  to update the [Django](/django.html) page by removing some old links and
  adding newer ones.
* New section on [source control](/source-control.html) page and resources
  for mono vs multi repo debate.
* Added a new section and additional [Vim](/vim.html) links.
* Added even more [Emacs](/emacs.html) resources and a new section for Elisp
  resources, the programming language used to customize the editor.

### June
* Added new [Emacs](/emacs.html) resources and descriptions.
* Merged [PR #175](https://github.com/mattmakai/fullstackpython.com/pull/175)
  to fix changed URLs on [data analysis page](/data-analysis.html) where the
  authors did not use 301 redirects to the new pages. Thank you 
  [mbanerjeepalmer](https://github.com/mbanerjeepalmer)!
* Major updates on [development environments](/development-environments.html)
  and [text editors and IDEs](/text-editors-ides.html) pages.
* New resources on the [operating systems](/operating-systems.html) and
  [development environments](/development-environments.html) pages.
* New blog post on how to
  [Configure Python 3, Flask and Gunicorn on Ubuntu 18.04 LTS](/blog/python-3-flask-gunicorn-ubuntu-1804-bionic-beaver.html).
* New [d3.js](/d3-js.html) resources.
* Merged [PR #173](https://github.com/mattmakai/fullstackpython.com/pull/173)
  for new [Git](/git.html) page section. Modified wording a bit from original
  pull request. Thanks [Sam](https://github.com/huangsam)!
* Add even more descriptions and resources to the 
  [Python companies](/companies-using-python.html) page.
* Fix 
  [issue #172](https://github.com/mattmakai/fullstackpython.com/issues/172)
  where Atom and RSS feeds did not have `/blog/` in the URLs so they were 
  pointing to incorrect (broken) article locations.
* Further work on [companies using Python](/companies-using-python.html)
  page.

### May
* Merged [PR #169](https://github.com/mattmakai/fullstackpython.com/pull/169)
  that cuts down on redirects to the new PyPI site. Thank you Sam!
* Merged [PR #168](https://github.com/mattmakai/fullstackpython.com/pull/168),
  which contained links to a great blog post on [Flask](/flask.html) by
  [TestDriven.io](https://testdriven.io/).
* New blog post on 
  [How to (Appropriately) Explain Your Product to Software Developers](/blog/explain-products-developers.html)
  that is based on a talk I gave in Silicon Valley.
* Added a bunch of great [podcast](/best-python-podcasts.html) episodes
  to that page.
* Merged [PR #166](https://github.com/mattmakai/fullstackpython.com/pull/166)
  and [PR #167](https://github.com/mattmakai/fullstackpython.com/pull/167) to
  update the URL scanning script as well as remove all 404 links. Thanks Sam!
* New blog post on 
  [How to Add Maps to Django Web App Projects with Mapbox](/blog/maps-django-web-applications-projects-mapbox.html).
* Updated with a slew of new [serverless](/serverless.html), 
  [static site generators](/static-site-generator.html),
  [Bokeh](/bokeh.html) and [community](/python-community.html) resources.
* Major update to [Python 2 or 3](/python-2-or-3.html) page with better 
  explanations that match community opinions in 2018 (originally page was
  written in 2016 and descriptions were not heavily modified enough since 
  then), along with a slew of new migration resources.
* Added [newsletter on PyCon US 2018](/full-stack-python-pycon-us-2018.html).
* New [podcast](/best-python-podcasts.html) resources.
* Merge 
  [pull request #164](https://github.com/mattmakai/fullstackpython.com/pull/164)
  with a new [task queues](/task-queues.html) resource.

### April
* New blog post on adding [Rollbar](/rollbar.html) for
  [Monitoring Python 3.6 Functions on AWS Lambda](/blog/monitor-python-3-6-example-code-aws-lambda-rollbar.html).
* New [TurboGears](/turbogears.html) web framework page via 
  [pull request #162](https://github.com/mattmakai/fullstackpython.com/pull/162).
  Thank you [Alessandro](https://github.com/amol-)!
* A slew of new resources and descriptions for the 
  [Jupyter Notebook](/jupyter-notebook.html) page.
* Reworking [web development](/web-development.html) page with new
  descriptions and resources.
* Major updates to [Flask](/flask.html) resources, example code and 
  descriptions.
* More broken or expired link clean up.

### March
* Fixed up a slew of link rot across the site.
* New resources on the [Pelican](/pelican.html) static site generator
  page.
* Added starter pages for [localhost tunnels](/localhost-tunnels.html), 
  [virtual environments (virtualenvs)](/virtual-environments-virtualenvs-venvs.html),
  and [environment variables](/environment-variables.html).
* Revamped the [table of contents / all topics](/table-of-contents.html) 
  to match vision for the site.
* New resources and explanations added to the [Markdown](/markdown.html) 
  page.
* New blog post on 
  [Developing Flask Apps in Docker Containers on macOS](https://www.fullstackpython.com/blog/develop-flask-web-apps-docker-containers-macos.html).
* Merged 
  [pull request #156](https://github.com/mattmakai/fullstackpython.com/pull/156)
  to remove a duplicated [Vim](/vim.html) page resource. Thanks 
  [Xurxo](https://github.com/xurxof)!
* New blog post on 
  [ReportLab and Future Community Project Launches](/blog/python-community-project-launches.html)
  that also went out as an email newsletter for March.
* Added new [learning programming](/learning-programming.html) practice 
  problem sets.
* Merged [PR #154](https://github.com/mattmakai/fullstackpython.com/pull/154)
  with a new [RQ](/redis-queue-rq.html) resource. Thanks again 
  [Michael](https://github.com/mjhea0)!

### February
* Merged [PR #153](https://github.com/mattmakai/fullstackpython.com/pull/153)
  that removed some out-of-date links and added some new ones to the 
  [Flask](/flask.html) page.
* Added a slew of new practice problems and teaching resources on the 
  [Learning Programming](/learning-programming.html) page.
* New [WebSockets](/websockets.html) resources.
* New starter page on [CSS frameworks](/css-frameworks.html) and 
  [Foundation CSS](/foundation-css.html).
* New 
  [blog post on adding Rollbar monitoring to Django applications](/blog/monitor-django-projects-web-apps-rollbar.html).
* Added new [enterprise Python](/enterprise-python.html) resources.

### January
* Incorporated new data from Stack Overflow and updated programming language
  rankings as evidence of reasons for 
  [why to use Python](/why-use-python.html).
* Merged [PR#151](https://github.com/mattmakai/fullstackpython.com/pull/151)
  that fixed an issue with the Slack bot and URLs in conversations.
* Merged [PR#148](https://github.com/mattmakai/fullstackpython.com/pull/148)
  that added a health check script. Fixed all URLs raised as issues with
  link rot, expired domains and redirects. Thanks 
  [Samuel](https://github.com/huangsam)!
* Add [Ansible](/ansible.html), [Matplotlib](/matplotlib.html),
  [PowerShell](/powershell.html), [tmux](/tmux.html), [Screen](/screen.html),
  [Pymux](/pymux.html), [PyCharm](/pycharm.html) and 
  [terminal multiplexers](/terminal-multiplexers.html) starter pages with 
  a few links, to be fleshed out later.
* New [Redis](/redis.html) and [Ubuntu](/ubuntu.html) resources.
* Happy New Year! This is the 6th year of Full Stack Python, coming after a
  wonderful [first five years](/blog/five-years-full-stack-python.html).

## 2017
### December
* Passed 1,000,000 characters written on Full Stack Python according to 
  [wc](https://stackoverflow.com/questions/25348406/whats-is-the-behaviour-of-the-wc-command) 
  on my [Markdown](markdown.html) content files. It's a super arbitrary but 
  fun little milestone.
* Removed a couple of [Best Python Resources](/best-python-resources.html)
  and added new resources to the [Morepath](/morepath.html) page.
* Added a ton of new [SQLite](/sqlite.html) resources.
* Cleaned up broken and redirected links on all pages including blog posts.
* Added [5 years of Full Stack Python](/blog/five-years-full-stack-python.html)
  retrospective blog post.
* Merged [PR#147](https://github.com/mattmakai/fullstackpython.com/pull/147) to
  fix an issue installing [MySQL](/mysql.html) server package.
* Major performance improvements by reducing all page sizes by 15-20%. Split apart
  the CSS, tuned it and minified the classes.
* Merged pull request for
  [How to Build Your First Slack Bot with Python](/blog/build-first-slack-bot-python.html)
  tutorial from Slack dev advocates because bot building has changed since
  I originally wrote the post with custom integrations. Thanks Ankur and Bear!
* Added new blog post based on latest email newsletter on
  [GitPython and new Git tutorials](/blog/gitpython-git-tutorials.html).
* Working on revamping older pages such as [Django](/django.html) by 
  eliminating outdated resources and adding the latest and greatest.
* Removing <a href="http://www.deploypython.com/">Guide to Deployments</a> 
  links until the next version is out (estimated Spring 2018 after 
  Ubuntu 18.04 LTS releases).
* Crossed the 120k words mark for content, thanks to a slew of new tutorials 
  and pages.
* New [serverless](/serverless.html) and 
  [AWS Lambda](/aws-lambda.html) resources.
* Merged [PR#144](https://github.com/mattmakai/fullstackpython.com/pull/144)
  which fixes an issue with the wrong `psql` command in the blog post on 
  [Setting up PostgreSQL with Python 3 and psycopg on Ubuntu 16.04](/blog/postgresql-python-3-psycopg2-ubuntu-1604.html).

### November
* New blog post on 
  [First Steps with GitPython](/blog/first-steps-gitpython.html).
* Added new 
  [blog post for latest newsletter on "DevOps, Thank You Maintainers and Contributing to Open Source"](/blog/devops-python-maintaining-contributing-open-source.html).
* Cleaned up some unfortunately broken links to websites that now 404.
* Merge [PR#143](https://github.com/mattmakai/fullstackpython.com/pull/143)
  to create new [Dramatiq](/dramatiq.html) task queue starter page.
* New 
  [blog post based on my DevOps, Continuous Delivery... and You talk](/blog/devops-continuous-delivery-you.html)
  with the slides and rough transcript from the sessions.

### October
* New resources on the [SQLite](/sqlite.html) and [Vim](/vim.html) pages.
* New [shells](/shells.html), [Bash](/bourne-again-shell-bash.html) 
  and [Zsh](/zsh-shell.html) starter pages.
* Added blog post version of mid-October email newsletter 
  [PyCon US 2018 CFP, Python Bytes and Pelican](/blog/pycon-us-2018-cfp-python-bytes-pelican.html).
* New starter page for [Rollbar](/rollbar.html) as part of the hosted
  monitoring services series.

### September
* New blog post on 
  [Monitoring Python Web Apps](/blog/monitor-python-web-applications.html)
  that uses [Bottle](/bottle.html) as the example 
  [web framework](/web-frameworks.html) with a simple application.
* New short blog post showing how to 
  [Provision Ubuntu 16.04 Linux Servers on Linode](/blog/provision-ubuntu-linux-servers-linode.html).
* Added new [minification](/minification.html) and 
  [data analysis](/data-analysis.html) starter pages.
* Modifying and favoring links to original sources rather than Medium links
  due to their new pop-ups that are really annoying for readers, especially
  when you're in the middle of trying to figure out a solution to a coding
  problem.

### August
* Updated subnav with a link to [changelog](/change-log.html).
* Added [d3.js](/d3-js.html) starter page.
* Added [responsive design](/responsive-design.html) starter page.
* Updated the [Redis](/redis.html) page with loads of new resources.
* New [Neo4j](/neo4j.html) starter page.
* Loads of new [Bokeh](/bokeh.html) resources and some new descriptions.
* Split out from the [ORMs](/object-relational-mappers-orms.html) and created 
  dedicated pages for [Django ORM](/django-orm.html),
  [Pony](/pony-orm.html) and [SQLObject](/sqlobject.html). Also included 
  updated resources for each page.
* Added new [page statuses](/page-statuses.html) by chapter to make it easier
  to track what's being worked on.
* Updated [future directions](/future-directions.html) with more context on
  page maturity.
* New starter pages for [Companies Using Python](/companies-using-python.html)
  and [Sublime Text](/sublime-text.html).
* New [Python 2 or 3?](/python-2-or-3.html) resources.
* Fixed diagram mistake on [Peewee](/peewee.html) ORM page that was 
  referencing SQLAlchemy instead of Peewee.

### July
* Added new 
  [Bokeh+Bottle bar charts post](/blog/python-bottle-bokeh-bar-charts.html)
  blog post.
* Added a way to highlight blog post code changes such as in the new
  [monitoring Flask apps](/blog/hosted-monitoring-flask-web-apps.html) post
  under the "Handling Errors" section.
* Added new blog post on how to
  [monitor Flask applications](/blog/hosted-monitoring-flask-web-apps.html).
* Fixed a typo in the 
  [Make Phone Calls in Python](/blog/make-phone-calls-python.html) 
  blog post thanks to my [colleague Greg Baugues'](http://baugues.com/) 
  sharp eyes. 

### June
* New blog post on 
  [How to Create Your First Static Site with Pelican and Jinja2](/blog/generating-static-websites-pelican-jinja2-markdown.html).
* Updates to [Twilio](/twilio.html) and [Pelican](/pelican.html) pages
  with more resources.

### May
* New [Falcon](/falcon.html) page to round out web frameworks pages.
* Major updates to the [WebSockets page](/websockets.html) with new Python
  projects, explanations and resources.
* New blog post with my answer to the question of 
  [How to become a successful self-taught professional software developer](/blog/become-successful-self-taught-software-developer.html).
* New very short stub page for [Google Cloud Functions](https://www.fullstackpython.com/google-cloud-functions.html). 
  Hopefully they add proper Python support to their platform soon.

### April
* Updated many existing blog posts with fixes based on reader feedback
  and re-ran them to check what changes were needed.
* New [Serverless compute](/serverless.html) concept page.
* Two new blog posts, one for 
  [Python 2.7 on AWS Lambda](/blog/aws-lambda-python-2-7.html) 
  and another on
  [Python 3.6 on AWS Lambda](/blog/aws-lambda-python-3-6.html). Also
  added a page for [AWS Lambda](/aws-lambda.html).
* Updated [Apache Cassandra page](/apache-cassandra.html) with a slew of
  new general and Python-specific resources.
* New [Pelican](/pelican.html) resources.
* Updated some of the [blog post tutorials](/blog.html) (they are marked 
  by updated dates) to fix issues with the steps or provide newer versions
  of libraries like [Green Unicorn](/green-unicorn-gunicorn.html)
  and operating systems such as [Ubuntu](/ubuntu.html).
* Added new [continuous integration](/continuous-integration.html) resources.
* New [PostgreSQL](/postgresql.html) page resources.

### March
* Pushed the [2000th commit](https://github.com/mattmakai/fullstackpython.com/commit/3baed0aa82e1b3b7fa0a337e91998018d62a0f23) 
  to Full Stack Python, just under 2 years after the 
  [1000th commit](https://github.com/mattmakai/fullstackpython.com/commit/2fc711b44ffed89c9855f4f999d4c1df076bc44d). Here's to the next 1,000 commits!
<img src="/img/visuals/2000th-commit.jpg" width="100%" alt="Screenshot of 2000th commit to Full Stack Python." class="shot rnd outl" />
* Added new [PostgreSQL](/postgresql.html) and [SQLAlchemy](/sqlalchemy.html)
  resources.
* New [Git](/git.html) resources.

### Feburary
* Add [generating SSH keys on macOS Sierra](/blog/ssh-keys-macos-sierra.html) 
  blog post.
* Removed all external CSS file loads and reduced the CSS for all pages and 
  posts to the minimum amount required for that specific page.
* Major performance improvements across the site by reducing CSS load
  and reducing image sizes.
* Added blog post on 
  [Creating SSH Keys on Ubuntu Linux 16.04 LTS](/blog/ssh-keys-ubuntu-linux.html).

### January
* New [Sanic](/sanic.html) stub page.
* New [Celery](/celery.html) resources.
* Added [RQ](/redis-queue-rq.html) stub page.
* Broke out [Celery](/celery.html) into its own page and cleaned up 
  [task queue](/task-queues.html) resources.
* Buffed up the number of [MongoDB](/mongodb.html) resources.
* Added more specific web frameworks such as Sanic and Tornado to the 
  [table of contents](/table-of-contents.html). Pages will be created later.
* Break out [Jenkins](/jenkins.html) page from 
  [continuous integration](/continuous-integration.html) page origins.
* Major update made to the [template engines](/template-engines.html) page 
  with a bunch of new resources and explanations.
* Added stub [Apache Cassandra](/apache-cassandra.html) page with a few
  resources.
* New [Redis](/redis.html) and [MongoDB](/mongodb.html) pages.
* Further work on the [Git](/git.html) page.
* New [Git](/git.html) page.
* New resources and descriptions on the 
  [development environments](/development-environments.html) page.
* New [static site generator](/static-site-generator.html) resources added.
* Added new resources to the [Python 2 or 3?](/python-2-or-3.html) page.
* Fixed all 404 link rot on every page. However, if a page has been rewritten
  or redirected and is no longer valuable as a link, please 
  [tweet me](https://twitter.com/fullstackpython) or 
  [file an issue ticket on GitHub](https://github.com/mattmakai/fullstackpython.com/issues).
* New [Why Python?](/why-use-python.html) resources.
* Happy New Year!


## 2016
### December
* Crossed 800,000 readers so far in 2016!
* Added a small [MkDocs](/mkdocs.html) page that needs to be expanded.
* Updated the [Nginx](/nginx.html) page with a better description of reverse
  proxies.
* Add new [Lektor](/lektor.html) page. Will be expanded upon during the
  month as I get to use the library.
* Merged [PR #111](https://github.com/mattmakai/fullstackpython.com/pull/111)
  that fixed some typos on the [Django](/django.html) page, added clarity to 
  a Django Channels statement and provided a new Django resource.

### November
* New blog post on 
  [How to Make Phone Calls in Python](/blog/make-phone-calls-python.html)
  that does not rely on a web framework for HTTP POST responses.
* Merge [PR #110](https://github.com/mattmakai/fullstackpython.com/pull/110)
  to add the new task queue project Kuyruk to the 
  [task queues](/task-queues.html) page.

### October
* Rearranged the individual pages and their meta to match the new
  [table of contents](/table-of-contents.html).
* Upgrades to the [Peewee](/peewee.html) page with more descriptions and 
  resources.
* Added new [Peewee ORM](/peewee.html) page.
* Added new [SQLAlchemy ORM](/sqlalchemy.html) page.
* Updated [all topics / table of contents](/table-of-contents.html) page 
  to show future topics I am working to create.
* Added stub page that needs to be expanded for 
  [Python Community](/python-community.html).
* New resources on the [DevOps](/devops.html) page.

### September
* Broke out [Pelican](/pelican.html) into its own page and added new content
  that was not previously found on the 
  [static website generators](/static-site-generator.html) page.
* Removed a ton of unnecessary CSS to make page loads faster.
* Added new resources to the [Python 2 or 3?](/python-2-or-3.html) page.
* New update to the 
  [Full Stack Python Guide to Deployments book](http://www.deploypython.com/)
  released!
* Updated the [Slack bot tutorial](/blog/build-first-slack-bot-python.html)
  with a new bit on how to solve a common issue when the bot does not seem
  to be responding to `@` mentions due to a missing colon in the input.
* New resources on the 
  [static site generators](/static-site-generator.html)
  page focusing on deploying a static site.

### August
* Added a new blog post on 
  [Dialing Outbound Phone Calls with a Bottle Web App](/blog/dial-outbound-phone-calls-python-bottle.html).
* Merged several pull requests such as 
  [#106](https://github.com/mattmakai/fullstackpython.com/pull/106) which
  fixed some bad errors on my part. Pull requests are amazing!
* Finished the hugely successful 
  [Python for Entrepreneurs Kickstarter campaign](https://www.kickstarter.com/projects/mikeckennedy/python-for-entrepreneurs-video-course).
  Thank you to everyone who contributed as a backer and supporter! Michael
  and I can't wait to get this new video course out to everyone.
* Updates with new resources on the [API Creation](/api-creation.html)
  and [development environments](/development-environments.html) pages.
* Added a [Twilio API](/twilio.html) page to the APIs chapter. May add more
  pages that provide Python guidance for using popular APIs like Slack,
  Google, Sendgrid, etc.
* Updated GitHub username references to 
  [mattmakai](https://github.com/mattmakai) from makaimc (old username).
* Additional [Bottle](/bottle.html) resources.
* New [Vim](/vim.html) resources.
* Made a slew of improvements and added more resources to the 
  [Python 2 or 3?](/python-2-or-3.html) page.

### July
* New blog post with some background information on the 
  [Python for Entrepreneurs Kickstarter](/blog/python-entrepreneurs.html).
* Launched a 
  [Kickstarter with Michael Kennedy to create a Python for Entrepreneurs](https://www.kickstarter.com/projects/mikeckennedy/python-for-entrepreneurs-video-course)
  video course!
* Added new [Why Use Python](why-use-python.html) resources to that page.
* Updated the [NoSQL](/no-sql-datastore.html) page with a couple of new
  resources.

### June
* Added another new blog post, this time on 
  [Setting Up Python 3, Django & Gunicorn on Linux Mint 17.3](/blog/python-3-django-gunicorn-linux-mint-17.html).
* New blog post for 
  [Configuring Python 3, Pyramid and Gunicorn on Ubuntu](/blog/python-3-pyramid-gunicorn-ubuntu-1604-xenial-xerus.html).
* Created little images for each of the posts on the 
  [blog post list page](/blog.html).
* Start of new page on [Ubuntu](/ubuntu.html).
* Two new tutorial blog posts: 
  [How to Build Your First Slack Bot with Python](/blog/build-first-slack-bot-python.html) 
  and
  [Replying to SMS Text Messages with Python and Bottle](/blog/reply-sms-text-messages-python-bottle.html).
* New [PostgreSQL](/postgresql.html) monitoring resources.

### May
* New [SQLite](/sqlite.html) resources.
* Removed or redirected a few broken links on various deployment pages.
* One more new blog post tutorial before the month ends: 
  [Responding to SMS Text Messages with Python & Flask](/blog/respond-sms-text-messages-python-flask.html).
* Added bunches of new content and links to the [MySQL](/mysql.html) page.
* Redirected several links that were still available but changed URLs.
  Make sure to 301 Redirect your old links that still have traffic! :)
* Fixed a few broken and old links throughout the site. Darn link rot.
* New blog post published: 
  [How to Use Redis with Python 3 and redis-py on Ubuntu 16.04](/blog/install-redis-use-python-3-ubuntu-1604.html).
* Added fifth blog post, this time on [Sending MMS Picture Messages with Python](/blog/send-mms-picture-messages-python.html).
* Two new tutorial blog posts: 
  [How to Send SMS Text Messages with Python](/blog/send-sms-text-messages-python.html)
  and
  [Configuring Python 3, Bottle and Gunicorn for Development on Ubuntu 16.04 LTS](/blog/python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus.html).
* Wrote another blog post, this time on 
  [How to set up Python 3, Flask and Green Unicorn on Ubuntu 16.04 LTS](/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html).
* Wrote a new [blog post](/blog.html) on 
  [Setting up Python 3, Django and Gunicorn on Ubuntu 16.04 LTS](/blog/python-3-django-gunicorn-ubuntu-1604-xenial-xerus.html).
* Added new resources to the [Vim](/vim.html) and [Emacs](/emacs.html)
  pages.
* New [Green Unicorn (Gunicorn)](/green-unicorn-gunicorn.html) page added.
  Still a bit sparse at the moment but starting to get filled in.

### April
* Updated the [Nginx](/nginx.html) page with a security section.
* Added new Channels section to [Django](/django.html) page.
* Clean up on some existing pages to remove broken links.
* Added new subnav under the logo and title so readers can more easily 
  access the [table of contents](/table-of-contents.html).

### March
* Added new [DevOps](/devops.html) resources.
* Removed unfortunate dead links from the [Django](/django.html) page.
* Made a huge improvement to the layout of the full-sized table of contents
  that appears on pages that are above 768px wide (the collapsed table of
  contents for mobile stays the same).
* Began work on an [Apache HTTP Server page](/apache-http-server.html).
* Added some new awesome [deployment](/deployment.html) resources.

### February
* Added a new section for [Python images within Docker containers](/docker.html).
* Added a couple of new resources to the [WebSockets](/websockets.html) page.

### January
* Added initial page for [SQLite](/sqlite.html) that will be built out over
  the next few weeks.
* Added a couple of new resources to the 
  [ORMs](/object-relational-mappers-orms.html)
  page.
* More resources on the [PostgreSQL page](/postgresql.html) and now grouped
  into Python-specific and general sections.
* Major update to [relational databases](/databases.html) page with new
  sections and resources.
* Updated the [Jinja2](/jinja2.html) page with new sections and resources.
  Also added a new tutorial link on the [Bottle](/bottle.html) page.
* Added new summaries and links to the [Docker](/docker.html) and 
  [Best Python Resources](/best-python-resources.html) pages.
* Expanding the [PostgreSQL](/postgresql.html) page with more detail and
  additional resources.
* Split the [relational databases](/databases.html) page sections on
  [PostgreSQL](/postgresql.html) and [MySQL](/mysql.html) out into their
  own pages so there is more room to write about the three topics without
  making the databases page a behemoth.
* Updated the [template engines](/template-engines.html) page with a new image
  to show the spectrum between arbitrary code execution and no logic in templates.
* Added a new [Jinja2](/jinja2.html) page specifically for that template engine.
* Happy New Year! Finished 2015 with over 455,000 users according to Google 
  Analytics. Thanks everyone! Can't wait to write more pages and improve the
  existing ones in 2016.

## 2015
### December
* Started on a [DevOps](/devops.html) page and began adding basic resources
  to it.
* Added new section on "Python for specific occupations" to the 
  [best resources page](/best-python-resources.html).
* New [web development](/web-development.html) resources.
* Released the December update to 
  [The Full Stack Python Guide to Deployments](http://www.deploypython.com/) 
  book with additional polish based on reader feedback.
* Added new resources to the [API creation](/api-creation.html), 
  [comprehensions](/comprehensions.html) and 
  [development environments](/development-environments.html) pages.
* New resources and a new basic page on the 
  [Python programming language itself](/python-programming-language.html).
* Added new starter projects to the [Flask](/flask.html) page.

### November
* Started a new page for [template engines](/template-engines.html). Needs some
  more writing and resources.
* Working on a page for the umbrella [web development](/web-development.html)
  concept, but it's early days as I'm trying to figure out how to be clear
  and concise about this broad topic.
* Merged 
  [pull request #70](https://github.com/mattmakai/fullstackpython.com/pull/70)
  and fixed some other issues that were in tickets.
* Made more updates to the static site generators page based on
  [feedback from folks on the /r/python subreddit](https://www.reddit.com/r/Python/comments/3rnkm9/an_overview_of_python_static_site_generators/).
* Updated the [static site generators](/static-site-generator.html) page
  with a better explanation of why they are useful.

### October
* Starting a [microservices](/microservices.html) page with some basic
  definitions and resources.
* Added a new resource to the [Enterprise Python](/enterprise-python.html) 
  page.

### September
* Updated the project templates section on the [Django page](/django.html).
* Added [API creation](/api-creation.html) resources.
* A new update for 
  [Full Stack Python Guide to Deployments](http://www.deploypython.com/)
  went out to existing purchasers!

### August
* Created new pages for [unit testing](/unit-testing.html) and 
  [integration testing](/integration-testing.html).
* Created a new page on [testing](/testing.html) that will be fleshed out
  over the next few weeks.
* Added new [Django](/django.html) resources, especially for migrations.
* Added new [web app security](/web-application-security.html) resources on
  HTTPS.

### July
* Updated a boatload of pages with typo and grammar fixes while reviewing
  everything for the upcoming launch of 
  [the PDF version of FSP contained in the packaged book deal](https://gumroad.com/l/WOvyt).
* Added the beginnings of a 
  [static site generator page](/static-site-generator.html).
* Updated sidebar with links to the new 
  [Full Stack Python Guide to Deployments](https://gumroad.com/l/kwjLZ)
  ebook.
* New resources on the [web frameworks](/web-frameworks.html) and 
  [Morepath](/morepath.html) pages.

### June
* New [API Creation](/api-creation.html) and [Django](/django.html) resources
  added.
* Added new Peewee resources on the 
  [ORMs page](/object-relational-mappers-orms.html).
* Nice little update to the [ORMs page](/object-relational-mappers-orms.html)
  with a diagram showing that different ORMs can work with varying
  web frameworks and backends.
* Added a new section just for Nginx resources and Removed broken links on 
  the [web servers](/web-servers.html) page.
* Added a new page on Python
  [object-relational mappers](/object-relational-mappers-orms.html), which
  helped condense that information on a single page and lighten the loads on
  the Django and relational databases pages.
* Added new page with a little advice on 
  [learning programming](/learning-programming.html).
* Proofread and tweaked the [web frameworks](/web-frameworks.html) page.
* Added a new section entitled "Do I have to use a web framework?" to the
  [web frameworks](/web-frameworks.html) page.
* Reviewed and updated the [introduction](/introduction.html) with slight
  modifications.
* Added new [Docker](/docker.html) resources.
* Made some changes to what is contained in the Markdown files versus the
  HTML Jinja2 templates. Behind the scenes work that needed to be done to
  move the project forward.
* Work continues on the 
  [Full Stack Python Guide to Deployments](http://www.deploypython.com/) book.

### May
* Got a whole lot of work done on my upcoming 
  [Full Stack Python Guide to Deployments](http://www.deploypython.com/) book.
  Very close to releasing it (looking at mid-June).
* Added new [Django](/django.html) resources, especially around migrations
  in Django 1.7+.
* Worked on making [Why Use Python?](/why-use-python.html) page specific to
  that topic now that the [Enterprise Python](/enterprise-python.html) page
  contains enterprise-y info.
* New page on the super broad topic of [Data](/data.html) with Python.
  Eventually it'll link to all sorts of data topics such as analysis,
  visualization and processing.
* New page on [Enterprise Python](/enterprise-python.html). A bit op-ed-ish
  perhaps, but I think it captures some of the spirit of the open source
  ecosystem with regards to Python for enterprise software development.
* Added additional [Django](/django.html) resources, specifically related to
  testing.

### April
* Added more [NoSQL resources](/no-sql-datastore.html), especially ones involving
  Redis.
* New [Pyramid](/pyramid.html) resource where the primary author is 
  interviewed about the web framework.
* New [Vim](/vim.html) resources.
* Updated the [Django](/django.html) page with new resources. The page is
  getting unwieldy at its current size so I'll likely pare it down with
  better categorizes sometime soon.
* Added new resources on the [Flask](/flask.html) page.

### March
* Added new [source control](/source-control.html) resources.
* Major site performance improvements. I removed font awesome and replaced
  icons with SVG elements that mimic the font awesome icons.
* Pushed the [1000th commit](https://github.com/mattmakai/fullstackpython.com/commit/2fc711b44ffed89c9855f4f999d4c1df076bc44d) 
  to Full Stack Python!
<img src="/img/visuals/1000th-commit.jpg" width="100%" alt="Screenshot of 1000th commit to Full Stack Python." class="shot rnd outl" />
* Major update to [Vim](/vim.html) page to add screenshots, a better example
  .vimrc configuration and many more resources.
* Updated the [web analytics](/web-analytics.html) page with a new 
  Python-specific section for walkthroughs that are specific to building or
  using analytics with Python applications.
* Adding a slew of new [Django](/django.html) resources.
* Working on including Crossbar.io and Autobahn to the 
  [websockets](/websockets.html) page.
* Added the Muffin framework to the 
  [other web frameworks](/other-web-frameworks.html) page.
* Added new [Emacs](/emacs.html) page based on 
  [pull request #49](https://github.com/mattmakai/fullstackpython.com/pull/49) 
  base information. Thank you!
* Added a new page on [best Python videos](/best-python-videos.html) that 
  breaks out all the videos I had scattered around the site and puts the
  best ones in a single place.
* Beefing up the Django resources and will soon break them further down 
  into subcategories so they are easier to find by topic.

### February
* Cleaned up the sidebar and [email](/email.html) subscribe messaging.
* Added new [monitoring](/monitoring.html), [websockets](/websockets.html) and
  [continuous integration](/continuous-integration.html) resources.
* New [Django](/django.html) resources.
* Updated the [Vim](/vim.html) page with a Vimrc configuration file 
  explanation along with Vimrc resources.
* Added a [generators](/generators.html) page that's mostly a stub that I will
  be building out to explain this core language feature.
* Updated [table of contents](/table-of-contents.html) with new layout that'll
  allow me to expand on core Python language topics.
* Updated several out of date resources and added a new 
  [logging](/logging.html) resource.
* New [Pyramid](/pyramid.html) resources. I definitely need to flesh that page
  out further.
* Added a [Vim](/vim.html) page and resources for learning Vim as a Python
  code editor.
* Reorganized content pages to make for better logical groupings as I add new
  content.
* Major improvements to [Websockets](/websockets.html) page after suggestions
  from 
  [issue #47 on GitHub repository](https://github.com/mattmakai/fullstackpython.com/issues/47).

### January
* Rewrote the Mailchimp sign up form for the email list so it doesn't have
  the external JQuery libraries as dependencies. Site should be even faster
  now.
* Stripped a significant portion of unused Bootstrap boilerplate from the CSS
  file and minified it. The resulting CSS file is over 100KB less (about
  25KB down from 130KB) so the site should load faster now.
* Major update to [WebSockets page](/websockets.html) with new diagrams 
  and better explanations for why server push is useful.
* New task queue resources.
* Major update with the beginning of a page on [Docker](/docker.html), split
  out static file handling resources on the [Django](/django.html) page
  and a new section on Python programming language popularity on the 
  "Why Use Python?" page.
* Working on a [Why Use Python?](/why-use-python.html) page with my own 
  assessment of the strengths and weaknesses of Python along with links to 
  resources where other folks discuss their own experiences.
* Continuing to add WebSockets resources, especially Python-specific ones.
* Added a new separate page for the [Morepath framework](/morepath.html).
* Updated the [future directions](/future-directions.html) page for 2015.
* Added new WebSockets resources.
* Added [WebSockets](/websockets.html) page and some initial resources.


## 2014
### December
* Added new security resources and splitting HTTPS resources into their own
  section.
* Split out Djangular resources into a separate section.
* New NoSQL Python client resources.
* Added new API resources for integration and creation.

### November
* Added a nice new continuous integration diagram.
* More Django and database resources.
* Revising development environments page and adding new resources.
* Adding my new Flask blog post on choose your own adventure presentations
  along with the open source repository.
* More resources under Best Python Resources.
* Removing broken links from Best Python Resources and Django pages.
* New monitoring and development environments resources.

### October
* Added the first new page in awhile! All about 
  [development environments](/development-environments.html).
* Always adding new links to the best resources. More resources for 
  deployments, web analytics and Flask.
* More API creation and consumption resources.
* Merged a bunch of pull requests that cleaned up spelling and grammar
  errors. Thank you contributors!
* Adding new Django 1.7-specific resources section on the Django page.
* New web frameworks, Bottle and Flask resources.

### September
* New resources for Flask, Django and task queues sections.
* A few new resources for NoSQL data stores.

### August
* New interesting link for web framework code complexity visualizations.
* Merged pull request that fixed some issues on WSGI page.
* Updated table of contents so it's easier to read and broken down by 
  sections.
* Added new [Web Design](/web-design.html) page to cleanly separate CSS from
  design topics and resources.
* New resources for code metrics and NoSQL databases.
* Added another Flask open source example app.
* Added new [Code Metrics](/code-metrics.html) page.
* Updated CI page with more services and open source projects.
* Added [Continuous Integration](/continuous-integration.html) page.
* Splitting out deployment from automation so I can add chapters on continuous
  integration, configuration management (which will be moved from the 
  existing deployment chapter) and related topics.
* Small tweaks to NoSQL, introduction and a few other pages.
* Moved topics map from introduction page to deployment page.

### July
* Merged pull request for Django page and updated Django page with project 
  template section.
* New Django example project resources.
* Rewrote parts of source control and CSS pages for clarity.
* Merged typo fixes PR #32.
* Added my Full Stack Python video from the EuroPython 2014 conference.
* Updated map with further details.
* Added a map to the front page. May move that elsewhere later though based
  on feedback.
* Merged a pull request for new REST frameworks.
* Lots of new Django, Flask and task queue resources.
* Added two new Python libraries lists to the Best Python Resources page.
* Thanks [Hacker News](https://news.ycombinator.com/item?id=7985692) for
  doubling my traffic so far in 2014! 65k uniques and counting...

### June
* Added more monitoring and logging resources.
* New resources for Flask and NoSQL projects.
* Updated NoSQL data store page with specific open source projects.
* Added diagram to source control page.
* Split version control resources from Git resources. Added new version
  control resources.
* Updated logging page with better explanations and content ordering.
* Added learning checklists for all sections. The remaining sections that now
  also have checklists are logging, web analytics and web application security.

### May
* Added link to my O'Reilly Programming blog post on demand for full stack 
  developer capabilities.
* Updated APIs page with basic information on webhooks.
* Added learning checklists for source control, application dependencies,
  configuration management, NoSQL data stores, APIs, API integration, 
  API creation, static content and caching sections.
* Moving learning checklists to the bottom of the pages since they are 
  specific advice for steps to take after reading a section.
* Added a stub section for APIs.
* Cleaned up and polished the task queues and web analytics pages.
* Added learning checklist to operating systems, web servers, task queues,
  monitoring pages and WSGI servers.
* Adding more logging resources.
* Continuing to add learning checklists to sections such as servers.
* Moving navigation options into meta tags on markdown pages.

### April
* Adding the concept of "learning checklists" to web frameworks, Django, CSS
  and JavaScript pages to give readers some guidance for how to learn each 
  topic. Will expand these checklists out into other pages over the next 
  couple of weeks.
* Added an email sign up form to determine how many people are interested in
  a full book since I've had a lot of requests in person to write one.
* Added new resources to the other web frameworks section.
* Updated the way choices to go from one page to another are generated. It's
  now done off metadata instead of duplicated HTML content.
* Huge site update to reorganize the way content is presented and navigated.
  Kinda has that "choose your own adventure" thing going for it, doesn't it?
* New logo! This one's way more Python software stack, way less boring 
  folder-thingy. Here's how the old one looked in comparison:
  <img src="/img/visuals/old-logo.png" width="100%" alt="Old Full Stack Python logo" class="shot" />

* Added a [future direction](../future-directions.html) section to explain
  current priorities for further developments on the site.
* More resources for web frameworks and configuration management sections.
* Added small JavaScript section. Updating witih basic resources.
* Updated application dependencies with new links to Python library 
  collections.
* Merged a couple of awesome pull requests that fixed typos and added 
  additional Bottle resources.

### March
* Updated logging page with new resources.
* Added new CSS page.
* New intermediate learning links on the best resources page.
* Updated task queues page with better explanations and many more curated
  resources.
* Added why is this piece necessary for databases, WSGI servers, web 
  frameworks and application dependencies.
* Updating best resources page with newsletters and a few additional beyond
  the basics resources.
* Adding 'why is this necessary' sections to servers, operating systems,
  and web servers pages.
* Extracting best Python resources from the introduction into a separate
  page.
* Cleaned up links on the first ten chapters and added new resources for
  web frameworks.
* Updated application dependencies section with new resources and initial
  content description.
* Updated the change log (how meta!) to have a cleaner layout.

### February 
* Added Bottle as a web framework next to Django and Flask.
* Added new Django resources. 
* New sitemap.xml. 
* Rewriting all sections to fix first draft typos and grammar mistakes 
  as well as add new content.
* Added task queues section due to reader feedback. 
* Rewrote intro section.
* Merged several pull requests (see closed 
  [GitHub repo pull requests](https://github.com/mattmakai/fullstackpython.com/pulls)). 
* New resources for platform-as-a-service section. 
* Added new sections specified by the community as missing. 
* Reorganized ordering of content. 
* Broke out subsections for Django and Flask. 
* Added signficant content to the WSGI section. 
* Converted from RST to Markdown (some of the downstream tools I want to 
  use work better with Markdown than RST). 
* Reorganized content into rough outline of "final" chapters.

### January 
* Added configuration management, application dependencies, and source 
  control sections. 
* Updated about section. 
* Fully responsive web design.


## 2013
### December
* Changed CDN section to static content section. 
* Transitioned diagrams from Paper app drawings to Balsamiq mockups 
  exported to PNG files. 
* Added Python database connectors to database section.

### November
* Modified color scheme. 
* Updated caching and introduction section.
* Added NoSQL data stores section.

### October 
* Created separate monitoring section.

### August
* Added more resources for web servers and other categories.

### June
* Updated styling.
* Switching around several sections.

### January
* Fleshed out web server, OS, and server sections, particularly IaaS 
  and PaaS topics.
* Added initial "hand drawn" diagram placeholders for better diagrams later.


## 2012
### December
* Initial incomplete release on fullstackpython.com, created 
  introduction, CDN, web frameworks, and database sections with stubs for 
  other areas.

