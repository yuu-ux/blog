import requests
from flask import render_template, Blueprint
# from sqlalchemy.orm import scoped_session, sessionmaker
# import config
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String

# user = config.USER
# password = config.PASSWORD
# port = config.PORT
# host = config.HOST
#
# engine = create_engine(f'mysql+mysqlconnector://{user}:{password}@{host}/blog')
#
# db_session = scoped_session(
#   sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine
#   )
# )
#
# Base = declarative_base()
# Base.query  = db_session.query_property()
#
# class Member(Base):
#   # テーブル名
#   __tablename__ = 'member'
#   # カラムの定義
#   id = Column(Integer, primary_key=True, autoincrement=True)
#   name = Column(String(200))
#
#   def __init__(self, id=None, name=None):
#       self.id = id
#       self.name = name
#
# Base.metadata.create_all(bind=engine)

root_bp = Blueprint('root_bp', __name__)

@root_bp.route('/', methods=['GET'])
def index():
    response = requests.get('https://yehara.microcms.io/api/v1/blogs', headers={'X-MICROCMS-API-KEY': 'vkp24wfI3ZpvW1fZkS5OTxygmEAYYzJzG6y7'})
    data = response.json().get('contents', [])
    return render_template('index.html', data=data)

@root_bp.route('/web', methods=['GET'])
def index_web():
    return render_template('index_web.html')
