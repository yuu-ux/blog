from setup_db import setup_db, AuditableColumns
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER

app, db = setup_db()
class Member(AuditableColumns, db.Model):
    __tablename__ = 'member'
    id: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False, default='')
    password: Mapped[str] = mapped_column(db.String(100), nullable=False, default='')

with app.app_context():
    db.create_all()

    if not db.session.get(Member, 1):
        member = Member(
            id=1,
            name="yehara",
            password="hogehoge",
        )
        db.session.add(member)
        db.session.commit()
        print('メンバー追加成功')
    else:
        print('すでにデータがあります')

