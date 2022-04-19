from  datetime import  datetime
from sqlalchemy import create_engine, Column, String, ForeignKey, Integer
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum

from app.config import DATABASE_URL

Base = declarative_base()

class StreamStatus(Enum):
    PLANED = 'planed'
    ACTIVE = 'active'
    CLOSED = 'closed'

def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    created_date = Column(String, default=datetime.utcnow())

class Stream(Base):
    __tablename__ = 'stream'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    topic = Column(String)
    status = Column(String, default=StreamStatus.PLANED.value)
    created_date = Column(String, default=datetime.utcnow())

class Authtoken(Base):
    __tablename__ = 'auth_token'

    id = Column(Integer, primary_key=True)
    token = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_date = Column(String, default=datetime.utcnow())