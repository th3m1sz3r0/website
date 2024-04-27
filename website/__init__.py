from flask import Flask

from views import views
from auth import auth

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config['SECRET_KEY'] = 'hurpoahsfhhjlausyafdiougalsdjjggghdaawwoeutyxmzx'


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    return app