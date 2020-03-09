from helper import Logger
from services.AdminService import AdminService

class Database:

    _database = {}
    _adminService =  AdminService()
    _userService = None
    def __init__(self):
        self._logger = Logger.Logger()

    def create(self, key: str, value: any):
        patch = {key: value}
        self._database.update(patch)
        self._logger.log(
            "[Database Create] Value : ({}, {}) ".format(key, value))

    def addMachine(self, machId):
        location, machineType, mcId = self._adminService.ID_splicer(machId)
        self._adminService.add_machine(location,machineType,mcId)

    def delMachine(self, machId):
        location, machineType, mcId = self._adminService.ID_splicer(machId)
        self._adminService.del_machine(location,machineType,mcId)

    def occupyMachine(self, machId):
        location, machineType, mcId = self._adminService.ID_splicer(machId)
        self._adminService.occupy_machine(location,machineType,mcId)
        pass

    def spoiledMachine(self, machId):
        location, machineType, mcId = self._adminService.ID_splicer(machId)
        self._adminService.spoiled_machine(location,machineType,mcId)
        pass

    def undoOccupyMachine(self, machId):
        location, machineType, mcId = self._adminService.ID_splicer(machId)
        self._adminService.undo_occupy_machine(location,machineType,mcId)
        pass

if __name__ == "__main__":
    data = Database()
    data.create("machine 1", "LMAO")
