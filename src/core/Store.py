from core.Action import Action
from helper import Logger, Database
from datetime import datetime


class Reducer:
    def __init__(self):
        self._logger = Logger.Logger()
        self._database = Database.Database()

    def useMachine(self, state: dict, action: Action) -> dict:
        """ Called when user wants to use a machine
        1. Changed the state of the machine form unoccupied to occupied
        2. Push a log to firebase
        """
        patch = {
            "availability": False,
            # Get the time now
            "lastUsed":  (datetime.now() - datetime(1970, 1, 1)).total_seconds(),
        }

        self._database.create(action.payload["machineId"], patch)

        state.update({
            action.payload["machineId"]: patch
        })
        return state

    def cancelMachine(self, state: dict, action: Action) -> dict:
        """ Called when user wants to undo the machine he/she pressed
        1. Change the state form occupied to unoccupied
        2. Remove the log from firestore
        3. Remove any reminder assigned to any telegram user
        """

    def updateTelegram(self, state: dict, action: Action) -> dict:
        return state

    def errorReducer(self, state: dict, action: Action) -> dict:
        self._logger.error(
            "unrecognized action -> action: {} || payload: {}".format(action.action, action.payload))
        return state

    def reduce(self, state: dict, action: Action) -> dict:
        return {
            "USE_MACHINE": lambda state, action: self.useMachine(state, action),
            "CANCEL_MACHINE": lambda state, action: self.cancelMachine(state, action),
            "UPDATE_TELEGRAM": lambda state, action: self.updateTelegram(state, action),
        }.get(action.action, self.errorReducer)(state, action)


class Store:
    def __init__(self):
        self._logger = Logger.Logger()
        self._reducer = Reducer()

        self.state = {}
        ''' state stores the state of the machine immutably
        INITIAL STATE V1.0

            iotID : "BLK_59_Laundry" or "BLK_55_PANTRY"
            machines : {
                "BLK_59_WASHING_MASHINE_1": {
                    availability: True,
                    lastUsed: 190123910239123 #time, seconds from 1 Jan 1970
                }
            }
            machineIDs : [
                "BLK_59_WASHING_MASHINE_1",
                "BLK_59_WASHING_MASHINE_1",
            ]

        '''

    def _convert(self, action: Action):
        state = self._reducer.reduce(self.state, action)
        self._logger.log("[STATE]")
        self._logger.log("{")
        [self._logger.log("    {}: {},".format(key, value))
         for key, value in self.state.items()]
        self._logger.log("}")

    def dispatch(self, action: Action):
        self._convert(action)
        self._logger.log("[ACTION] {}".format(action.action))


if __name__ == "__main__":

    store = Store()

    a = Action("lmao", {
        "ids": 1
    })
    b = Action("USE_MACHINE", {
        "machineId": "BLK_59_Laundry",
    })

    store.dispatch(a)
    store.dispatch(b)

    d = {}
