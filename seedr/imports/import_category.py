from setup_db import setup_db, AuditableColumns
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER

app, db = setup_db()
class Category(AuditableColumns, db.Model):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(db.String(30), nullable=False, unique=True)



with app.app_context():
    db.create_all()

    if not db.session.get(Category, 1):
        category = [
            Category(id = 1, name = 'web'), #type: ignore
            Category(id = 2, name = 'school'), #type: ignore
        ]
        db.session.add_all(category)
        db.session.commit()
        print('カテゴリー追加成功')
    else:
        print('すでにデータがあります')

