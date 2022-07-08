from flask import Flask

app = Flask(__name__)

def create_app():

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app

if __name__ == '__main__':
    app.run(debug=True)