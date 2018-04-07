import argparse
import os
from os.path import isdir, isfile


BASE_DIR = './tempcontent/'
BASE_FSP = "https://www.fullstackpython.com/"

links = {"/introduction.html":
         "../01-introduction/02-learning-programming.markdown",
         "/learning-programming.html":
         "../01-introduction/02-learning-programming.markdown",
         "/why-use-python.html":
         "../01-introduction/03-why-use-python.markdown",
         "/python-2-or-3.html":
         "../01-introduction/04-python-2-or-3.markdown",
         "/enterprise-python.html":
         "../01-introduction/05-enterprise-python.markdown",
         "/best-python-resources.html":
         "../01-introduction/11-best-python-resources.markdown",
         "/best-python-videos.html":
         "../01-introduction/12-best-python-videos.markdown",

         "/development-environments.html":
         "../02-development-environments/01-development-environments.markdown",
         "/vim.html":
         "../02-development-environments/03-vim.markdown",
         "/emacs.html":
         "../02-development-environments/04-emacs.markdown",

         "/python-programming-language.html":
         "../03-programming-language/01-programming-language.markdown",
         "/generators.html":
         "../03-programming-language/08-generators.markdown",
         "/comprehensions.html":
         "../03-programming-language/09-comprehensions.markdown",

         "/web-development.html":
         "../04-web-development/01-web-development.markdown",
         "/web-frameworks.html":
         "../04-web-development/02-web-frameworks.markdown",
         "/django.html":
         "../04-web-development/03-django.markdown",
         "/flask.html":
         "../04-web-development/04-flask.markdown",
         "/bottle.html":
         "../04-web-development/05-bottle.markdown",
         "/pyramid.html":
         "../04-web-development/06-pyramid.markdown",
         "/morepath.html":
         "../04-web-development/07-morepath.markdown",
         "/other-web-frameworks.html":
         "../04-web-development/09-other-web-frameworks.markdown",
         "/web-design.html":
         "../04-web-development/10-web-design.markdown",
         "/cascading-style-sheets.html":
         "../04-web-development/11-css.markdown",
         "/javascript.html":
         "../04-web-development/12-javascript.markdown",
         "/websockets.html":
         "../04-web-development/13-websockets.markdown",
         "/template-engines.html":
         "../04-web-development/14-template-engines.markdown",
         "/web-application-security.html":
         "../04-web-development/15-web-app-security.markdown",
         "/static-site-generator.html":
         "../04-web-development/16-static-site-generator.markdown",
         "/jinja2.html":
         "../04-web-development/17-jinja2.markdown",

         "/data.html":
         "../05-data/01-data.markdown",
         "/databases.html":
         "../05-data/02-databases.markdown",
         "/no-sql-datastore.html":
         "../05-data/03-nosql.markdown",
         "/object-relational-mappers-orms.html":
         "../05-data/04-object-relational-mappers.markdown",
         "/postgresql.html":
         "../05-data/05-postgresql.markdown",
         "/mysql.html":
         "../05-data/06-mysql.markdown",
         "/sqlite.html":
         "../05-data/07-sqlite.markdown",

         "/application-programming-interfaces.html":
         "../06-web-apis/01-application-programming-interfaces.markdown",
         "/api-integration.html":
         "../06-web-apis/02-api-integration.markdown",
         "/api-creation.html":
         "../06-web-apis/03-api-creation.markdown",

         "/deployment.html":
         "../07-web-app-deployment/01-deployment.markdown",
         "/servers.html":
         "../07-web-app-deployment/02-servers.markdown",
         "/platform-as-a-service.html":
         "../07-web-app-deployment/04-platform-as-a-service.markdown",
         "/operating-systems.html":
         "../07-web-app-deployment/05-operating-systems.markdown",
         "/web-servers.html":
         "../07-web-app-deployment/06-web-servers.markdown",
         "/wsgi-servers.html":
         "../07-web-app-deployment/07-wsgi-servers.markdown",
         "/source-control.html":
         "../07-web-app-deployment/08-source-control.markdown",
         "/application-dependencies.html":
         "../07-web-app-deployment/09-app-dependencies.markdown",
         "/static-content.html":
         "../07-web-app-deployment/10-static-content.markdown",
         "/task-queues.html":
         "../07-web-app-deployment/11-task-queues.markdown",
         "/configuration-management.html":
         "../07-web-app-deployment/12-configuration-management.markdown",
         "/continuous-integration.html":
         "../07-web-app-deployment/13-continuous-integration.markdown",
         "/logging.html":
         "../07-web-app-deployment/14-logging.markdown",
         "/monitoring.html":
         "../07-web-app-deployment/15-monitoring.markdown",
         "/web-analytics.html":
         "../07-web-app-deployment/16-web-analytics.markdown",
         "/docker.html":
         "../07-web-app-deployment/17-docker.markdown",
         "/caching.html":
         "../07-web-app-deployment/18-caching.markdown",
         "/microservices.html":
         "../07-web-app-deployment/19-microservices.markdown",
         "/devops.html":
         "../07-web-app-deployment/20-devops.markdown",
         "/nginx.html":
         "../07-web-app-deployment/21-nginx.markdown",
         "/apache-http-server.html":
         "../07-web-app-deployment/22-apache-http-server.markdown",
         "/caddy.html":
         "../07-web-app-deployment/23-caddy.markdown",
         "/green-unicorn-gunicorn.html":
         "../07-web-app-deployment/24-gunicorn.markdown",


         "/testing.html":
         "../08-testing/01-testing.markdown",
         "/unit-testing.html":
         "../08-testing/02-unit-testing.markdown",
         "/integration-testing.html":
         "../08-testing/03-integration-testing.markdown",
         "/code-metrics.html":
         "../08-testing/05-code-metrics.markdown",
         "/debugging.html":
         "../08-testing/08-debugging.markdown",

         "/what-full-stack-means.html":
         "../13-meta/01-what-full-stack-means.markdown",
         "/change-log.html":
         "../13-meta/02-change-log.markdown",
         "/future-directions.html":
         "../13-meta/03-future-directions.markdown",
         "/about-author.html":
         "../13-meta/04-about-author.markdown",

         "/email.html":
         BASE_FSP + "email.html",
         "<a href=\"/full-stack-python-map.pdf\" target=\"_blank\" style=\"border: none;\"><img src=\"/img/full-stack-python-map.png\" width=\"100%\" alt=\"Full Stack Python site map.\" class=\"technical-diagram\" /></a>":
         "<img src=\"/img/full-stack-python-map.png\" alt=\"Full Stack Python deployment map.\" />",

         "/blog.html":
         BASE_FSP + "blog.html",
         "/blog/python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus.html":
         BASE_FSP + "blog/python-3-bottle-gunicorn-ubuntu-1604-xenial-xerus.html",
         "/blog/install-redis-use-python-3-ubuntu-1604.html":
         BASE_FSP + "blog/install-redis-use-python-3-ubuntu-1604.html",
         "/blog/postgresql-python-3-psycopg2-ubuntu-1604.html":
         BASE_FSP + "blog/postgresql-python-3-psycopg2-ubuntu-1604.html",
         "/blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html":
         BASE_FSP + "blog/python-3-flask-green-unicorn-ubuntu-1604-xenial-xerus.html",
         "/blog/python-3-django-gunicorn-ubuntu-1604-xenial-xerus.html":
         BASE_FSP + "blog/python-3-django-gunicorn-ubuntu-1604-xenial-xerus.html",
         }


def transform(output_format='pdf'):
    dirs = os.listdir(BASE_DIR)
    print os.listdir(BASE_DIR)
    for d in dirs:
        if isdir(BASE_DIR + d):
            # modify all markdown files in directory
            files = os.listdir(BASE_DIR + d)
            for f in files:
                with open(BASE_DIR + d + '/' + f, 'r') as read_f:
                    all_lines = read_f.readlines()

                with open(BASE_DIR + d + '/' + f, 'w') as write_f:
                    for l in all_lines[8:]:
                        for k, v in links.iteritems():
                            l = l.replace(k, v)
                        if "<div class=\"well see-also\">" in l:
                            write_f.write("")
                        else:
                            write_f.write(l)
                    print 'prepared file ' + str(d) + '/' + str(f)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("o")
    args = parser.parse_args()

    if args.o == 'pdf':
        transform('pdf')
    elif args.o == 'epub':
        transform('epub')
