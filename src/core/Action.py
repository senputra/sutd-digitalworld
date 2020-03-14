class Action:
    def __init__(self, action: str, payload: dict):
        self.action = action
        self.payload = payload

class UseMachineAction(Action):

    def __init__(self, machineId: str):
        self.action = "USE_MACHINE"
        self.payload = {
            "machineId": machineId,
        }

class AddMachineAction(Action):

    def __init__(self, machineId: str):
        self.action = "ADD_MACHINE"
        self.payload = {
            "machineId": machineId,
        }

class DelMachineAction(Action):

    def __init__(self, machineId: str):
        self.action = "DEL_MACHINE"
        self.payload = {
            "machineId": machineId,
        }

class CancelMachineAction(Action):

    def __init__(self, machineId: str):
        self.action = "CANCEL_MACHINE"
        self.payload = {
            "machineId": machineId,
        }