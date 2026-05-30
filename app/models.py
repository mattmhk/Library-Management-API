from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from datetime import date


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    quantity: Mapped[int] = mapped_column(nullable=False, default=0)


class Member(Base):
    __tablename__ = "members"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)


class Borrow(Base):
    __tablename__ = "borrows"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    book_id: Mapped[int] = mapped_column(nullable=False)
    member_id: Mapped[int] = mapped_column(nullable=False)
    borrowed_at: Mapped[date] = mapped_column(Date, default=date.today, nullable=False)
    returned_at: Mapped[date] = mapped_column(Date, nullable=True)