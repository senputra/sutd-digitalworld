from threading import Event, Thread


class Runner:

    __new_thread = None
    __stopped = Event()

    def __init__(self, machineID):
        self.__machineID = machineID

        #print("Thread initiated")

    # set interval

    # 1. Takes in the function and the arguments that it has to run
    # 2. After the timeInterval

    def call_repeatedly(self, interval, func, *args):
        def loop():
            # the first call is in `interval` secs
            while not self.__stopped.wait(interval):

                func(*args)
                break
            return self.__stopped.clear()

        #print("An iteration")
        self.__new_thread = Thread(target=loop)
        self.__new_thread.start()
        return self.__stopped.set

    def end_timer(self):
        return not self.__new_thread.is_alive()


'''
# Sample debugging code
b = Booking()
mac = ["Block57_Dryer_01", "Block57_Dryer_02", "Block57_Dryer_03", "Block55_Dryer_01", "Block55_Washer_01"]

for i in mac:    
    a = Runner(i)
    Loc, Type, ID = b.ID_splicer(i)
    
    a.call_repeatedly(10, b.undo_occupy_machine, Loc, Type, ID) 
    if a.end_timer():
        del a #should delete the object
'''
