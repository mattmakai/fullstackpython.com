============
Contributing
============

Contributions are welcome and greatly appreciated!


Fix Typos, Grammar Errors, etc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create pull requests at
https://github.com/makaimc/fullstackpython.github.com/pulls.


Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/makaimc/fullstackpython.github.com/issues.


Get Started!
------------

If you're not familiar with `Pelican <http://docs.getpelican.com/>`_, check out the blog post on
`Getting Started with Pelican and GitHub Pages <http://www.mattmakai.com/introduction-to-pelican.html>`_.

Ready to contribute? Here's how to set up Full Stack Python for local
development.

1. Fork the `fullstackpython.github.com <https://github.com/makaimc/fullstackpython.github.com>`_ repo on GitHub.

2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/fullstackpython.github.com.git fsp

3. Install your local copy into a virtualenv and set up your fork for local development::

    $ virtualenv --no-site-packages venvs/fsp
    $ source venvs/fsp/bin/activate
    $ cd fsp

4. Install the requirements by running:

    $ pip install -r source/requirements.txt

From the root directory.

5. Make changes to the source/content/pages/\*.rst files then run:

    $ python source/build.py

From the root directory. This will rebuild the static HTML files with your
changes. Check them out in a browser to be sure you're happy with them!

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin gh-pages

7. Submit a pull request through the GitHub website.

