import kivy,os
kivy.require(''+kivy.__version__) # replace with your current kivy version !
import datetime
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

class DayData(BoxLayout):
    from kivy.properties import ObjectProperty
    theTxt = ObjectProperty(None)

class CreateDayData(App):

    def build(self):
        self.root = Builder.load_file('DayData.kv')
        return self.root

if __name__ == '__main__':
    CreateDayData().run()
