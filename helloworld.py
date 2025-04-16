import kivy

# Replace this with your 
# current version
kivy.require('1.11.1')   
# To find your kivy version use,
# print(kivy.__version__)

from kivy.app import App
from kivy.uix.label import Label 

class MyFirstKivyApp(App): 
	def build(self):
		return Label(text="Hello World!")


MyFirstKivyApp().run()


