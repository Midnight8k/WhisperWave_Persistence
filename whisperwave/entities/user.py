class User:
    def __init__(self) -> None:
        self._id = None
        self._username = None
        self._tts_status = None

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id

    @property
    def username(self):
        return self.username
    
    @username.setter
    def username(self, username):
        self._username = username

    @property
    def tts_status(self):
        return self._tts_status
    
    @tts_status.setter
    def set_tts_status(self, tts_status):
        self._tts_status = tts_status
        