# from core.WashingMachine.Actions.Update import Update
from facade import Facade
from helper import Logger
from core.Action import Action, UseMachineAction

if __name__ == "__main__":
    _logger = Logger.Logger()
    _logger.log("Fake UI implementation")

    facade = Facade()
    # facade.updateWashingMachine("BLK59_WM_1", "spoilt")
    # facade.updateWashingMachine("BLK59_WM_1", "occupied")

    # b = Action("USE_MACHINE", {
    #     "machineId": "BLK_59_Laundry",
    # })

    # c = UseMachineAction("BLK_59_WASHING_01")
    # facade.dispatch(b)
    # facade.dispatch(c)

    stop = False
    while not stop:
        action = input("Tap which machines you want: ")
        if action == "":
            stop = True
            break
        else:
            facade.useMachine("BLK_59_WASHING_"+action)

exit
