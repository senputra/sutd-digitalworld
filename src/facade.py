from core.WashingMachine.Constants import STATUS
from core.Action import Action
from core.WashingMachine.Actions.Update import Update


class Facade:
    """ Facade
        API:

        request_machin
    """

    def _dispatch(self, action: Action) -> None:
        return

    def updateWashingMachine(self, machineId: str, status: str) -> None:
        if STATUS.checkStatusValid(status):
            print("action is valid")
            self._dispatch(Update({
                "id": machineId,
                "status": status,
            }))
        return
