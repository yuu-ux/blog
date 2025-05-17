from flask import Flask
from controllers.root_controller import root_bp
from controllers.login_controller import login_bp
from db.database import init_db

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db:3306/blog'
init_db(app)

url_prefix = '/'

app.register_blueprint(root_bp, url_prefix=url_prefix)
app.register_blueprint(login_bp, url_prefix=url_prefix + 'login')

if __name__ == '__main__':
    app.run()
