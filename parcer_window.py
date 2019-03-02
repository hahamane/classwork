#! usr/bin/env python
# 1. load dataset from a file
# 2. organize the text fie so we can access columns or rows of it easily
# 3. compute some summary stats about the dataset
# 4. print those summary stats


# 1. load a dataset
# 1a. import the dataset

# The reason why using argparse instead of input() is for automation
# With input(), name is required to be inputed all the time
# But with argparse, we can automate it using ls | ...

from argparse import ArgumentParser
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
from tkinter import * 

parser = ArgumentParser(description = 'A CSV Reader + stats maker')
parser.add_argument ('csvfile', type=str,help='Path')
parsed_args=parser.parse_args()
myfile = parsed_args.csvfile
import os 
import os.path as op

assert op.isfile(myfile), "give a real file"

print("file is here")

# 1b load the dataset
# To install pandas:
# pip3 install --upgrade pip --user
# pip3 install pandas --user
# pip3 freeze | grep pandas to check the version of pandas
# pip3 freeze will give all the versions of packages

import pandas as pd

data = pd.read_csv(myfile, sep='\s+|,', header=None, engine = 'python')

# Checking if the header exists
# If the first value of the table is a string, that means that 
# there is a header. Therefore, check the header, then act accordingly

try:
	checkHeader = float(data.iloc[0,0])
	print(checkHeader)

except ValueError:
	
	data = pd.read_csv(myfile, sep='\s+|,', engine = 'python')




# 3. Compute some summary stats of the dataset




# 4. printing histogram

def chooseColumn():
	
	# Printing the headers of the columns for the user to chose

	for i in range(0, len(data.colums)):
		print("1: " + str(list(data.columns.values[i])))

	choice = input("which data would you like to view")
	return int(choice)+1


# 5. printing pair plot
def pairPlot():
	for i in range(0, len(data.columns)):

		for k in range (i, len(data.columns)):

			plt.scatter(data.iloc[:,i], data.iloc[:,k])
			plt.title(str(list(data.columns.values[i] ))+ " vs " + str(list(data.columns.values[k])))
	#		plt.show()


# Printing the file in different window
class Window (Frame):
	def getHistogram(self, choice):
		#print("hello" + str(choice))

		#histogramWindow = Toplevel (master = self)

		data.iloc[:,choice].plot.hist()
		plt.title(str(list(data.columns.values[choice])))
		plt.show()

	def columnChoice(self):
		columnWindow= Toplevel(master = self)
		columnWindow.title("Choose the Column you want to see")
		for i in range(0, len(data.columns)):
			columnChoice = Button (columnWindow, text = str(i+1)+" " + str(list(data.columns.values[i])),command=self.getHistogram(i))
			columnChoice.pack()
		exitButton = Button(columnWindow, text='Exit', width=25,command=columnWindow.destroy)
		exitButton.pack()



	def statSummary(self):
		statSum = Toplevel(self)
		statSum.title("Summary Statistics")
		averageTitle = Label (statSum, text = "Averages of the columns")
		average = Label (statSum, text = np.mean(data))
		stdTitle = Label (statSum, text = "Standard deviations of the columns")
		std = Label (statSum, text = np.std(data))
		exitButton = Button(statSum, text='Exit', width=25,command=statSum.destroy)
		averageTitle.pack()
		average.pack()
		stdTitle.pack()
		std.pack()
		exitButton.pack()

	def __init__(self, master=None):
		Frame.__init__(self,master)
		self.master = master
		self.init_window()

	def init_window(self):
		self.master.title("Analysis")
		self.pack(fill=BOTH, expand=1)
		quitbutton = Button (self, text="Quit", width=25,command=self.client_exit)
		statButton = Button(self, text='Summary Statistics', width=25, command = self.statSummary)
		HistogramButton = Button(self, text='Histogram', width=25, command = self.columnChoice)
		statButton.pack()
		HistogramButton.pack()
		quitbutton.pack()
	def client_exit(self):
		exit()


root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()
#root = tk.Tk()
#root.title('Analysis')

#statButton = tk.Button(root, text='Summary Statistics', width=25, command=statSummary())
#histogramButton = tk.Button(root, text='Histograms', width = 25, command=plotHistogram())
#pairButton = tk.Button(root, text='Scatter Plot', width = 25, command=pairPlot())
#exitButton = tk.Button(root, text='Exit', width=25,command=root.destroy)
#statButton.pack()
#histogramButton.pack()
#pairButton.pack()
#exitButton.pack()
#root.mainloop()