import kivy
kivy.require(''+kivy.__version__) # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class WelcomeScreen(Screen):
    pass

class Welcome(App):

    def build(self):
        return WelcomeScreen()


if __name__ == '__main__':
    Welcome().run()
