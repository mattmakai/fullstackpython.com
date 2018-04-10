import argparse
import os
from os.path import isdir, isfile


BASE_DIR = './tempcontent/pages/'
BASE_FSP = "https://www.fullstackpython.com/"

links = {# chapter 1
         "(/introduction.html)":
         "(#introduction)",
         "(/learning-programming.html)":
         "(#learning-programming)",
         "(/python-programming-language)":
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
         "(#text-editors-and-ides)",
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
         "(#zsh)",
         "(/powershell.html)":
         "(#powershell)",
         "(/terminal-multiplexers.html)":
         "(#terminal-multiplexers)",
         "(/tmux.html)":
         "(#tmux)",
         "(/screen.html)":
         "(#screen)",
         "(/pymux.html)":
         "(#pymux)",
         "(/environment-configuration.html)":
         "(#environment-configuration)",
         "(/application-dependencies.html)":
         "(#application-dependencies)",
         "(/virtual-environments-virtualenvs-venvs.html)":
         "(#virtual-environments-virtualenvs)",
         "(/environment-variables.html)":
         "(#environment-variables)",
         "(/localhost-tunnels.html)":
         "(#localhost-tunnels)",
         "(/source-control.html)":
         "(#source-control)",
         "(/git.html)":
         "(#git)",
         "(/mercurial.html)":
         "(#mercurial)",
         "(/apache-subversion.html)":
         "(#apache-subversion)",
         "(/hosted-source-control-services.html)":
         "(#hosted-source-control-services)",
         "(/github.html)":
         "(#github)",
         "(/bitbucket.html)":
         "(#bitbucket)",
         "(/gitlab.html)":
         "(#gitlab)",

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
         "(#django-object-relational-mapper)",
         "(/sqlobject.html)":
         "(#sqlobject)",
         "(/pony-orm.html)":
         "(#pony-orm)",
         "(/no-sql-datastore.html)":
         "(#nosql-data-stores)",
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
         "(/numpy.html)":
         "(#numpy)",
         "(/scipy.html)":
         "(#scipy)",
         #("/.html)":
         #("#)",
         "(/bokeh.html)":
         "(#bokeh)",
         "(/d3-js.html)":
         "(#data-driven-documents-d3js)",
         "(/matplotlib.html)":
         "(#matplotlib)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
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
         "(#cascading-style-sheets-css)",
         "(/responsive-design.html)":
         "(#responsive-design)",
         "(/minification.html)":
         "(#minification)",
         "(/css-frameworks.html)":
         "(#css-frameworks)",
         "(/bootstrap-css.html)":
         "(#bootstrap)",
         "(/foundation-css.html)":
         "(#foundation)",
         #"(/.html)":
         #"(#)",
         #"(/.html)":
         #"(#)",
         "(/javascript.html)":
         "(#javascript)",
         #"(/.html)":
         #"(#)",
         #"(/.html)":
         #"(#)",
         #"(/.html)":
         #"(#)",
         #"(/.html)":
         #"(#)",
         "(/task-queues.html)":
         "(#task-queues)",
         "(/celery.html)":
         "(#celery)",
         "(/redis-queue-rq.html)":
         "(#redis-queue-rq)",
         "(/dramatiq.html)":
         "(#dramatiq)",
         #("/.html)":
         #("#)",
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
         #("/.html)":
         #("#)",
         "(/code-metrics.html)":
         "(#code-metrics)",
         "(/debugging.html)":
         "(#debugging)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         "(/websockets.html)":
         "(#websockets)",
         #("/.html)":
         #("#)",
         "(/uvloop.html)":
         "(#uvloop)",
         "(/application-programming-interfaces.html)":
         "(#application-programming-interfaces)",
         "(/microservices.html)":
         "(#microservices)",
         #("/.html)":
         #("#)",
         "(/bots.html)":
         "(#bots)",
         "(/api-creation.html)":
         "(#api-creation)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         "(/api-integration.html)":
         "(#api-integration)",
         "(/twilio.html)":
         "(#twilio)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         "(/web-application-security.html)":
         "(#web-application-security)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",

         # chapter 5
         "(/deployment.html)":
         "(#deployment)",
         #("/.html)":
         #("#)",
         "(/servers.html)":
         "(#servers)",
         "(/static-content.html)":
         "(#static-content)",
         #("/.html)":
         #("#)",
         "(/virtual-private-servers-vps.html)":
         "(#virtual-private-servers-vps)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         "(/platform-as-a-service.html)":
         "(#platform-as-a-service)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         "(/operating-systems.html)":
         "(#operating-systems)",
         "(/ubuntu.html)":
         "(#ubuntu)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         "(/web-servers.html)":
         "(#web-servers)",
         "(/apache-http-server.html)":
         "(#apache-http-server)",
         "(/nginx.html)":
         "(#nginx)",
         "(/caddy.html)":
         "(#caddy)",
         #("/.html)":
         #("#)",
         "(/wsgi-servers.html)":
         "(#wsgi-servers)",
         "(/green-unicorn-gunicorn.html)":
         "(#green-unicorn-gunicorn)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         "(/continuous-integration.html)":
         "(#continuous-integration)",
         "(/jenkins.html)":
         "(#jenkins)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         "(/configuration-management.html)":
         "(#configuration-management)",
         "(/ansible.html)":
         "(#ansible)",
         #("/.html)":
         #("#)",
         #("/.html)":
         #("#)",
         "(/docker.html)":
         "(#docker)",
         #("/.html)":
         #("#)",
         "(/serverless.html)":
         "(#serverless)",
         "(/aws-lambda.html)":
         "(#aws-lambda)",
         #("/.html)":
         #("#)",
         "(/google-cloud-functions.html)":
         "(#google-cloud-functions)",

         # chapter 6
         "(/devops.html)":
         "(#devops)",
         "(/monitoring.html)":
         "(#monitoring)",
         "(/rollbar.html)":
         "(#rollbar)",
         "(/caching.html)":
         "(#caching)",
         "(/logging.html)":
         "(#logging)",
         "(/web-analytics.html)":
         "(#web-analytics)",

         # meta (chapter 7)
         "(/what-full-stack-means.html)":
         "(#what-full-stack-means)",
         "(/about-author.html)":
         "(#about-the-author)",
         "(/change-log.html)":
         "(" + BASE_FSP + "change-log.html)",
         "(/future-directions.html)":
         "(" + BASE_FSP + "future-directions.html)",

         "(/email.html)":
         "(" + BASE_FSP + "email.html)",
         "<a href=\"/full-stack-python-map.pdf\" target=\"_blank\" style=\"border: none;\"><img src=\"/img/full-stack-python-map.png\" width=\"100%\" alt=\"Full Stack Python site map.\" class=\"technical-diagram\" /></a>":
         "<img src=\"/img/full-stack-python-map.png\" alt=\"Full Stack Python deployment map.\" />",

         "(/blog.html)":
         "(" + BASE_FSP + "blog.html",
         "(/blog/python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus.html)":
         "(" + BASE_FSP + "blog/python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus.html",
         "(/blog/install-redis-use-python-3-ubuntu-1604.html)":
         "(" + BASE_FSP + "blog/install-redis-use-python-3-ubuntu-1604.html",
         "(/blog/postgresql-python-3-psycopg2-ubuntu-1604.html)":
         "(" + BASE_FSP + "blog/postgresql-python-3-psycopg2-ubuntu-1604.html",
         "(/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html)":
         "(" + BASE_FSP + "blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html",
         "(/blog/python-3-django-gunicorn-ubuntu-1604-xenial-xerus.html)":
         "(" + BASE_FSP + "blog/python-3-django-gunicorn-ubuntu-1604-xenial-xerus.html",
         }


def transform(output_format='pdf'):
    dirs = os.listdir(BASE_DIR)
    print(os.listdir(BASE_DIR))
    for d in dirs:
        if isdir(BASE_DIR + d):
            # modify all markdown files in directory
            files = os.listdir(BASE_DIR + d)
            for f in files:
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
