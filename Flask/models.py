from flask_login import UserMixin, LoginManager
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db=SQLAlchemy()
login_manager=LoginManager()

class User(UserMixin, db.Model):
    __tablename__="Usuarios"
    id=db.Column(db.integer, primary_key=True)
    nombre=db.Column(db.String(80), nullable=False)
    email=db.Column(db.String(250), unique=True, nullable=False)
    password=db.Column(db.String(20), nullable=False)
    is_admin=db.Column(db.Boolean, default=False)

    def set_password(self, password):
        self.password=generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password,password)

