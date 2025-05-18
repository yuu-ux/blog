import hashlib
import bcrypt
from flask import session
from sqlalchemy.orm import Mapped, mapped_column
from db.database import AuditableColumns, db
from sqlalchemy.dialects.mysql import INTEGER

class Member(AuditableColumns, db.Model):
    __tablename__ = 'member'

    id: Mapped[int] = mapped_column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(db.String(100), nullable=False, default='')
    password: Mapped[str] = mapped_column(db.String(100), nullable=False, default='')

    @staticmethod
    def login(member):
        session['member_id'] = member.id

    @staticmethod
    def fetch_active_member(member_id):
        return db.session.query(Member).filter_by(id = member_id).first()

    @staticmethod
    def check_password(input_password, target_hashed_password):
        input_sha256_hashed_password = hashlib.sha256(input_password.encode('utf-8')).hexdigest()
        return bcrypt.checkpw(input_sha256_hashed_password.encode('utf-8'), target_hashed_password.encode('utf-8'))
