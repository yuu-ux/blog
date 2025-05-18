from flask import Flask
from controllers.root_controller import root_bp
from controllers.school_controller import school_bp
from controllers.web_controller import web_bp
from settings.asset import ScssBundler
from db.database import init_db

app = Flask(__name__)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db:3306/blog'
init_db(app)

# SCSS ビルド
scss_bundler = ScssBundler(app)
scss_bundler.build()
scss_bundler.start_hot_build()

url_prefix = '/'

app.register_blueprint(root_bp, url_prefix=url_prefix)
app.register_blueprint(school_bp, url_prefix=url_prefix + 'school')
app.register_blueprint(web_bp, url_prefix=url_prefix + 'web')

if __name__ == '__main__':
    app.run()
