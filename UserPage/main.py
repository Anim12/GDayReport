import kivy
from UserPage.CreateDayData import CreateDayData
kivy.require(''+kivy.__version__) # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.lang import Builder
#from CreateDayData import main.py

class UserPage(GridLayout):
    pass

class User(App):

    def build(self):
        self.root = Builder.load_file('UserPage.kv')
        return self.root

if __name__ == '__main__':
    User().run()
