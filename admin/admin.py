from flask import Flask
from controllers.root_controller import root_bp
from controllers.login_controller import login_bp

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

url_prefix = '/'

app.register_blueprint(root_bp, url_prefix=url_prefix)
app.register_blueprint(login_bp, url_prefix=url_prefix + 'login')

if __name__ == '__main__':
    app.run()
