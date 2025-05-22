class User:
    """
    Domain entity representing a user.

    This class is part of the enterprise business rules layer in a Clean Architecture
    setup. It models the essential properties of a user without any dependencies
    on frameworks or infrastructure.

    Attributes:
        _id (int): Unique identifier of the user.
        _username (str): Username used to identify the user.
        _tts_status (bool): Indicates whether text-to-speech (TTS) is enabled for this user.
    """

    def __init__(self) -> None:
        """
        Initializes a new User instance with default values.
        All attributes should be set using the provided setters.
        """
        self._id = None
        self._username = None
        self._tts_status = None

    @property
    def id(self):
        """
        Gets the ID of the user.

        Returns:
            int: The unique identifier of the user.
        """        
        return self._id
    
    @id.setter
    def id(self, id):
        """
        Sets the ID of the user.

        Parameters:
            id (int): Unique identifier to assign to the user.
        """        
        self._id = id

    @property
    def username(self):
        """
        Gets the username of the user.

        Returns:
            str: The user's username.
        """        
        return self.username
    
    @username.setter
    def username(self, username):
        """
        Sets the username of the user.

        Parameters:
            username (str): A unique name to identify the user.
        """        
        self._username = username

    @property
    def tts_status(self):
        """
        Gets the TTS (text-to-speech) status for the user.

        Returns:
            bool: True if TTS is enabled; False otherwise.
        """
        return self._tts_status
    
    @tts_status.setter
    def set_tts_status(self, tts_status):
        """
        Sets the TTS (text-to-speech) status for the user.

        Parameters:
            tts_status (bool): Flag indicating whether TTS is enabled.
        """        
        self._tts_status = tts_status
        