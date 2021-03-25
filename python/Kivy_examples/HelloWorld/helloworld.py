import  kivy

from kivy.app import  App
from kivy.uix.button import Button
from kivy.uix.label import  Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout

class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen,self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text = 'User Name:'))
        self.add_widget(TextInput(multiline=False))
        self.add_widget(Label(text='Password:'))
        self.add_widget(TextInput(password = True,multiline=False))

class MyApp(App):
    def build(self):
        return LoginScreen()




if __name__ == '__main__':
    app = MyApp();
    app.run()

