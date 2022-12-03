import atexit
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import PG_DSN

engine = create_engine(PG_DSN)
Base = declarative_base(bind=engine)


class AdsModel(Base):

    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True, autoincrement=True)
    heading = Column(String, index=True, nullable=False)
    description = Column(String)
    create_date = Column(DateTime)
    owner = Column(String)

Base.metadata.create_all()


Session = sessionmaker(bind=engine)


atexit.register(lambda: engine.dispose())