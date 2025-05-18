from flask import Flask, g, session
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
print("★ sys.path:", sys.path)

from controllers.root_controller import root_bp
from controllers.login_controller import login_bp
from controllers.post_controller import post_bp
from db.database import init_db
from common.models.member import Member

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.secret_key = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db:3306/blog'
init_db(app)

def before_request():
    g.member = Member.fetch_active_member(session.get('member_id', None))

url_prefix = '/'

app.register_blueprint(root_bp, url_prefix=url_prefix)
app.register_blueprint(login_bp, url_prefix=url_prefix + 'login')
app.register_blueprint(post_bp, url_prefix=url_prefix + 'post')

app.before_request(before_request)
if __name__ == '__main__':
    app.run()
