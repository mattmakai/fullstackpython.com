============
Contributing
============

Contributions are welcome and greatly appreciated!


Fix Typos, Grammar Errors, etc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create pull requests at
https://github.com/makaimc/fullstackpython.com/pulls.


Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at
https://github.com/makaimc/fullstackpython.com/issues.


Get Started!
------------

If you're not familiar with `Pelican <http://docs.getpelican.com/>`_, check out the blog post on
`Getting Started with Pelican and GitHub Pages <http://www.mattmakai.com/introduction-to-pelican.html>`_.

**Ready to contribute? Here's how to set up Full Stack Python for local development.**

1. Fork the `fullstackpython.com <https://github.com/makaimc/fullstackpython.com>`_ repo on GitHub.

2. Clone your fork locally::

    $ git clone git@github.com:your_name_here/fullstackpython.com.git fsp

3. Install your local copy into a virtualenv and set up your fork for local development::

    $ virtualenv --no-site-packages venvs/fsp
    $ source venvs/fsp/bin/activate
    $ cd fsp

4. Install the requirements::

    $ pip install -r requirements.txt

Note: make changes to the source/content/pages/\*.rst files then execute a
*make run* command from the source/ directory.

5. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin gh-pages

6. Submit a pull request through the GitHub website.

**Keep your fork in Sync**

1. To keep your fork in sync with the original repo, add an `upstream remote <https://help.github.com/articles/configuring-a-remote-for-a-fork/>`_::

    $ git remote add upstream git@github.com:makaimc/fullstackpython.com.git

2. Sync your repo with the original repo::

    $ git fetch upstream
    $ git merge upstream/gh-pages
