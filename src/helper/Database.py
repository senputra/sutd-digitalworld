from helper import Logger


class Database:

    _database = {}

    def __init__(self):
        self._logger = Logger.Logger()

    def create(self, key: str, value: any):
        patch = {key: value}
        self._database.update(patch)
        self._logger.log(
            "[Database Create] Value : ({}, {}) ".format(key, value))


if __name__ == "__main__":
    data = Database()
    data.create("machine 1", "LMAO")
