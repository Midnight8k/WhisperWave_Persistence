from whisperwave.data.database_config import Database
from whisperwave.data.messages import Messages
from whisperwave.data.users import User
import time

class Repository:
    """
    Repository class for managing user and message interactions with the database.

    This class abstracts and encapsulates CRUD operations and state transitions
    related to users and their messages in the application.

    Attributes:
        database (Database): An instance of the custom Database wrapper providing SQLAlchemy session access.
    """

    def __init__(self):
        """
        Initializes the Repository instance.

        - Instantiates a Database connection and stores it for session-based operations.
        """
        self.database = Database()

    def add(self, user):
        """
        Adds a new user to the database with TTS (text-to-speech) enabled by default.

        Parameters:
            user (str): Username to be added to the database.
        """
        users_table = User(user, True)
        self.database.create(users_table)
        self.database.commit()
    
    def remove(self, user):
        """
        Removes a user from the database.

        Parameters:
            user (str): Username to be removed.
        """
        self.database.session.query(User).filter_by(Username=user).delete()
        self.database.commit()

    def activate(self, user):
        """
        Activates TTS (text-to-speech) for the specified user.

        Parameters:
            user (str): Username whose TTS status will be set to True.
        """
        self.database.session.query(User).filter_by(Username=user).update({"TtsStatus": True})
        self.database.commit()

    def deactivate(self, user):
        """
        Deactivates TTS (text-to-speech) for the specified user.

        Parameters:
            user (str): Username whose TTS status will be set to False.
        """
        self.database.session.query(User).filter_by(Username=user).update({"TtsStatus": False})
        self.database.commit()

    def message(self, user, message):
        """
        Records a message in the database for the specified user.

        Parameters:
            user (str): Username who sent the message.
            message (str): Message content to be saved.
        """
        messages_table = Messages(user, message, int(time.time()))
        self.database.create(messages_table)
        self.database.commit()

    def check(self, user) -> bool:
        """
        Checks whether TTS is enabled for the specified user.

        Parameters:
            user (str): Username to check.

        Returns:
            bool: True if TTS is enabled, False otherwise or if user is not found.
        """
        status = False
        try:
            user_data = self.database.session.query(User).filter_by(Username=user).one()
            print("The TTS status is: " + str(user_data.TtsStatus))
            status = user_data.TtsStatus
        except Exception:
            print(f"User '{user}' not found.")
            status = False

        return status
    
    def say(self, user, message):
        """
        Records a message in the database for TTS output. Functionally identical to `message()`.

        Parameters:
            user (str): Username for whom the message is to be recorded.
            message (str): The message content.
        """
        messages_table = Messages(user, message, int(time.time()))
        self.database.create(messages_table)
        self.database.commit()
