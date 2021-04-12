from sqlalchemy import Column, Integer, String,Date,Text,DateTime,Boolean,TypeDecorator,Float,BigInteger
from sqlalchemy import create_engine
from .config import Config
import datetime
import json

engine = create_engine(Config.DATABASE_URI, echo = True,connect_args={'check_same_thread': False})

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()

class Group(Base):
    __tablename__='group'
    id=Column(Integer,primary_key=True)
    group=Column(String)
    tag_all=Column(Boolean)
    
class Message(Base):
    __tablename__='message'
    id=Column(Integer,primary_key=True)
    group=Column(String)
    message_id=Column(Integer)
    

    
Base.metadata.create_all(engine)    