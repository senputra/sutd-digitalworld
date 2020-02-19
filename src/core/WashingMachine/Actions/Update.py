from core.Action import Action


class Update(Action):
    """Update Washing Machine Status

    :param _payload: A {id:string, status: Constants.status}, id of the washing machine
    """
    _name = "[Washing Machine] update status"

    # putting "int" infront of the argument enables automated typechecking
    def __init__(self, payload: dict) -> None:
        self._payload = payload

    def getPayload(self) -> dict:
        return self._payload

    def getName(self) -> str:
        return self._name + " || id: {}".format(self._payload)
