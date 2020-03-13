from core import Store
from core.Action import UseMachineAction, AddMachineAction, CancelMachineAction, DelMachineAction
from helper import Logger, StringFormater


class Facade:
    """ Facade
        API:

        1. get machines' availability
        2. register machines's state if it is being used
        3. update telegram
        4. make telegram broadcast

    """
    BLK_NO = "Block57"

    def __init__(self):
        super().__init__()
        self.store = Store.Store()
        # Register self as a listener. With 'notify' as the trigger function
        self.store.addlistener(self)
        self.stateListeners = []
        self._logger = Logger.Logger()

    def useMachineWasher(self, machineId: str) -> None:
        if len(machineId.split("_")) != 3:
            machId = "{}_WASHER_{}".format(
                self.BLK_NO, StringFormater.force_double_digit(machineId[3:]))
            self._useMachine(machId)

    def useMachineDryer(self, machineId: str) -> None:
        if len(machineId.split("_")) != 3:
            machId = "{}_DRYER_{}".format(
                self.BLK_NO, StringFormater.force_double_digit(machineId[3:]))
            self._useMachine(machId)

    # Store mapper

    def _useMachine(self, machineId: str) -> None:
        self._dispatch(UseMachineAction(machineId))

    def cancelMachine(self, machineId: str) -> None:
        self._dispatch(CancelMachineAction(machineId))

    def addMachine(self, machineId: str) -> None:
        self._dispatch(AddMachineAction(machineId))

    def delMachine(self, machineId: str) -> None:
        self._dispatch(DelMachineAction(machineId))

    def _dispatch(self, action):
        self.store.dispatch(action)

    # Implementing listener functions
    def notify(self, newDict):
        """
            Store will notify Facade for any changes through this function
        """
        self.updateState(newDict)

    def updateState(self, newDict):
        for listener in self.stateListeners:
            listener(newDict)

    def registerStateListener(self, callback):
        self.stateListeners.append(callback)
        self._logger.warn("Current no of state listener: {}".format(
            len(self.stateListeners)))
