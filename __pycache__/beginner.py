import kivy
from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello world from Nobiscumdeus")
        
        #This is how to run a basic app that displays hello world

    
if __name__ =='__main__':
    MyApp().run()