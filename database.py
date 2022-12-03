from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class AdsModel:
    id = Column(Integer, primary_key=True, autoincrement=True)
    heading = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    create_date = Column(DateTime, nullable=False)
    owner = Column(String, nullable=False)
    