from datetime import datetime
from db.database import AuditableColumns, db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER
from models.category import Category

class Post(AuditableColumns, db.Model):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(db.String(100), nullable=False, default='無題')
    body: Mapped[str] = mapped_column(db.Text, nullable=True)
    published_at: Mapped[datetime] = mapped_column(db.DateTime(), nullable=True)
    is_draft: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    category_id: Mapped[int] = mapped_column(db.ForeignKey('category.id'), nullable=False)
    category: Mapped['Category'] = relationship('Category', backref='posts')
