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
        self._adminService.manage_Machine("add",location,machineType,mcId)

    def delMachine(self, machId):
        location, machineType, mcId = self._adminService.ID_splicer(machId)
        self._adminService.manage_Machine("del",location,machineType,mcId)

if __name__ == "__main__":
    data = Database()
    data.create("machine 1", "LMAO")
