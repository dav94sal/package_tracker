from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user
from ..forms.login_form import LoginForm
from ..forms.signup_form import SignupForm
from ..models import User, db


bp = Blueprint("session", __name__, url_prefix="/session")


@bp.route("/", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("routes.index"))
    form = LoginForm()

    if form.validate_on_submit():
        username = form.data["username"]
        user = User.query.filter(User.username == username).first()
        if not user or not user.check_password(form.data["password"]):
            return redirect(url_for(".login"))
        login_user(user)
        return redirect(url_for("routes.index"))

    return render_template("login.html", form=form)


@bp.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return redirect(url_for(".login"))


@bp.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()

    if form.validate_on_submit():
        data = form.data

        user = User(first_name=data["first_name"],
                    last_name=data["last_name"],
                    email=data["email"],
                    username=data["username"],
                    password = data["password"])

        db.session.add(user)
        db.session.commit()
        return redirect("/")

    return render_template("signup.html", form=form)
