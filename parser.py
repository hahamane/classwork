#! usr/bin/env python
# 1. load dataset from a file
# 2. organize the text file so we can access columns or rows of it easily
# 3. if the file does not have header, ask user if the user wants to add header. If yes, add
# 3. compute some summary stats about the dataset
# 4. plot histogram of a chosen column
# 5. plot scatter plot of 2 chosen column


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

checkHeader = True

try:
# If the first value is not a float, it means that there is header
	checkHeader = float(data.iloc[0,0])
# By changing the checkHeader as false we can later add the headers
	checkHeader = False

except ValueError:
	
	data = pd.read_csv(myfile, sep='\s+|,', engine = 'python')

if checkHeader == False:
	check = False

# If the user inputs wrong value, the program will keep on asking

	while check == False:
		answerHeader = input("Would you like to add header? Y/N")
		
# 3.If the answer is Yes then ask for the header

		if answerHeader =="Y" or answerHeader == "y":
			headerArray = []

# 3a. Ask for the header and store it in the headerArray arry			
			
			for i in range(0, len(data.columns)):
				header = input("What is the header for " +str(i+1)+("th column?"))	
				headerArray.append(header)

# 3b. Adding the header
			
			data = pd.read_csv(myfile, sep='\s+|,', names = headerArray, engine = 'python')
			check = True

# 3c. If the user does not want to add header, then just change check into True to exit the loop

		elif answerHeader =="N" or answerHeader == "n":
			check = True

# If the user inputs other than Y or N, then keep the check as false to rerun the question

		else:
			print("Please input correct option")

# 4. Compute some summary stats of the dataset
def getStats():
	check = True

# Ask which statistics the user wants. Using try/except, catch if the user does not
# input the required option

	while check == True:

		print("1. Averages of the columns")
		print("2. Standard Deviations of the columns")
		print("3. Exit")
		try:
			choice = int(input())

			if choice == 1:
				print("Printing averages of the columns")
				print(np.mean(data))
			elif choice == 2:
				print("Printing standard deviations of the columns")
				print(np.std(data))
			elif choice == 3:
				check = False
			else :
				print("Please choose the correct option")
		except ValueError:
			print("Please choose the correct option")

# 5. printing histogram
def getHistogram():

# 5a. Ask which column the user wants the histogram

	choice = getColumn()
# 5b. Using the result of the getColumn, plot the histogram

	data.iloc[:,choice-1].plot.hist()	
	plt.title(str(list(data.columns.values[choice-1])))
	plt.ylabel("Counts")
	plt.xlabel(str(list(data.columns.values[choice-1])))
	plt.show()

# This method will return the index of the column that the user choses
def getColumn():
	
	# Printing the headers of the columns for the user to chose
	for i in range(0, len(data.columns)):
		print(str(i+1) + " " + str(list(data.columns.values[i])))
	check = True
	while check ==True:
		try:
			choice = int(input("which data would you like?"))
			
		except ValueError:
			print("Please choose correct option")
		if choice > len(data.columns):
			print("Please choose correct option")
		else:
			check = False
	return choice


# 6.  printing pair plot
def getPairPlot():
# 6a. Ask for the columns to be plotted.

	print("First column")
	firstChoice = getColumn()
	print("Second column")
	secondChoice = getColumn()

# 6b. Plot using the 2 columns user wants

	plt.scatter(data.iloc[:,firstChoice-1], data.iloc[:,secondChoice-1])
	plt.title(str(list(data.columns.values[firstChoice-1] ))+ " vs " + str(list(data.columns.values[secondChoice-1])))
	plt.xlabel(str(list(data.columns.values[firstChoice-1] )))
	plt.ylabel(str(list(data.columns.values[secondChoice-1])))

	plt.show()

# This method will print the first 5 rows of data
def getData():
	print("Printing the data")
	print(data.head())

# This method is the menu method
def mainMenu(): 
	check = True
	while check == True:
		check = False
		print("What would you like to do?")
		print("1. View first 5 entries of data")
		print("2. View Summary stats")
		print("3. View Histogram")
		print("4. View Scatter plots of 2 columns chosen")
		print("5. Exit")

		choice = input()
		if choice == "1":
			getData()
			check = True
		elif choice == "2":
			getStats()
			check = True
		elif choice == "3":
			getHistogram()
			check = True
		elif choice == "4":
			getPairPlot()
			check = True
		elif choice == "5":
			check = False
		else:
			print("Please enter valid option")
			check = True

# Run the program
mainMenu()
