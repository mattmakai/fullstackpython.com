title: flask.ctx after_this_request Example Code
category: page
slug: flask-ctx-after-this-request-examples
sortorder: 500021011
toc: False
sidebartitle: flask.ctx after_this_request
meta: Python example code that shows how to use the after_this_request callable from the flask.ctx module of the Flask project.


[after_this_request](https://github.com/pallets/flask/blob/master/src/flask/ctx.py)
is a function in the `flask.ctx` module of the [Flask](/flask.html)
[web framework](/web-frameworks.html). The function's name is strongly
descriptive of what it does and it particularly useful for modifying
response objects, especially when you want a function other than the
view function to modify a response.

<a href="/flask-ctx-has-app-context-examples.html">has_app_context</a>
and
<a href="/flask-ctx-has-request-context-examples.html">has_request_context</a>
are a couple of other callables within the `flask.ctx` package that also have code examples.

## Example 1 from Flask-Security-Too
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

[**Flask-Security-Too / flask_security / unified_signin.py**](https://github.com/Flask-Middleware/flask-security/blob/master/flask_security/./unified_signin.py)

```python
# unified_signin.py

import time
import typing as t

from flask import current_app as app
~~from flask import after_this_request, request, session
from flask_login import current_user
from werkzeug.datastructures import MultiDict
from wtforms import BooleanField, RadioField, StringField, SubmitField, validators

from .confirmable import requires_confirmation
from .decorators import anonymous_user_required, auth_required, unauth_csrf
from .forms import Form, Required, get_form_field_label
from .proxies import _security, _datastore
from .quart_compat import get_quart_status
from .signals import us_profile_changed, us_security_token_sent
from .twofactor import (
    is_tf_setup,
    tf_login,
    tf_verify_validility_token,
)
from .utils import (
    _,
    SmsSenderFactory,
    base_render_json,
    check_and_get_token_status,
    config_value as cv,
    do_flash,
    find_user,
    get_identity_attributes,


## ... source file abbreviated to get to after_this_request examples ...



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate(self):
        if not super().validate():
            return False

        if not _security._totp_factory.verify_totp(
            token=self.passcode.data,
            totp_secret=self.totp_secret,
            user=self.user,
            window=cv("US_TOKEN_VALIDITY"),
        ):
            self.passcode.errors.append(get_message("INVALID_PASSWORD_CODE")[0])
            return False

        return True


def _send_code_helper(form):
    user = form.user
    method = form.chosen_method.data
    totp_secrets = _datastore.us_get_totp_secrets(user)
    if method == "email" and method not in totp_secrets:
~~        after_this_request(view_commit)
        totp_secrets[method] = _security._totp_factory.generate_totp_secret()
        _datastore.us_put_totp_secrets(user, totp_secrets)

    msg = user.us_send_security_token(
        method,
        totp_secret=totp_secrets[method],
        phone_number=getattr(user, "us_phone_number", None),
        send_magic_link=True,
    )
    code_sent = True
    if msg:
        code_sent = False
        form.chosen_method.errors.append(msg)
    return code_sent, msg


@anonymous_user_required
@unauth_csrf(fall_through=True)
def us_signin_send_code():
    form_class = _security.us_signin_form

    if request.is_json:
        if request.content_length:
            form = form_class(MultiDict(request.get_json()), meta=suppress_form_csrf())


## ... source file abbreviated to get to after_this_request examples ...


    form.submit.data = True

    if form.validate_on_submit():

        remember_me = form.remember.data if "remember" in form else None
        if cv("TWO_FACTOR") and form.authn_via in cv("US_MFA_REQUIRED"):
            if request.is_json and request.content_length:
                tf_validity_token = request.get_json().get(  # type: ignore
                    "tf_validity_token", None
                )
            else:
                tf_validity_token = request.cookies.get("tf_validity", default=None)

            tf_validity_token_is_valid = tf_verify_validility_token(
                tf_validity_token, form.user.fs_uniquifier
            )
            if cv("TWO_FACTOR_REQUIRED") or is_tf_setup(form.user):
                if cv("TWO_FACTOR_ALWAYS_VALIDATE") or (not tf_validity_token_is_valid):

                    return tf_login(
                        form.user,
                        remember=remember_me,
                        primary_authn_via=form.authn_via,
                    )

~~        after_this_request(view_commit)
        login_user(form.user, remember=remember_me, authn_via=[form.authn_via])

        if _security._want_json(request):
            return base_render_json(form, include_auth_token=True)

        return redirect(get_post_login_redirect())

    code_methods = _compute_code_methods()
    if _security._want_json(request):
        payload = {
            "available_methods": cv("US_ENABLED_METHODS"),
            "code_methods": code_methods,
            "identity_attributes": get_identity_attributes(),
        }
        return base_render_json(form, include_user=False, additional=payload)

    if current_user.is_authenticated:
        return redirect(get_post_login_redirect())

    form.passcode.data = None

    if form.requires_confirmation and cv("REQUIRES_CONFIRMATION_ERROR_VIEW"):
        do_flash(*get_message("CONFIRMATION_REQUIRED"))
        return redirect(get_url(cv("REQUIRES_CONFIRMATION_ERROR_VIEW")))


## ... source file abbreviated to get to after_this_request examples ...


        if _security.redirect_behavior == "spa":
            return redirect(
                get_url(
                    cv("LOGIN_ERROR_VIEW"),
                    qparams=user.get_redirect_qparams({c: m}),
                )
            )
        do_flash(m, c)
        return redirect(url_for_security("us_signin"))

    if (
        cv("TWO_FACTOR")
        and "email" in cv("US_MFA_REQUIRED")
        and (cv("TWO_FACTOR_REQUIRED") or is_tf_setup(user))
    ):
        if _security.redirect_behavior == "spa":
            return redirect(
                get_url(
                    cv("LOGIN_ERROR_VIEW"),
                    qparams=user.get_redirect_qparams({"tf_required": 1}),
                )
            )
        return tf_login(user, primary_authn_via="email")

    login_user(user, authn_via=["email"])
~~    after_this_request(view_commit)
    if _security.redirect_behavior == "spa":
        return redirect(
            get_url(cv("POST_LOGIN_VIEW"), qparams=user.get_redirect_qparams())
        )

    do_flash(*get_message("PASSWORDLESS_LOGIN_SUCCESSFUL"))
    return redirect(get_post_login_redirect())


@auth_required(
    lambda: cv("API_ENABLED_METHODS"),
    within=lambda: cv("FRESHNESS"),
    grace=lambda: cv("FRESHNESS_GRACE_PERIOD"),
)
def us_setup() -> "ResponseValue":
    form_class = _security.us_setup_form

    if request.is_json:
        if request.content_length:
            form = form_class(MultiDict(request.get_json()), meta=suppress_form_csrf())
        else:
            form = form_class(formdata=None, meta=suppress_form_csrf())
    else:
        form = form_class(meta=suppress_form_csrf())


## ... source file abbreviated to get to after_this_request examples ...


    form_class = _security.us_setup_validate_form

    if request.is_json:
        form = form_class(MultiDict(request.get_json()), meta=suppress_form_csrf())
    else:
        form = form_class(meta=suppress_form_csrf())

    expired, invalid, state = check_and_get_token_status(
        token, "us_setup", get_within_delta("US_SETUP_WITHIN")
    )
    if invalid:
        m, c = get_message("API_ERROR")
    if expired:
        m, c = get_message("US_SETUP_EXPIRED", within=cv("US_SETUP_WITHIN"))
    if invalid or expired:
        if _security._want_json(request):
            payload = json_error_response(errors=m)
            return _security._render_json(payload, 400, None, None)
        do_flash(m, c)
        return redirect(url_for_security("us_setup"))

    form.totp_secret = state["totp_secret"]
    form.user = current_user

    if form.validate_on_submit():
~~        after_this_request(view_commit)
        method = state["chosen_method"]
        phone = state["phone_number"] if method == "sms" else None
        _datastore.us_set(current_user, method, state["totp_secret"], phone)

        us_profile_changed.send(
            app._get_current_object(), user=current_user, method=method  # type: ignore
        )
        if _security._want_json(request):
            return base_render_json(
                form,
                include_user=False,
                additional=dict(
                    chosen_method=method, phone=current_user.us_phone_number
                ),
            )
        else:
            do_flash(*get_message("US_SETUP_SUCCESSFUL"))
            return redirect(
                get_url(cv("US_POST_SETUP_VIEW")) or get_url(cv("POST_LOGIN_VIEW"))
            )

    if _security._want_json(request):
        return base_render_json(form, include_user=False)
    m, c = get_message("INVALID_PASSWORD_CODE")


## ... source file continues with no further after_this_request examples...

```

