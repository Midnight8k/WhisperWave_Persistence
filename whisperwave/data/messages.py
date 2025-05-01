from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Messages(Base):
    __tablename__ = "messages"

    Id = Column(Integer, primary_key=True, unique=True, autoincrement=True)

    User = Column(Integer())
    Message = Column(String())
    Timestamp = Column(Integer())

    def __init__(self, User, Message, Timestamp):
        self.User = User
        self.Message = Message
        self.Timestamp = Timestamp
