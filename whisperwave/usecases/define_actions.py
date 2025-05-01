from whisperwave.entities.status import Status
from whisperwave.data.repository import Repository
from enum import Enum

class Action(Enum):
    ADD = "add"
    REMOVE = "remove"
    ACTIVATE = "activate"
    DEACTIVATE = "deactivate"
    CHECK = "check"
    SAY = "say"


class DefineActions:
    def __init__(self) -> None:
        self.status = None
        self.repo = Repository()

    def _perform(self):
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
        print(body)
        self.status = Status.from_json(body)
        self._perform()

        return self.status.to_json()
