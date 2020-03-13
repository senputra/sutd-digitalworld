# from core.WashingMachine.Actions.Update import Update
from facade import Facade
from helper import Logger
from core.Action import Action, UseMachineAction

from ui.washy import WashyApp

if __name__ == "__main__":
    _logger = Logger.Logger()
    _logger.log("Fake UI implementation")

    facade = Facade()

    wa = WashyApp()
    wa.setFacade(facade)
    wa.run()

    # facade.updateWashingMachine("BLK59_WM_1", "spoilt")
    # facade.updateWashingMachine("BLK59_WM_1", "occupied")

    # b = Action("USE_MACHINE", {
    #     "machineId": "BLK_59_Laundry",
    # })

    # c = UseMachineAction("BLK_59_WASHING_01")
    # facade.dispatch(b)
    # facade.dispatch(c)

    # stop = False
    # while not stop:
    #     action = input("Tap which machines you want: ").upper()
    #     if action == "":
    #         stop = True
    #         break
    #     elif action.find("CANCEL") != -1 and len(action.split()) == 2:
    #         _logger.log("cancel machine" + action.split()[1])
    #         facade.cancelMachine("BLK59_WASHING_" + action.split()[1])
    #     elif action.find("ADD") != -1 and len(action.split()) == 2:
    #         facade.addMachine("BLK59_WASHING_"+action.split()[1])
    #     elif action.find("DEL") != -1 and len(action.split()) == 2:
    #         facade.delMachine("BLK59_WASHING_"+action.split()[1])
    #     elif(action.isdigit()):
    #         facade.useMachine("BLK59_WASHING_"+action)

exit
