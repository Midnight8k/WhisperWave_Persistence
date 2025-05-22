from whisperwave.entities.status import Status
from whisperwave.data.repository import Repository
from enum import Enum

class Action(Enum):
    """
    Enumeration for valid actions.

    Attributes:
        ADD (str): Represents the 'add' action.
        REMOVE (str): Represents the 'remove' action.
        ACTIVATE (str): Represents the 'activate' action.
        DEACTIVATE (str): Represents the 'deactivate' action.
        CHECK (str): Represents the 'check' action.
        SAY (str): Represents the 'say' action.
    """
    ADD = "add"
    REMOVE = "remove"
    ACTIVATE = "activate"
    DEACTIVATE = "deactivate"
    CHECK = "check"
    SAY = "say"


class DefineActions:
    """
    A class to execute actions based on a given status message.

    This class encapsulates the logic for performing operations on a repository based
    on the provided action. The operations include adding, removing, activating, or
    deactivating a user, as well as checking the current user's state or sending a message.
    """

    def __init__(self) -> None:
        """
        Initializes the DefineActions instance with a null status and a new Repository instance.
        """
        self.status = None
        self.repo = Repository()

    def _perform(self):
        """
        Determines and performs the appropriate repository operation based on the action value.

        The method examines `self.status.action` and carries out the following:
            - For Action.ADD: Calls `repo.add(username)` using the 'username' key from the message.
            - For Action.REMOVE: Calls `repo.remove(username)` using the 'username' key.
            - For Action.ACTIVATE: Calls `repo.activate(username)` using the 'username' key.
            - For Action.DEACTIVATE: Calls `repo.deactivate(username)` using the 'username' key.
            - For Action.CHECK: Calls `repo.check(username)` and assigns the result to `self.status.response`.
            - For Action.SAY: Calls `repo.say(username, message)`, using both the 'username' and the
              'message' keys from the message.

        If the action does not match any known value, an Exception is raised indicating that the 
        action is unrecognized.

        Raises:
            Exception: If `self.status.action` is not one of the supported actions.
        """

        if self.status.action == Action.ADD.value:
            self.repo.add(self.status.message.get("username"))
        
        elif self.status.action == Action.REMOVE.value:
            self.repo.remove(self.status.message.get("username"))
        
        elif self.status.action == Action.ACTIVATE.value:
            self.repo.activate(self.status.message.get("username"))
        
        elif self.status.action == Action.DEACTIVATE.value:
            self.repo.deactivate(self.status.message.get("username"))

        elif self.status.action == Action.CHECK.value:
            self.status.response = self.repo.check(self.status.message.get("username"))

        elif self.status.action == Action.SAY.value:
            self.repo.say(self.status.message.get("username"), 
                          self.status.message.get("message"))

        else:
            raise Exception("Unable to find the disered action. The available actions are:%s, %s, %s, %s".format(
                Action.ADD.value, Action.REMOVE.value, Action.ACTIVATE.value, Action.DEACTIVATE.value
            ))

    def execute_action(self, body):
        """
        Executes an action based on the provided JSON payload.

        This method carries out the following steps:
            1. Prints the input `body` (for logging/debugging purposes).
            2. Converts the input from JSON into a `Status` object via `Status.from_json(body)`.
            3. Calls the private `_perform()` method to execute the corresponding repository operation.
            4. Returns the updated status as a JSON-formatted string using `self.status.to_json()`.

        Parameters:
            body (str or dict): A JSON-formatted string or dictionary that must include:
                - "action": A string indicating the desired action (e.g., "add", "remove", etc.).
                - "message": A JSON object/dictionary containing necessary details such as "username",
                  and optionally a "message" field when the action is SAY.

        Returns:
            str: A JSON-formatted string reflecting the updated Status after the action has been executed.
        """
        self.status = Status.from_json(body)
        self._perform()

        return self.status.to_json()
