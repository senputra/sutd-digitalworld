from core.WashingMachine.Actions.Update import Update
from facade import Facade


if __name__ == "__main__":
    print("Fake UI implementation")

    a = Update({
        "id": "asdf",
        "status": "empty"
    })
    print(a.getName())
    print(a.getPayload())

    facade = Facade()
    facade.updateWashingMachine("BLK59_WM_1","spoilt")
    facade.updateWashingMachine("BLK59_WM_1","occupied")
