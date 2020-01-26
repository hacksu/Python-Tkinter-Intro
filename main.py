from tkinter import *
import time

master = Tk()
master.geometry("512x256")
master.grid_rowconfigure(0,weight=1)
master.grid_rowconfigure(1,weight=1)
master.grid_columnconfigure(0,weight=1)
master.grid_columnconfigure(1,weight=1)

timeVar = StringVar()
colorVar = StringVar()
colorVar.set("#00FF88")
reminderVar = StringVar()

def updateColor():
    colorEntry = Entry(colorFrame, textvariable=colorVar, bg=colorVar.get(), relief=RAISED)
    colorButton = Button(colorFrame, text="Update Color", bg=colorVar.get(), command=updateColor, relief=RAISED)
    colorEntry.grid(row=0, column=0, sticky=N + E + W + S)
    colorButton.grid(row=1, column=0, sticky=N + E + W + S)

label = Label(master, textvariable=timeVar, relief=RAISED)
label.grid(row=0,column=0,sticky=N+W+E+S)

colorFrame = Frame(master, relief=RAISED)
colorEntry = Entry(colorFrame, textvariable=colorVar, bg=colorVar.get(), relief=RAISED)
colorButton = Button(colorFrame, text="Update Color", bg=colorVar.get(), command=updateColor, relief=RAISED)
colorFrame.grid(row=1,column=0,sticky=N+E+W+S)
colorFrame.grid_rowconfigure(0,weight=1)
colorFrame.grid_rowconfigure(1,weight=1)
colorFrame.grid_columnconfigure(0,weight=1)
colorEntry.grid(row=0, column=0,sticky=N+E+W+S)
colorButton.grid(row=1, column=0,sticky=N+E+W+S)

def addReminder():
    reminders.append(reminderVar.get())
    reminderVar.set('')

reminderFrame = Frame(master, relief=RAISED)
reminders = ["help", "me", "understand"]
reminderList = Frame(reminderFrame, relief=RAISED)
reminderEntry = Entry(reminderFrame, textvariable=reminderVar, relief=RAISED)
reminderButton = Button(reminderFrame, text='Add Reminder', relief=RAISED, command=addReminder)
reminderFrame.grid(row=0,column=1,rowspan=2,sticky=N+E+W+S)
reminderFrame.grid_rowconfigure(0, weight=9)
reminderFrame.grid_rowconfigure(1, weight=1)
reminderFrame.grid_columnconfigure(0,weight=1)
reminderList.grid(row=0,column=0,columnspan=2,sticky=N+E+W+S)
reminderList.grid_columnconfigure(0,weight=1)
reminderEntry.grid(row=1,column=0,sticky=N+E+W+S)
reminderButton.grid(row=1,column=1,sticky=N+E+W+S)

def updateReminderList():
    for reminder in reminders:
        l = Label(reminderList, text=reminder, relief=RAISED)
        l.grid(row=reminders.index(reminder),column=0,sticky=N+E+W+S)

while(True):
    timeVar.set(time.strftime("%I:%M:%S %m/%d/%Y"))
    updateReminderList()
    master.update_idletasks()
    master.update()