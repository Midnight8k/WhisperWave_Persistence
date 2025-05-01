from whisperwave.data.database_config import Database
from whisperwave.data.messages import Messages
from whisperwave.data.users import User
import time

class Repository:
    def __init__(self):
        self.database = Database()

    def add(self, user):
        users_table = User(user, True)
        self.database.create(users_table)
        self.database.commit()
    
    def remove(self, user):
        self.database.session.query(User).filter_by(Username=user).delete()
        self.database.commit()

    def activate(self, user):
        self.database.session.query(User).filter_by(Username=user).update({"TtsStatus": True})
        self.database.commit()

    def deactivate(self, user):
        self.database.session.query(User).filter_by(Username=user).update({"TtsStatus": False})
        self.database.commit()

    def message(self, user, message):
        messages_table = Messages(user, message, int(time.time()))
        self.database.create(messages_table)
        self.database.commit()

    def check(self, user) -> bool:
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
        messages_table = Messages(user, message, int(time.time()))
        self.database.create(messages_table)
        self.database.commit()
