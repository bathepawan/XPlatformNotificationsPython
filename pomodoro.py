from Tkinter import Tk,Button
from sys import exit
import Thread

def showPopup(s):
    popupRoot = Tk()
    popupRoot.after(2000)
    popupButton = Button(popupRoot, text = s, font = ("Verdana", 12), bg = "yellow", command = exit)
    popupButton.pack()
    popupRoot.geometry('400x50+700+500')
    popupRoot.mainloop()

if __name__=='__main__':

	while True:
		showPopup('this is notifications')

