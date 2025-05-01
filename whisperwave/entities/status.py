import json


class Status:
    def __init__(self) -> None:
        self._action = None
        self._message = None
        self._response = None

    @property
    def action(self):
        return self._action
    
    @action.setter
    def action(self, action):
        self._action = action

    @property
    def message(self):
        return self._message
    
    @message.setter
    def message(self, message):
        self._message = message

    @property
    def response(self):
        return self._response
    
    @response.setter
    def response(self, response):
        self._response = response

    def to_dict(self):
        return {
            "action": self._action,
            "message": self._message,
            "response": self._response
        }

    def to_json(self):
        return json.dumps(self.to_dict())

    @staticmethod
    def from_dict(data):
        status = Status()
        status.action = data.get("action")
        status.message = data.get("message")
        status.response = data.get("response")
        return status

    @staticmethod
    def from_json(json_str):
        data = json.loads(json_str)
        return Status.from_dict(data)