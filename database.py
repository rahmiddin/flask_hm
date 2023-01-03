import atexit
import uuid

from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, ForeignKey
from config import PG_DSN

engine = create_engine(PG_DSN)
Base = declarative_base(bind=engine)


class UserModel(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)


class AdsModel(Base):

    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True, autoincrement=True)
    heading = Column(String, index=True, nullable=False)
    description = Column(String)
    create_date = Column(DateTime)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    user = relationship(UserModel, lazy="joined")


class Token(Base):

    __tablename__ = 'tokens'

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    creation_time = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(UserModel, lazy="joined")


Base.metadata.create_all()


Session = sessionmaker(bind=engine)


atexit.register(lambda: engine.dispose())