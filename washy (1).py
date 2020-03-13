import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout 

class MainWindow(Screen):
    pass
class WasherWindow(Screen):
    washer7=ObjectProperty(None)
    washer8=ObjectProperty(None)
    washer9=ObjectProperty(None)
    washer10=ObjectProperty(None)
    washer11=ObjectProperty(None)
    washer12=ObjectProperty(None)
    washer13=ObjectProperty(None)
    washer14=ObjectProperty(None)
    washer15=ObjectProperty(None)
    washer16=ObjectProperty(None)
    washer17=ObjectProperty(None)
    
    def do_action(self):
        for i in self.ids.keys():
            if self.ids[i].state=='down':
                self.ids[i].background_color=[1,0,0,1]
                #if i[-2] !=1: 
                    #washer="Block59_Washer_0" + self.ids[i].text
                #else:
                    #washer="Block59_Washer_" + self.ids[i].text

                
class DryerWindow(Screen): 
    
    dryer1=ObjectProperty(None)
    dryer2=ObjectProperty(None)
    dryer3=ObjectProperty(None)
    dryer4=ObjectProperty(None)
    dryer5=ObjectProperty(None)
    dryer6=ObjectProperty(None)
    def do_action(self):
        for i in self.ids.keys():
            if self.ids[i].state=='down':
                self.ids[i].background_color=[1,0,0,1]
                dryer="Block59_Dryer_0" + self.ids[i].text
                #if Machine_dict[dryer]=="False":
                  #  show_in_use()
               # elif Machine_dict[dryer]=="Faulty"
                #    show_faulty
               # else:
                   # Machine_dict[dryer]="False"
                    #'''db.child("_").set(Machine_dict)'''
    
    
class WindowManager(ScreenManager):
    pass

class Machine_in_Use(FloatLayout):
    pass        
def show_in_use():
    show=Machine_in_Use()
    window=Popup(title='Did not proceed',content=show,size_hint=(None,None),size=(400,400))
    window.open()

class Machine_Faulty(FloatLayout):
    pass

def show_faulty():
    show=Machine_Faulty()
    window=Popup(title='Did not proceed',content=show,size_hint=(None,None),size=(400,400))
    window.open()
    
kv= Builder.load_file("hello.kv")

class WashyApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    WashyApp().run()
    

#to put inside class so they can manipulate firebase    
'''config = {"apiKey": "CHANGE",
              "authDomain": "Change",
              "databaseURL": "Change",
}
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    Machine_dict=db.child("_").get().val()'''


#helps to manipulate the dictionary inside the class   
'''def refresh(self):
        if self.Machine_dict == db.child("_").get().val():
            pass #create a popup 
        else:
            self.Machine_dict = db.child("_").get().val()
            for i in self.ids.keys():
                if self.Machine_dict['Block59_Dryer_0'+i[3]]=='True':
                    self.ids[i].background_color=[0, .7, .2, .85] '''