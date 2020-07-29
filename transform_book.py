import argparse
import os
from os.path import isdir, isfile


BASE_DIR = './tempcontent/pages/'
BASE_FSP = "https://www.fullstackpython.com/"

links = {
         "(/table-of-contents.html)":
         "(#table-of-contents)",

         # chapter 1
         "(/introduction.html)":
         "(#introduction)",
         "(/learning-programming.html)":
         "(#learning-programming)",
         "(/python-programming-language.html)":
         "(#python-programming-language)",
         "(/why-use-python.html)":
         "(#why-use-python)",
         "(/python-2-or-3.html)":
         "(#python-2-or-3)",
         "(/enterprise-python.html)":
         "(#enterprise-python)",
         "(/python-community.html)":
         "(#python-community)",
         "(/companies-using-python.html)":
         "(#companies-using-python)",
         "(/best-python-resources.html)":
         "(#best-python-resources)",
         "(/best-python-videos.html)":
         "(#best-python-videos)",
         "(/best-python-podcasts.html)":
         "(#best-python-podcasts)",

         # chapter 2
         "(/development-environments.html)":
         "(#development-environments)",
         "(/text-editors-ides.html)":
         "(#text-editors-ides)",
         "(/vim.html)":
         "(#vim)",
         "(/emacs.html)":
         "(#emacs)",
         "(/sublime-text.html)":
         "(#sublime-text)",
         "(/pycharm.html)":
         "(#pycharm)",
         "(/jupyter-notebook.html)":
         "(#jupyter-notebook)",
         "(/shells.html)":
         "(#shells)",
         "(/bourne-again-shell-bash.html)":
         "(#bourne-again-shell-bash)",
         "(/zsh-shell.html)":
         "(#zsh-shell)",
         "(/powershell.html)":
         "(#powershell)",
         "(/terminal-multiplexers.html)":
         "(#terminal-multiplexers)",
         "(/tmux.html)":
         "(#tmux)",
         "(/screen.html)":
         "(#screen)",
         "(/environment-configuration.html)":
         "(#environment-configuration)",
         "(/application-dependencies.html)":
         "(#application-dependencies)",
         "(/virtual-environments-virtualenvs-venvs.html)":
         "(#virtual-environments-virtualenvs-venvs)",
         "(/localhost-tunnels.html)":
         "(#localhost-tunnels)",
         "(/source-control.html)":
         "(#source-control)",
         "(/git.html)":
         "(#git)",
         "(/mercurial.html)":
         "(#mercurial)",

         # chapter 3
         "(/data.html)":
         "(#data)",
         "(/databases.html)":
         "(#relational-databases)",
         "(/postgresql.html)":
         "(#postgresql)",
         "(/mysql.html)":
         "(#mysql)",
         "(/sqlite.html)":
         "(#sqlite)",
         "(/object-relational-mappers-orms.html)":
         "(#object-relational-mappers-orms)",
         "(/sqlalchemy.html)":
         "(#sqlalchemy)",
         "(/peewee.html)":
         "(#peewee)",
         "(/django-orm.html)":
         "(#django-orm)",
         "(/pony-orm.html)":
         "(#pony-orm)",
         "(/no-sql-datastore.html)":
         "(#no-sql-datastore)",
         "(/redis.html)":
         "(#redis)",
         "(/mongodb.html)":
         "(#mongodb)",
         "(/apache-cassandra.html)":
         "(#apache-cassandra)",
         "(/neo4j.html)":
         "(#neo4j)",
         "(/data-analysis.html)":
         "(#data-analysis)",
         "(/pandas.html)":
         "(#pandas)",
         "(/scipy-numpy.html)":
         "(#scipy-numpy)",
         "(/data-visualization.html)":
         "(#data-visualization)",
         "(/bokeh.html)":
         "(#bokeh)",
         "(/d3-js.html)":
         "(#d3-js)",
         "(/matplotlib.html)":
         "(#matplotlib)",
         "(/markup-languages.html)":
         "(#markup-languages)",
         "(/restructuredtext.html)":
         "(#restructuredtext)",
         "(/markdown.html)":
         "(#markdown)",

         # chapter 4
         "(/web-development.html)":
         "(#web-development)",
         "(/web-frameworks.html)":
         "(#web-frameworks)",
         "(/django.html)":
         "(#django)",
         "(/flask.html)":
         "(#flask)",
         "(/bottle.html)":
         "(#bottle)",
         "(/pyramid.html)":
         "(#pyramid)",
         "(/turbogears.html)":
         "(#turbogears)",
         "(/falcon.html)":
         "(#falcon)",
         "(/morepath.html)":
         "(#morepath)",
         "(/sanic.html)":
         "(#sanic)",
         "(/other-web-frameworks.html)":
         "(#other-web-frameworks)",
         "(/template-engines.html)":
         "(#template-engines)",
         "(/jinja2.html)":
         "(#jinja2)",
         "(/mako.html)":
         "(#mako)",
         "(/django-templates.html)":
         "(#django-templates)",
         "(/web-design.html)":
         "(#web-design)",
         "(/hypertext-markup-language-html.html)":
         "(#hypertext-markup-language-html)",
         "(/cascading-style-sheets.html)":
         "(#cascading-style-sheets)",
         "(/responsive-design.html)":
         "(#responsive-design)",
         "(/minification.html)":
         "(#minification)",
         "(/css-frameworks.html)":
         "(#css-frameworks)",
         "(/bootstrap-css.html)":
         "(#bootstrap-css)",
         "(/foundation-css.html)":
         "(#foundation-css)",
         "(/javascript.html)":
         "(#javascript)",
         "(/react.html)":
         "(#react)",
         "(/vuejs.html)":
         "(#vuejs)",
         "(/angular.html)":
         "(#angular)",
         "(/task-queues.html)":
         "(#task-queues)",
         "(/celery.html)":
         "(#celery)",
         "(/redis-queue-rq.html)":
         "(#redis-queue-rq)",
         "(/dramatiq.html)":
         "(#dramatiq)",
         "(/static-site-generator.html)":
         "(#static-site-generator)",
         "(/pelican.html)":
         "(#pelican)",
         "(/lektor.html)":
         "(#lektor)",
         "(/mkdocs.html)":
         "(#mkdocs)",
         "(/testing.html)":
         "(#testing)",
         "(/unit-testing.html)":
         "(#unit-testing)",
         "(/integration-testing.html)":
         "(#integration-testing)",
         "(/debugging.html)":
         "(#debugging)",
         "(/code-metrics.html)":
         "(#code-metrics)",
         "(/networking.html)":
         "(#networking)",
         "(/https.html)":
         "(#https)",
         "(/websockets.html)":
         "(#websockets)",
         "(/webrtc.html)":
         "(#webrtc)",
         "(/application-programming-interfaces.html)":
         "(#application-programming-interfaces)",
         "(/microservices.html)":
         "(#microservices)",
         "(/webhooks.html)":
         "(#webhooks)",
         "(/bots.html)":
         "(#bots)",
         "(/api-creation.html)":
         "(#api-creation)",
         "(/api-frameworks.html)":
         "(#api-frameworks)",
         "(/django-rest-framework-drf.html)":
         "(#django-rest-framework-drf)",
         "(/api-integration.html)":
         "(#api-integration)",
         "(/twilio.html)":
         "(#twilio)",
         "(/stripe.html)":
         "(#stripe)",
         "(/slack.html)":
         "(#slack)",
         "(/okta.html)":
         "(#okta)",
         "(/web-application-security.html)":
         "(#web-application-security)",
         "(/sql-injection.html)":
         "(#sql-injection)",
         "(/cross-site-request-forgery-csrf.html)":
         "(#cross-site-request-forgery-csrf)",

         # chapter 5
         "(/deployment.html)":
         "(#deployment)",
         "(/hosting.html)":
         "(#hosting)",
         "(/servers.html)":
         "(#servers)",
         "(/static-content.html)":
         "(#static-content)",
         "(/content-delivery-networks-cdns.html)":
         "(#content-delivery-networks-cdns)",
         "(/virtual-private-servers-vps.html)":
         "(#virtual-private-servers-vps)",
         "(/linode.html)":
         "(#linode)",
         "(/digitalocean.html)":
         "(#digitalocean)",
         "(/lightsail.html)":
         "(#lightsail)",
         "(/platform-as-a-service.html)":
         "(#platform-as-a-service)",
         "(/heroku.html)":
         "(#heroku)",
         "(/pythonanywhere.html)":
         "(#pythonanywhere)",
         "(/aws-codestar.html)":
         "(#aws-codestar)",
         "(/operating-systems.html)":
         "(#operating-systems)",
         "(/ubuntu.html)":
         "(#ubuntu)",
         "(/macos.html)":
         "(#macos)",
         "(/microsoft-windows.html)":
         "(#microsoft-windows)",
         "(/freebsd.html)":
         "(#freebsd)",
         "(/web-servers.html)":
         "(#web-servers)",
         "(/apache-http-server.html)":
         "(#apache-http-server)",
         "(/nginx.html)":
         "(#nginx)",
         "(/caddy.html)":
         "(#caddy)",
         "(/wsgi-servers.html)":
         "(#wsgi-servers)",
         "(/green-unicorn-gunicorn.html)":
         "(#green-unicorn-gunicorn)",
         "(/uwsgi.html)":
         "(#uwsgi)",
         "(/mod-wsgi.html)":
         "(#mod-wsgi)",
         "(/continuous-integration.html)":
         "(#continuous-integration)",
         "(/jenkins.html)":
         "(#jenkins)",
         "(/gocd.html)":
         "(#gocd)",
         "(/configuration-management.html)":
         "(#configuration-management)",
         "(/ansible.html)":
         "(#ansible)",
         "(/salt.html)":
         "(#salt)",
         "(/containers.html)":
         "(#containers)",
         "(/docker.html)":
         "(#docker)",
         "(/kubernetes.html)":
         "(#kubernetes)",
         "(/serverless.html)":
         "(#serverless)",
         "(/aws-lambda.html)":
         "(#aws-lambda)",
         "(/azure-functions.html)":
         "(#azure-functions)",
         "(/google-cloud-functions.html)":
         "(#google-cloud-functions)",

         # chapter 6
         "(/devops.html)":
         "(#devops)",
         "(/monitoring.html)":
         "(#monitoring)",
         "(/prometheus.html)":
         "(#prometheus)",
         "(/rollbar.html)":
         "(#rollbar)",
         "(/sentry.html)":
         "(#sentry)",
         "(/scout.html)":
         "(#scout)",
         "(/web-app-performance.html)":
         "(#web-app-performance)",
         "(/logging.html)":
         "(#logging)",
         "(/caching.html)":
         "(#caching)",
         "(/web-analytics.html)":
         "(#web-analytics)",

         # meta (chapter 7)
         "(/what-full-stack-means.html)":
         "(#what-full-stack-means)",
         "(/about-author.html)":
         "(#about-author)",
         "(/change-log.html)":
         "(" + BASE_FSP + "change-log.html)",
         "(/future-directions.html)":
         "(" + BASE_FSP + "future-directions.html)",

         # code examples
         "(/django-code-examples.html)":
         "(" + BASE_FSP + "django-code-examples.html)",
         "(/sqlalchemy-extensions-plug-ins-related-libraries.html)":
         "(" + BASE_FSP + "sqlalchemy-extensions-plug-ins-related-libraries.html)",

         "(/email.html)":
         "(" + BASE_FSP + "email.html)",
         "<a href=\"/full-stack-python-map.pdf\" style=\"border:none\"><img src=\"/img/visuals/full-stack-python-map.png\" width=\"100%\" alt=\"Full Stack Python deployments map.\" class=\"shot\"></a>":
         "<img src=\"img/visuals/full-stack-python-map.png\" alt=\"Full Stack Python deployments map.\">",

         "(/blog.html)":
         "(" + BASE_FSP + "blog.html",
         "(/blog/":
         "(" + BASE_FSP + "blog/",
         }


def transform(output_format='pdf'):
    dirs = os.listdir(BASE_DIR)
    print(os.listdir(BASE_DIR))
    for d in dirs:
        if isdir(BASE_DIR + d):
            # modify all markdown files in directory
            files = os.listdir(BASE_DIR + d)
            for f in files:
                if not isdir(BASE_DIR + d + '/' + f):
                    with open(BASE_DIR + d + '/' + f, 'r',
                              encoding="utf-8") as read_f:
                        all_lines = read_f.readlines()

                    with open(BASE_DIR + d + '/' + f, 'w') as write_f:
                        for l in all_lines:
                            for k, v in links.items():
                                l = l.replace(k, v)
                            if "<div class=\"well see-also\">" in l:
                                write_f.write("")
                            else:
                                write_f.write(l)
                        print('prepared file ' + str(d) + '/' + str(f))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("o")
    args = parser.parse_args()

    if args.o == 'pdf':
        transform('pdf')
    elif args.o == 'epub':
        transform('epub')
