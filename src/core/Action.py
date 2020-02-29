class Action:
    def __init__(self, action: str, payload: dict):
        self.action = action
        self.payload = payload
        pass


class UseMachineAction(Action):

    def __init__(self, machineId: str):
        self.action = "USE_MACHINE"
        self.payload = {
            "machineId": machineId,
        }
        pass
