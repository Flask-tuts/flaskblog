from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
mail = Mail(app)


from src.users.routes import users
from src.posts.routes import posts
from src.main.routes import main


app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)