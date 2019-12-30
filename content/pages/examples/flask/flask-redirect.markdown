title: flask redirect Example Python Code
category: page
slug: flask-redirect-examples
sortorder: 500021005
toc: False
sidebartitle: flask redirect
meta: Python code examples for the redirect function from the Flask project used for building web applications.


The [Flask](/flask.html)
[redirect](https://flask.palletsprojects.com/en/1.1.x/api/#flask.redirect)
([source code](https://github.com/pallets/werkzeug/blob/master/src/werkzeug/utils.py))
function appropriately sends a redirect status code, one of 
301, 302, 303, 305, 307, or 308. 


## Example 1 from FlaskBB
[FlaskBB](https://github.com/flaskbb/flaskbb)
([project website](https://flaskbb.org/)) is a [Flask](/flask.html)-based
forum web application. The web app allows users to chat in an open
message board or send private messages in plain text or 
[Markdown](/markdown.html). FlaskBB is provided as open source 
[under this license](https://github.com/flaskbb/flaskbb/blob/master/LICENSE).

This example can be slightly confusing because it wraps `redirect` and calls
`self.redirect` to invoke the wrapper function.

[**flaskbb / flaskbb / user / views.py**](https://github.com/flaskbb/flaskbb/blob/master/flaskbb/user/views.py)

```python
# -*- coding: utf-8 -*-
"""
    flaskbb.user.views
    ------------------
    The user view handles the user profile
    and the user settings from a signed in user.
    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
import logging

import attr
~~from flask import Blueprint, flash, redirect, request, url_for
from flask.views import MethodView
from flask_babelplus import gettext as _
from flask_login import current_user, login_required
from pluggy import HookimplMarker


## ... code abbreviated here to get to the appropriate examples ...


@attr.s(frozen=True, cmp=False, hash=False, repr=True)
class UserSettings(MethodView):
    form = attr.ib(factory=settings_form_factory)
    settings_update_handler = attr.ib(factory=settings_update_handler)

    decorators = [login_required]

    def get(self):
        return self.render()

    def post(self):
        if self.form.validate_on_submit():
            try:
                self.settings_update_handler.apply_changeset(
                    current_user, self.form.as_change()
                )
            except StopValidation as e:
                self.form.populate_errors(e.reasons)
                return self.render()
            except PersistenceError:
                logger.exception("Error while updating user settings")
                flash(_("Error while updating user settings"), "danger")
                return self.redirect()

            flash(_("Settings updated."), "success")
            return self.redirect()
        return self.render()

    def render(self):
        return render_template("user/general_settings.html", form=self.form)

    def redirect(self):
~~        return redirect(url_for("user.settings"))


@attr.s(frozen=True, hash=False, cmp=False, repr=True)
class ChangePassword(MethodView):
    form = attr.ib(factory=change_password_form_factory)
    password_update_handler = attr.ib(factory=password_update_handler)
    decorators = [login_required]

    def get(self):
        return self.render()

    def post(self):
        if self.form.validate_on_submit():
            try:
                self.password_update_handler.apply_changeset(
                    current_user, self.form.as_change()
                )
            except StopValidation as e:
                self.form.populate_errors(e.reasons)
                return self.render()
            except PersistenceError:
                logger.exception("Error while changing password")
                flash(_("Error while changing password"), "danger")
                return self.redirect()

            flash(_("Password updated."), "success")
            return self.redirect()
        return self.render()

    def render(self):
        return render_template("user/change_password.html", form=self.form)

    def redirect(self):
~~        return redirect(url_for("user.change_password"))


@attr.s(frozen=True, cmp=False, hash=False, repr=True)
class ChangeEmail(MethodView):
    form = attr.ib(factory=change_email_form_factory)
    update_email_handler = attr.ib(factory=email_update_handler)
    decorators = [login_required]

    def get(self):
        return self.render()

    def post(self):
        if self.form.validate_on_submit():
            try:
                self.update_email_handler.apply_changeset(
                    current_user, self.form.as_change()
                )
            except StopValidation as e:
                self.form.populate_errors(e.reasons)
                return self.render()
            except PersistenceError:
                logger.exception("Error while updating email")
                flash(_("Error while updating email"), "danger")
                return self.redirect()

            flash(_("Email address updated."), "success")
            return self.redirect()
        return self.render()

    def render(self):
        return render_template("user/change_email.html", form=self.form)

    def redirect(self):
~~        return redirect(url_for("user.change_email"))


## ... code continues from here with similar redirect examples ...
```
