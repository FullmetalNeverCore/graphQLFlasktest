import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker,scoped_session


DATABASE_URI = "postgresql://ncore:root@localhost:5432/test"
engine = create_engine(DATABASE_URI)
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = Session.query_property()



"""
table users
id - primary key
uname : str 



table posts:
id - primary key
title : str 
content : str
uid -> users.id 
"""


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    uname = Column(String(255),nullable=False)
    posts = relationship('Posts',backref="author")

    def __repr__(self) -> str:
        return f'User: {self.uname}'
    
class Posts(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    content = Column(String(255))
    uid = Column(Integer, ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f'Title: {self.title}'

