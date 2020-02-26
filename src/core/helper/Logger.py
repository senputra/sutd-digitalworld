class Logger(object):

    """
    Logger is a class that helps you print your messages during coding and 
    block all the message altogether for production.

    Logger allows user to show messages with regards to its importance.

    The verbosity of the logger is default to 3. It can be changed from
    0 to 4 (no logging to full logging). 


    USE CASE 

        logger1 = Logger()
        logger1.log("Hello this is verbosity level 3")
        logger1.verbosity = 2 #changing the verbosity
        logger1.log("Hello this is verbosity level 2")
        logger1.warn("Hello this is verbosity level 2 from warning")

        print(logger2.verbosity)

    ################################################
    ##### on your console / terminal you will see###
    [LOG] Hello this is verbosity level 3 from Logging
    [WARNING] Hello this is verbosity level 2 from Warning
    2
    ################################################

    verbosity level:
    0 = no logging
    1 = only error message
    2 = important message (warnings)
    3 = debug spam message
    """

    _verbosity = 3

    @property
    def verbosity(self) -> int:
        return type(self)._verbosity

    @verbosity.setter
    def verbosity(self, level: int):
        if (level > 3):
            type(self)._verbosity = 3
        elif (level < 0):
            type(self)._verbosity = 0
        else:
            type(self)._verbosity = level

    @verbosity.getter
    def verbosity(self):
        return type(self)._verbosity

    def log(self, message) -> None:
        if (type(self)._verbosity >= 3):
            print("[LOG]", message)
        return

    def warn(self, message) -> None:
        if (type(self)._verbosity >= 2):
            print("[WARNING]", message)
        return

    def error(self, message) -> None:
        if (type(self)._verbosity >= 1):
            print("[ERROR]", message)
        return


logger1 = Logger()
logger2 = Logger()
logger1.log("Hello this is verbosity level 3")
logger1.verbosity = 2
logger1.log("Hello this is verbosity level 2")
logger1.warn("Hello this is verbosity level 2 from warning")

print(logger2.verbosity)
