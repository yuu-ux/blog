from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from datetime import datetime

class Base(DeclarativeBase):
    pass

def setup_db():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@db:3306/blog'
    app.secret_key = 'secret'
    db = SQLAlchemy(model_class=Base)
    db.init_app(app)
    return app, db

app, db = setup_db()

class AuditableColumns:
    created_on: Mapped[datetime] = mapped_column(db.DateTime(6), nullable=False, default=datetime.now)
    modified_on: Mapped[datetime] = mapped_column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
