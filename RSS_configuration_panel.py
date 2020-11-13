import tkinter
import RSS_parser_module

#Class to define GUI to manage RSS feeds, which inherits from the tkinter.Tk class 
class RSS_panel(tkinter.Tk):

	#RSS_Panel class constructor
	def __init__(self, *args, **kwargs):

		tkinter.Tk.__init__(self, *args, **kwargs) #Calling the super class constructor
		self.geometry("1500x900")
		self.resizable(False, False)
		self.label = tkinter.Label(text="Test...")
		self.label.pack(padx=10, pady=10)
