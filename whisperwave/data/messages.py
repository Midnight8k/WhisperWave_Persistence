from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Messages(Base):
    """
    SQLAlchemy ORM model for the `messages` table.

    Represents a message record with the following fields:
    - `Id`: Auto-incrementing primary key.
    - `User`: ID of the user who sent the message.
    - `Message`: Text content of the message.
    - `Timestamp`: Time the message was created, typically stored as a UNIX timestamp.

    Attributes:
        Id (int): Unique identifier for the message (primary key).
        User (int): Identifier of the user who sent the message.
        Message (str): Text of the message.
        Timestamp (int): Timestamp when the message was created.
    """
    __tablename__ = "messages"

    Id = Column(Integer, primary_key=True, unique=True, autoincrement=True)

    User = Column(Integer())
    Message = Column(String())
    Timestamp = Column(Integer())

    def __init__(self, User, Message, Timestamp):
        """
        Initializes a new instance of the Messages class.

        Parameters:
            User (int): ID of the user sending the message.
            Message (str): The message content.
            Timestamp (int): The creation time of the message, as a UNIX timestamp.
        """
        self.User = User
        self.Message = Message
        self.Timestamp = Timestamp
