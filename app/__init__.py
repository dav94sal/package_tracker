from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from .config import Config
from .routes import routes, session
from .models import db, User

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(routes.bp)
app.register_blueprint(session.bp)

login = LoginManager(app)
login.login_view = "session.login"


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
