from services import Logger
class Runner:

    _logger = None

    def __init__(self):
        self._logger = Logger.Logger()

    """
    set interval 

    1. Takes in the function and the arguments that it has to run 
    2. After the timeInterval

    https://stackoverflow.com/questions/12435211/python-threading-timer-repeat-function-every-n-seconds/16368571#16368571
    https://stackoverflow.com/questions/22498038/improve-current-implementation-of-a-setinterval-python/22498708#22498708
    """
    def set_interval(self, function, timeInterval:int):
        self._logger.log("NOT IMPLEMENTED")
        pass 