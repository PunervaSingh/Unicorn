from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
import razorpay
from flask_mail import Mail

keyid = 'rzp_test_72b14Bb260520s'
keysecret = 'BpIsSYWreMjd2bN4BRKamo5Q'

app = Flask(__name__)
razorpay_client = razorpay.Client(auth=(keyid, keysecret))
app.config['SECRET_KEY'] = '7adc3fc0925de76b452faf237e6e1f7e'

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
admin = Admin(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'phoenix.we9574@gmail.com'
app.config['MAIL_PASSWORD'] = 'yjnmbueyoogojjgs'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['TESTING'] = False
mail = Mail(app)

from flask_app import routes 