from core import Reducer, Action
from core.helper import Logger


class Store:
    """ Store class to implement redux in python """

    _reducer: Reducer
    _state: dict

    def __init__(self, reducer: Reducer, verbose=False) -> None:
        super().__init__()

        self._reducer = reducer
        self._verbsoe = verbose

    def dispatch(self, action: Action) -> None:
        self._reducer.convertActionToState(self._state, action)
        _log(action.getName())
        return

    def _log(self, message) -> None:
        if self._verbose is True:
            Logger.logToConsole(message)
