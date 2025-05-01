class Message():
    def __init__(self) -> None:
        self._id = None
        self._message = None
        self._timestamp = None
        self._user = None

    @property
    def id(self):
        return self.id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self, message):
        self._message = message

    @property
    def timestamp(self):
        return self._message
    
    @message.setter
    def timestamp(self, timestamp):
        self._timestamp = timestamp

    @property
    def user(self):
        return self._user
    
    @user.setter
    def user(self, user):
        self._user = user
        
