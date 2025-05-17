from flask import Flask
from controllers.root_controller import root_bp

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

url_prefix = '/'

app.register_blueprint(root_bp, url_prefix=url_prefix)

if __name__ == '__main__':
    app.run()
