from core import Reducer, Action
from core.helper import Logger


class Store:

    class StoreTYPE:
        WASHING_MACHINE = "washing_machine"
        DRYING_MACHINE = "drying_machine"

    """ Store class to implement redux in python """

    # _reducer: Reducer
    # _state: dict

    _cache: dict = {
        "washing_machine": {},
        "drying_machine": {},
    }

    def __init__(self, verbose=False) -> None:
        super().__init__()

        self._verbsoe = verbose
        self._callbacks = []

    def upsert(self, feature: str, id: str, value) -> None:
        if (feature not in _cache.keys()):
            _log("ERROR: feature not found")
            return
        self._cache[feature][id] = value

        # Notifies listeners on changes in values
        self.notify()
        return

    def addListener(self, callbackFn):
        return self._callbacks.append(callbackFn)

    def removeListener(self, callbackFn):
        return self._callbacks.remove(callbackFn)

    def notify(self):
        for callback in self._callbacks:
            callback()
        return

    # def dispatch(self, action: Action) -> None:
    #     self._reducer.convertActionToState(self._state, action)
    #     _log(action.getName())
    #     return

    def _log(self, message) -> None:
        if self._verbose is True:
            Logger.logToConsole("[STORE] " + message)
