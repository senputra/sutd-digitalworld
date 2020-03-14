import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

from helper import Logger
from facade import Facade


class MainWindow(Screen):
    pass


class WasherWindow(Screen):

    _facade = None

    washer7 = ObjectProperty(None)
    washer8 = ObjectProperty(None)
    washer9 = ObjectProperty(None)
    washer10 = ObjectProperty(None)
    washer11 = ObjectProperty(None)
    washer12 = ObjectProperty(None)
    washer13 = ObjectProperty(None)
    washer14 = ObjectProperty(None)
    washer15 = ObjectProperty(None)
    washer16 = ObjectProperty(None)
    washer17 = ObjectProperty(None)

    _pressedButtonId = ""

    def __init__(self, **kw):
        # Logger.Logger().log(self._facade)
        self._facade.registerStateListener(self.updateUI)
        super().__init__(**kw)

    def button_release(self):
        """Register action only when there is a release action"""

        if True:  # TODO: make some logic here to check if the machine is False beforehand
            self._facade.useMachineWasher(self._pressedButtonId)
            # self._logger.log("Register button press on {}".format(
            #     self._pressedButtonId))
        else:  # If False then get the popup
            pass

    def button_down(self):
        for buttonId, button in self.ids.items():
            if button.state == 'down':
                self._pressedButtonId = buttonId
                self._logger.log("Down on {}".format(buttonId))

    def updateUI(self, newDict):
        """
            newDict = {
                "BLK55_WASHER_01" : "True" | "False" | "broken",
                "BLK55_WASHER_02" : "True" | "False" | "broken",
                "BLK55_WASHER_03" : "True" | "False" | "broken",
            }

            a = {
                 'Block57_WASHER_07': {'availability': 'False', 'lastUsed': 1584153003.587104},
                 'Block57_WASHER_08': {'availability': 'False', 'lastUsed': 1584153007.432525},
            }
        """
        for btnId, state in newDict.items():
            # change button text
            if("WASHER" not in btnId):
                continue

            self.ids["btn{}".format(int(btnId.split("_")[-1]))].text = {
                "True": "",
                "False": "OCCUPIED",
                "broken": "BROKEN",
            }.get(state['availability'], "UNDEFINED STATE")
            # change button color
            self.ids["btn{}".format(int(btnId.split("_")[-1]))].background_color = {
                "True": [0, 0.7, 0.3, 1],
                "False": [1, 0, 0, 1],
                "broken": [1, 0.7, 0.3, 1],
            }.get(state['availability'], [0, 0.7, 0.3, 1])
        pass


class DryerWindow(Screen):

    _facade = None

    dryer1 = ObjectProperty(None)
    dryer2 = ObjectProperty(None)
    dryer3 = ObjectProperty(None)
    dryer4 = ObjectProperty(None)
    dryer5 = ObjectProperty(None)
    dryer6 = ObjectProperty(None)

    _pressedButtonId = ""

    def __init__(self, **kw):
        # Logger.Logger().log("#2")
        # Logger.Logger().log(self._facade)
        self._facade.registerStateListener(self.updateUI)
        super().__init__(**kw)

    def button_release(self):
        """Register action only when there is a release action"""
        if True:  # TODO: make some logic here to check if the machine is False beforehand
            self._facade.useMachineDryer(self._pressedButtonId)
            # self._logger.log("Register button press on {}".format(
            #     self._pressedButtonId))
        else:  # If False then get the popup
            pass

    def button_down(self):
        for buttonId, button in self.ids.items():
            if button.state == 'down':
                self._pressedButtonId = buttonId
                self._logger.log("Down on {}".format(buttonId))

    def updateUI(self, newDict):
        """
            newDict = {
                "BLK55_WASHER_01" : "True" | "False" | "broken",
                "BLK55_DRYER_02" : "True" | "False" | "broken",
                "BLK55_WASHER_03" : "True" | "False" | "broken",
            }
        """
        for btnId, state in newDict.items():
            if("DRYER" not in btnId):
                continue
            # change button text
            self.ids["btn{}".format(int(btnId.split("_")[-1]))].text = {
                "True": "",
                "False": "OCCUPIED",
                "broken": "BROKEN",
            }.get(state['availability'], "UNDEFINED STATE")
            # change button color
            self.ids["btn{}".format(int(btnId.split("_")[-1]))].background_color = {
                "True": [0, 0.7, 0.3, 1],
                "False": [1, 0, 0, 1],
                "broken": [1, 0.7, 0.3, 1],
            }.get(state['availability'], [0, 0.7, 0.3, 1])
        pass


class WindowManager(ScreenManager):
    pass


class Machine_in_Use(FloatLayout):
    pass


def show_in_use():
    show = Machine_in_Use()
    window = Popup(title='Did not proceed', content=show,
                   size_hint=(None, None), size=(400, 400))
    window.open()


class Machine_Faulty(FloatLayout):
    pass


def show_faulty():
    show = Machine_Faulty()
    window = Popup(title='Did not proceed', content=show,
                   size_hint=(None, None), size=(400, 400))
    window.open()


class WashyApp(App):

    _facade = None

    @staticmethod
    def setFacade(newFacade: Facade):
        WashyApp._facade = newFacade

    def updateNewDict(self, newDict):
        pass

    def build(self):
        Logger.Logger().log(self._facade)
        DryerWindow._logger = Logger.Logger()
        DryerWindow._facade = self._facade
        WasherWindow._logger = Logger.Logger()
        WasherWindow._facade = self._facade
        return Builder.load_file("./ui/hello.kv")


if __name__ == "__main__":
    _logger = Logger.Logger()
    WashyApp().run()
    _logger.log("EXITZAZA")

# to put inside class so they can manipulate firebase
'''config = {"apiKey": "CHANGE",
              "authDomain": "Change",
              "databaseURL": "Change",
}
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    Machine_dict=db.child("_").get().val()'''


# helps to manipulate the dictionary inside the class
'''def refresh(self):
        if self.Machine_dict == db.child("_").get().val():
            pass #create a popup 
        else:
            self.Machine_dict = db.child("_").get().val()
            for i in self.ids.keys():
                if self.Machine_dict['Block59_Dryer_0'+i[3]]=='True':
                    self.ids[i].background_color=[0, .7, .2, .85] '''
