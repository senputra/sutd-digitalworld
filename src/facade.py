from core import Store
from core.Action import UseMachineAction


class Facade:
    """ Facade
        API:

        1. get machines' availability
        2. register machines's state if it is being used
        3. update telegram
        4. make telegram broadcast

    """

    def __init__(self):
        super().__init__()
        self.store = Store.Store()

    def useMachine(self, machineId: str) -> None:
        self._dispatch(UseMachineAction(machineId))
        return

    def _dispatch(self, action):
        self.store.dispatch(action)
