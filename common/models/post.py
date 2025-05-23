import logging
from datetime import datetime
from common.db.database import AuditableColumns, db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.exc import SQLAlchemyError
from common.models.category import Category


class Post(AuditableColumns, db.Model):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(
        INTEGER(unsigned=True), primary_key=True, autoincrement=True
    )
    title: Mapped[str] = mapped_column(db.String(100), nullable=False, default='無題')
    body: Mapped[str] = mapped_column(db.Text, nullable=True)
    published_at: Mapped[datetime] = mapped_column(db.DateTime(), nullable=True)
    is_draft: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    is_deleted: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    category_id: Mapped[int] = mapped_column(
        db.ForeignKey('category.id'), nullable=False
    )
    category: Mapped['Category'] = relationship('Category', backref='posts')

    @classmethod
    def save_post(cls, form, post=None):
        try:
            if post is None:
                post = cls()
                post.published_at = (
                    datetime.now() if not form.submit_draft.data else None
                )

            post.title = form.title.data
            post.body = form.body.data
            post.category_id = form.category.data
            post.is_draft = form.submit_draft.data

            db.session.add(post)
            db.session.commit()
            return post
        except SQLAlchemyError:
            logging.exception('save_post error')
            return None

    def publish_post(self):
        try:
            self.is_draft = False
            db.session.commit()
            return self
        except SQLAlchemyError:
            logging.exception('publish_post error')
            return None
