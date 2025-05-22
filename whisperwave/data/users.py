from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy ORM model representing a user in the `users` table.

    This class is used to store information about users and whether they have
    text-to-speech (TTS) functionality enabled.

    Attributes:
        Id (int): Primary key, unique identifier for the user (auto-incremented).
        Username (str): Unique username identifying the user.
        TtsStatus (bool): Indicates whether TTS (text-to-speech) is enabled for the user.
    """
    __tablename__ = "users"

    Id = Column(Integer, primary_key=True, unique=True, autoincrement=True)

    Username = Column(String(), unique=True)
    TtsStatus = Column(Boolean())

    def __init__(self, Username, TtsStatus):
        """
        Initializes a new instance of the User class.

        Parameters:
            Username (str): The username of the user.
            TtsStatus (bool): A boolean indicating whether TTS is enabled for this user.
        """
        self.Username = Username
        self.TtsStatus = TtsStatus
