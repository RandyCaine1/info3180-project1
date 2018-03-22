from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "hVCLUIeu2D"
app.config['SQLALCHEMY_DATABASE_URI'] = "'postgres://qaizdxufksfvbh:1d8d61a7e86236e3d2605b0a2700a2efecda7024d5898b46c8db2ee43d9fe267@ec2-50-17-182-150.compute-1.amazonaws.com:5432/dci7r8pis11ro9'"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning
app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])

db = SQLAlchemy(app)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.config.from_object(__name__)
from app import views
