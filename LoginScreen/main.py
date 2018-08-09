import kivy
kivy.require(''+kivy.__version__) # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 3
        self.padding_left=2
        self.padding_top=2
        self.padding_right=2
        self.padding_bottom=2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        self.add_widget(Label(text=''))
        self.LoginButton = Button(text='Login')
        self.add_widget(self.LoginButton)

class Login(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    Login().run()
