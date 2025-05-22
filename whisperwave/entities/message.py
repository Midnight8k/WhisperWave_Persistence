class Message():
    """
    Domain entity representing a message.

    This class is part of the enterprise business rules layer in Clean Architecture.
    It defines the core properties and behaviors of a message independent of
    any infrastructure or framework concerns.

    Attributes:
        _id (int): Unique identifier of the message.
        _message (str): Content of the message.
        _timestamp (int): Time when the message was created, usually as a UNIX timestamp.
        _user (str): Identifier or username of the user who sent the message.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the Message entity with default None values.
        All properties must be explicitly set using their respective setters.
        """
        self._id = None
        self._message = None
        self._timestamp = None
        self._user = None

    @property
    def id(self):
        """
        Gets the ID of the message.

        Returns:
            int: Message ID.
        """
        return self.id
    
    @id.setter
    def id(self, id):
        """
        Sets the ID of the message.

        Parameters:
            id (int): Unique message identifier.
        """
        self._id = id

    @property
    def message(self):
        """
        Gets the content of the message.

        Returns:
            str: Message content.
        """
        return self._message
    
    @message.setter
    def message(self, message):
        """
        Sets the content of the message.

        Parameters:
            message (str): Message content to assign.
        """
        self._message = message

    @property
    def timestamp(self):
        """
        Gets the timestamp of when the message was created.

        Returns:
            int: Message creation time (usually UNIX timestamp).
        """
        return self._message
    
    @message.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of the message.

        Parameters:
            timestamp (int): Timestamp value (usually UNIX time).
        """
        self._timestamp = timestamp

    @property
    def user(self):
        """
        Gets the user associated with the message.

        Returns:
            str: Username or user identifier.
        """
        return self._user
    
    @user.setter
    def user(self, user):
        """
        Sets the user associated with the message.

        Parameters:
            user (str): Username or user identifier.
        """
        self._user = user
        
