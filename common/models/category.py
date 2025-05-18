from common.db.database import AuditableColumns, db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.mysql import INTEGER

class Category(AuditableColumns, db.Model):
    __tablename__ = 'category'

    id: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(db.String(30), nullable=False, unique=True)

