import argparse


"""Automates posting to social channels and tutorials page on
fullstackpython.com.

Arguments:

-c, --channel   which channel to post to, options are "all", "twitter",
                "facebook", "tutorials"

-s, --subject   custom subject line for the posting, otherwise <h1>
                element's content will be used

-t, --tags      tags for tutorials page


Examples:

1. Post URL to all channels with the default title found within the page's
   <h1> and tagged with any keywords that match between the page content
   and the table of contents map.

	python post.py https://www.fullstackpython.com/django.html


2. Post URL to all channels with the default title found within the page's
   <h1> and tagged "git" and "source control".

	python post.py https://www.fullstackpython.com/git.html "git, source control"


3. Post URL to all channels with a custom description of "Newest Mapbox
   tutorial is live!" and tagged "django", "web development" and
   "web frameworks".

    python post.py https://www.fullstackpython.com/blog/maps-django-web-applications-projects-mapbox.html "django, web development, web frameworks" -d "Newest Mapbox tutorial is live!"


4. Post URL only to Twitter with a custom description of "An overview of relational databases for Python."

	python post.py https://www.fullstackpython.com/databases.html "postgresql, mysql" -d "An overview of relational databases for Python." -c twitter
"""

def post_to_buffer():
    """See: https://buffer.com/developers/api/updates#updatesshare
    """
    pass


parser = argparse.ArgumentParser(description='Post a tutorial.')
parser.add_argument('url', metavar='1', type=str, nargs='?',
                    help='URL for the tutorial to post')
parser.add_argument("-c", "--channel", help="channel to post tutorial to")
parser.add_argument("-s", "--subject", help="subject line to use with the post")
parser.add_argument("-t", "--tags", help="comma-delimited list of fsp topics")


args = parser.parse_args()
print(args.url)
print(args.channel)
print(args.subject)
print(args.tags)


