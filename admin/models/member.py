from sqlalchemy.orm import Mapped, mapped_column
from db.database import AuditableColumns, db
from sqlalchemy.dialects.mysql import INTEGER

class Member(AuditableColumns, db.Model):
    __tablename__ = 'member'
    id: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False, default='')
    password: Mapped[str] = mapped_column(db.String(100), nullable=False, default='')
