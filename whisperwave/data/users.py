from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    Id = Column(Integer, primary_key=True, unique=True, autoincrement=True)

    Username = Column(String(), unique=True)
    TtsStatus = Column(Boolean())

    def __init__(self, Username, TtsStatus):
        self.Username = Username
        self.TtsStatus = TtsStatus
