from abc import abstractmethod


class Action:
    """ base Action class

    This is an interface that needs implementation

    :param _name: A string, Action name
    :param _action: A string, type of action
    :param _payload: An object, Action payload; can be None

    """

    @abstractmethod
    def getPayload(self):
        return

    @abstractmethod
    def getName(self):
        return
