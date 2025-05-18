from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def init_db(app):
    db.init_app(app)

class AuditableColumns:
    created_on: Mapped[datetime] = mapped_column(db.DateTime(6), nullable=False, default=datetime.now)
    modified_on: Mapped[datetime] = mapped_column(db.TIMESTAMP, nullable=False, server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
