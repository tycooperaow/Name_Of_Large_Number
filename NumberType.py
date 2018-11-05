import numpy
import math
import tkinter as tk
from tkinter import*

mainWin = tk.Tk()
mainWin.title('Your Number Dominion')
mainWin.resizable(False, False)
mainWin.configure(background = 'ghost white')

#============Variables==============
num = 411
presentingNum = ''
userNumber = StringVar()
typerNum = ['Ones  Place', 'Tens Place','Hundreds Place',]
largeNUM = ['Hundreds', 'Thousands', 'Millions', 'Billions', 'Trillions', 'Quadrillions', 'Quintillions', 'Sextillions', 'Septillions', 'Octillions', 'Nonillions', 'Decillions', 'Undecillion', 'Duodecillion', 'Tredecillion ', 'Quattuordecillion', 'Quindecillion', 'Sedecillion', 'Septendecillion' ]

def clicked():
       num = data.get()
       if num == ' ':
           aNum.configure(text = 'You must enter a number.')
       else:
           actualNum.configure(text = num, bg = 'SteelBlue1')
           aNum.configure(text = 'Your number results to: ', bg = 'SteelBlue1' )
           theMainFrame.configure(bg = 'SteelBlue1')
           theMainFrame.configure(width = 350)
           theMainFrame.configure(height = 200)
       print('#'*40)
       print('The number is: ' + num)

def whatType():
    userNumber = data.get()
    if (len(userNumber) - 1) % 3 == 0:
          print(typerNum[0])
          print(userNumber[0:1], end='  ')

    elif (len(userNumber) - 2) % 3 == 0:
          print(typerNum[1])
          print(userNumber[0:2],  end='  ')

    elif len(userNumber) % 3 == 0:
          print(typerNum[2])
          print(userNumber[0:3],  end='  ')

def clear():
    userNumber.set('')

def determineNumType():
       userNumber = data.get()
       if int(userNumber) <= 999 and  int(userNumber) > -1:
              print(largeNUM[0])
              whatType()

       elif int(userNumber) <= 999999 and int(userNumber) >999:
              whatType()
              print(largeNUM[1])

       elif int(userNumber) <= 999999999 and int(userNumber) > 999999:
              whatType()
              print(largeNUM[2])

       elif int(userNumber) <= 999999999999 and int(userNumber) > 999999999:
              whatType()
              print(largeNUM[3])

       elif int(userNumber) <= 999999999999999 and int(userNumber) > 999999999999:
              whatType()
              print(largeNUM[4])

       elif int(userNumber) <= 999999999999999999 and int(userNumber) > 999999999999999:
              whatType()
              print(largeNUM[5])

       elif int(userNumber) <= 999999999999999999999 and int(userNumber) > 999999999999999999:
              whatType()
              print(largeNUM[6])

       elif int(userNumber) <= 999999999999999999999999 and int(userNumber) > 999999999999999999999:
              whatType()
              print(largeNUM[7])

       elif int(userNumber) <= 999999999999999999999999999 and int(userNumber) > 999999999999999999999999:
              whatType()
              print(largeNUM[8])

       elif int(userNumber) <= 999999999999999999999999999999 and int(userNumber) > 999999999999999999999999999:
              whatType()
              print(largeNUM[9])

       elif int(userNumber) <= 999999999999999999999999999999999 and int(userNumber) > 999999999999999999999999999999:
              whatType()
              print(largeNUM[10])

       elif int(userNumber) <= 999999999999999999999999999999999999 and int(userNumber) > 999999999999999999999999999999999:
              whatType()
              print(largeNUM[11])

       elif int(userNumber) <= 999999999999999999999999999999999999999 and int(userNumber) > 999999999999999999999999999999999999:
              whatType()
              print(largeNUM[12])

       elif int(userNumber) <= 999999999999999999999999999999999999999999 and int(userNumber) > 999999999999999999999999999999999999999:
              whatType()
              print(largeNUM[13])

       elif int(userNumber) <= 999999999999999999999999999999999999999999999 and int(userNumber) > 999999999999999999999999999999999999999999:
              whatType()
              print(largeNUM[14])

       elif int(userNumber) <= 999999999999999999999999999999999999999999999999 and int(userNumber) > 999999999999999999999999999999999999999999999:
              whatType()
              print(largeNUM[15])

       elif int(userNumber) <= 999999999999999999999999999999999999999999999999999 and int(userNumber) > 999999999999999999999999999999999999999999999999:
              whatType()
              print(largeNUM[16])

       else:
            print("NUMBER HAS BEEN EXECEED")


#============Functions============

titleOfWindow = Label(mainWin, text = 'Enter a Number', fg= 'LightSteelBlue2', font = ('ariel ', 25))
titleOfWindow.configure(background = 'ghost white')
titleOfWindow.grid(row = 0, column = 0, columnspan = 5)

data = Entry(mainWin, bd = 2, insertwidth = 2, width = 30, textvariable = userNumber, font = ('ariel', 15), relief = 'sunken', justify = 'left')
data.grid(row = 1, column = 0, columnspan = 3)

numberPressed = Button(mainWin,  bg= '#003cb3', fg= 'white', font = ('Century Gothic', 20), text = 'Click', command  = lambda:[clicked(), determineNumType()],  pady= 4, padx = 4, relief = 'raised', bd = 4 )
numberPressed.grid(row = 2, column = 0)

resetButton = Button(mainWin, text = 'Reset',  font = ('Century Gothic', 20), command = clear, bd=4, bg= '#c20a0a', fg= 'white', relief = 'raised', pady = 4, padx = 4)
resetButton.grid(row=2, column = 2)

theMainFrame = Frame(mainWin, bd  = 2, width = 1, height = 1, bg = 'ghost white')
theMainFrame.grid(row = 3, column = 0, columnspan = 5)

aNum = Label(theMainFrame, text ='',  font = ('Century Gothic', 20))
aNum.grid(row = 0, column = 0)

actualNum = Label(theMainFrame, text = '', font = ('Century Gothic',12))
actualNum.grid(row = 1, column = 0, columnspan = 4, rowspan = 5)

mainWin.mainloop()
