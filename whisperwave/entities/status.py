import json


class Status:
    """
    Domain entity representing the status of an operation or action.

    This entity encapsulates a standard way to represent feedback from business
    logic in a clean and framework-agnostic format, suitable for use across
    application layers (e.g., responses, logs, or internal communication).

    Attributes:
        _action (str): The action or command that was executed.
        _message (str): A human-readable message describing the status.
        _response (Any): A generic response payload associated with the action.
    """

    def __init__(self) -> None:
        """
        Initializes a new Status instance with default None values.
        Use setters or deserialization methods to populate data.
        """
        self._action = None
        self._message = None
        self._response = None

    @property
    def action(self):
        """
        Gets the action associated with this status.

        Returns:
            str: The name or type of the action performed.
        """        
        return self._action
    
    @action.setter
    def action(self, action):
        """
        Sets the action associated with this status.

        Parameters:
            action (str): A description or identifier of the action.
        """        
        self._action = action

    @property
    def message(self):
        """
        Gets the human-readable status message.

        Returns:
            str: A message explaining the result or status.
        """        
        return self._message
    
    @message.setter
    def message(self, message):
        """
        Sets the status message.

        Parameters:
            message (str): A human-readable explanation of the result.
        """        
        self._message = message

    @property
    def response(self):
        """
        Gets the response payload associated with this status.

        Returns:
            Any: A generic response, can be a string, dict, or custom object.
        """
        return self._response
    
    @response.setter
    def response(self, response):
        """
        Sets the response payload.

        Parameters:
            response (Any): Data related to the result of the action.
        """
        self._response = response

    def to_dict(self):
        """
        Converts the Status object to a dictionary.

        Returns:
            dict: A dictionary representation of the status.
        """
        return {
            "action": self._action,
            "message": self._message,
            "response": self._response
        }

    def to_json(self):
        """
        Converts the Status object to a JSON string.

        Returns:
            str: JSON-encoded representation of the status.
        """
        return json.dumps(self.to_dict())

    @staticmethod
    def from_dict(data):
        """
        Creates a Status instance from a dictionary.

        Parameters:
            data (dict): A dictionary with keys 'action', 'message', and 'response'.

        Returns:
            Status: A new Status instance populated with the dictionary data.
        """
        status = Status()
        status.action = data.get("action")
        status.message = data.get("message")
        status.response = data.get("response")
        return status

    @staticmethod
    def from_json(json_str):
        """
        Creates a Status instance from a JSON string.

        Parameters:
            json_str (str): JSON string representing a Status.

        Returns:
            Status: A new Status instance deserialized from JSON.
        """
        data = json.loads(json_str)
        return Status.from_dict(data)