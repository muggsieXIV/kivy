# Program to learn how to make checkbox in kivy

# import kivy module 
import kivy

# base Class of your App inherits from the App class. 
# app:always refers to the instance of your application 
from kivy.app import App

# The :class:`Widget` class is the base class
# required for creating Widgets.
from kivy.uix.widget import Widget

# The Label widget is for rendering text.
from kivy.uix.label import Label

# To use the checkbox must import it from this module
from kivy.uix.checkbox import CheckBox

# The GridLayout arranges children in a matrix.
from kivy.uix.gridlayout import GridLayout


# Container class for the app's widgets
class check_box(GridLayout):

	def __init__(self, **kwargs):
		# super function can be used to gain access 
		# to inherited methods from a parent or sibling class 
		# that has been overwritten in a class object. 
		super(check_box, self).__init__(**kwargs)

		# 2 columns in grid layout
		self.cols = 2

		# Add checkbox, widget and labels
		self.add_widget(Label(text ='Male'))
		self.active = CheckBox(active = True)
		self.add_widget(self.active)

		self.add_widget(Label(text ='Female'))
		self.active = CheckBox(active = True)
		self.add_widget(self.active)

		self.add_widget(Label(text ='Other'))
		self.active = CheckBox(active = True)
		self.add_widget(self.active)

	
# App derived from App class
class CheckBoxApp(App):
	def build(self):	 
		return check_box()

# Run the app
if __name__ == '__main__':
	CheckBoxApp().run()
