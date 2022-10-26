"""
initialise login manager
configure app for login
provide a user_loader callback, that stores user_id in the session
user class which implements the required properties and methods, use UserMixin class
once a user has authenticated, log them in with the login_user function
use logout_user function to log them out
use login_required decorator for pages that require a user to be logged in
"""

"""
in addition to flask-login, we can use wtforms and a flask loginform to authenticate client-side data
wtforms provides validate_on_submit()
You MUST validate the value of the next parameter. If you do not, your application will be vulnerable to open redirects.
You can then access the logged-in user with the current_user proxy, which is available in every template
"""

"""
This callback is used to reload the user object from the user ID stored in the session. It should take the str ID of a user, and return the corresponding user object.
@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
"""

"""
callback for login failures, very optional as app redirects back to login view
@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401
"""

"""
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)
"""

# You can then access the logged-in user with the current_user proxy, which is available in every template

# Views that require your users to be logged in can be decorated with the login_required decorator
# the logout_user function logs the user out
# The name of the log in view can be set as LoginManager.login_view; login_manager.login_view = "users.login"