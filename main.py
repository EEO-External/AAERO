import kivy
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.app import App
from kivy.core.window import Window
from kivy.lang import Builder


Window.size = (300,500)

class SplashScreenApp(App):
    def build(self):
        global sm 
        sm = ScreenManager()
        Window.color = (30,109,166)
        return Image(source ='aa.png')
    
        
SplashScreenApp().run()