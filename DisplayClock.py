from tkinter import *
from StillClock import StillClock


class DisplayClock:

	# DisplayClock Class Object Constructor Initializer Method:
	def __init__(self):

		# Creates a Tk Widget Object Instance as the main window of the application:
		window = Tk()
		window.title("Change Clock Time")

		# Creates a StillClock Object Instance on the main window of application:
		self.clock = StillClock(window)
		self.clock.pack()

		# Creates a Frame Object Instance within the main window of application:
		frame = Frame(window)
		frame.pack()

		# Creates the Hour Label and Input Entry Objects:
		Label(frame, text = "Hour: ").pack(side = LEFT)
		self.hour = IntVar()
		self.hour.set(self.clock.getHour())
		Entry(frame, textvariable = self.hour, width = 2).pack(side = LEFT)

		# Creates the Minute Label and Input Entry Objects:
		Label(frame, text = "Minute: ").pack(side = LEFT)
		self.minute = IntVar()
		self.minute.set(self.clock.getMinute())
		Entry(frame, textvariable = self.minute, width = 2).pack(side = LEFT)

		# Creates the Second Label and Input Entry Objects:
		Label(frame, text = "Second: ").pack(side = LEFT)
		self.second = IntVar()
		self.second.set(self.clock.getMinute())
		Entry(frame, textvariable = self.second, width = 2).pack(side = LEFT)

		# Creates the Set New Time Button Object:
		Button(frame, text = "Set New Time", command = self.setNewTime).pack(side = LEFT)

		# Halts Excution of Program:
		window.mainloop()

	# DisplayClock Class Object Mutator Methods:
	def setNewTime(self):
		self.clock.setHour(self.hour.get())
		self.clock.setMinute(self.minute.get())
		self.clock.setSecond(self.second.get())	