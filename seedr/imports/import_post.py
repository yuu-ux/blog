from datetime import datetime
from setup_db import setup_db, AuditableColumns
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.mysql import INTEGER

app, db = setup_db()

class Category(AuditableColumns, db.Model):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(db.String(30), nullable=False, unique=True)

class Post(AuditableColumns, db.Model):
    __tablename__ = 'post'

    id: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(db.String(100), nullable=False, default='無題')
    body: Mapped[str] = mapped_column(db.Text, nullable=True)
    published_at: Mapped[datetime] = mapped_column(db.DateTime(), nullable=True)
    is_draft: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    is_deleted: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    category_id: Mapped[int] = mapped_column(db.ForeignKey('category.id'), nullable=False)
    category: Mapped['Category'] = relationship('Category', backref='posts')



with app.app_context():
    db.create_all()

    if not db.session.get(Post, 1):
        post = [
            Post(
                title='Pythonの基本文法',
                body='Pythonはインデントでブロックを表現する言語です。',
                published_at=datetime(2024, 1, 10, 10, 0),
                is_draft=False,
                is_deleted=False,
                category_id=1,
            ),
            Post(
                title='FlaskでWebアプリ開発',
                body='FlaskはPython製の軽量なWebフレームワークです。',
                published_at=datetime(2024, 2, 5, 14, 30),
                is_draft=False,
                is_deleted=False,
                category_id=1,
            ),
            Post(
                title='新学期の準備',
                body='新しい教科書や文房具をそろえよう。',
                published_at=datetime(2024, 3, 20, 9, 0),
                is_draft=False,
                is_deleted=False,
                category_id=2,
            ),
            Post(
                title='読書感想文の書き方',
                body='感想文はあらすじではなく、自分の考えを書くことが大切です。',
                published_at=datetime(2024, 4, 12, 16, 45),
                is_draft=False,
                is_deleted=False,
                category_id=2,
            ),
            Post(
                title='下書き記事',
                body='これはまだ公開されていない記事の内容です。',
                published_at=None,
                is_draft=True,
                is_deleted=False,
                category_id=1,
            ),
        ]
        db.session.add_all(post)
        db.session.commit()
        print('ポスト追加成功')
    else:
        print('すでにデータがあります')

