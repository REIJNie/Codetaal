import string
import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, StringProperty


class FirstPage(FloatLayout):

    def switch1(self):
        myapp.screen_manager.transition = SlideTransition(direction="left")
        myapp.screen_manager.current = "Second"

    def switch2(self):
        myapp.screen_manager.transition = SlideTransition(direction="left")
        myapp.screen_manager.current = "Third"


class SecondPage(FloatLayout):
    text_input = ObjectProperty(None)
    text_output = ObjectProperty(None)


    def switch(self):
        myapp.screen_manager.transition = SlideTransition(direction="right")
        myapp.screen_manager.current = "First"
        self.text_input.text = ""
        self.text_output.text = ""
    
    def omvormen(self):
        
        self.text_output.text = ""
        eind = 0
        if self.text_input.text:
            while len(self.text_input.text) > eind:

                if self.text_input.text[eind] in "0123456789":
                    begin = eind
                    keuze = string.punctuation + string.ascii_uppercase + string.ascii_lowercase
                    a = 0
                    teller = 0

                    while a == 0:
                        teller += 1
                        if self.text_input.text[begin + teller] in keuze:
                            a = self.text_input.text[begin + teller]

                    eind = begin + teller
                    self.text_output.text += str(chr(int(self.text_input.text[begin:eind])))

                else:
                    self.text_output.text += self.text_input.text[eind]
                
                eind += 1

            return self.text_output.text


# Ha108V108eo 105jk b101Pn 82q101M105(jn 101<n d105tt 105js cod101{ taa108l.


class ThirdPage(FloatLayout):
    text_input = ObjectProperty(None)
    text_output = ObjectProperty(None)


    def switch(self):
        myapp.screen_manager.transition = SlideTransition(direction="right")
        myapp.screen_manager.current = "First"
        self.text_input.text = ""
        self.text_output.text = ""
    
    def omvormen(self):
        self.text_output.text = ""
        opsomming = string.ascii_lowercase + string.ascii_uppercase
        for element in self.text_input.text:
            if element in opsomming:
                self.text_output.text = self.text_output.text + str(ord(element)) + random.choice(string.punctuation + string.ascii_uppercase + string.ascii_lowercase)
            else:
                self.text_output.text += element
        return self.text_output.text


class MyApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.firstpage = FirstPage()
        screen = Screen(name="First")
        screen.add_widget(self.firstpage)
        self.screen_manager.add_widget(screen)

        self.secondpage = SecondPage()
        screen = Screen(name="Second")
        screen.add_widget(self.secondpage)
        self.screen_manager.add_widget(screen)

        self.thirdpage = ThirdPage()
        screen = Screen(name="Third")
        screen.add_widget(self.thirdpage)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


myapp = MyApp()
myapp.run()
