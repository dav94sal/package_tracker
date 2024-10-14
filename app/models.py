from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .map.map import advance_delivery, DELIVERED

db = SQLAlchemy()


class Package(db.Model):
    __tablename__ = "packages"

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.String, nullable=False)
    recipient = db.Column(db.String, nullable=False)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    user = db.relationship("User", back_populates="packages")


    @staticmethod
    def advance_all_locations():
        packages = Package.query.all()
        for package in packages:
            if package.location is not DELIVERED:
                package.location = advance_delivery(package.location,
                                                    package.destination)

        db.session.commit()


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    hashed_password = db.Column(db.String, nullable=False)

    packages = db.relationship("Package", back_populates="user")

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
