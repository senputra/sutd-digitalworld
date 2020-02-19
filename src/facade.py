from core.WashingMachine.Constants import STATUS
from core.Action import Action
from core.WashingMachine.Actions.Update import Update
from core.Store import Store
from core.Reducer import Reducer


class Facade:
    """ Facade
        API:

        request_machin
    """

    def __init__(self):
        super().__init__()
        self.store = Store(verbose=True)

    def requestDataFromFirestore(self) -> None:
        # Call a funtion from Long&Weisi's code and bind with a callback
        return

    def listeningToWashingMachineStatus(self, callback) -> None:
        """ listening to the status of wanted object"""
        '''
            bind a callback 
            if there is a new data
            call the callback with the payload


            Data is in dict: {
                "BLK55_WM_1" : "occupied",
                .
                .
                .
            }
        '''
        callback(self._washingMachineData)
        return

    def updateWashingMachine(self, machineId: str, status: str) -> None:
        if STATUS.checkStatusValid(status):
            print("action is valid")
            self._dispatch(Update({
                "id": machineId,
                "status": status,
            }))
        return
