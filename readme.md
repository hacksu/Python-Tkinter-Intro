# Python Tkinter Introduction

## Preface

[Tkinter](https://docs.python.org/3/library/tk.html) is a GUI framework for Python that allows programmers to easily create windows with any level of complexity. Tkinter is object-oriented and fairly easy to understand when approached with the correct mindset. This lesson will teach you how to create a Tkinter GUI that displays the time, allows the user to see the color based on its triple-hex value, and allows you set reminders.

The recommended IDE to use is [Pycharm](https://www.jetbrains.com/pycharm/download/), but any method of running python code will work if you have access to Tkinter.

## Simple Example

The simplest Tkinter program looks like this: 

```python
from tkinter import *

master = Tk()
master.mainloop()
```

This is no fun because you can't see anything and it does absolutely nothing. To make a better program you type this:

```python
from tkinter import *

master = Tk()
master.geometry("512x256")
master.grid_rowconfigure(0,weight=1)
master.grid_columnconfigure(0,weight=1)

l = Label(master, text="Hello, World!")
l.grid(row=0,column=0,sticky=N+W+E+S)

master.mainloop()
```

But we are getting ahead of ourselves, let's take a look at the way Tkinter works.

## Tkinter Architecture

Tkinter is built on an object of the Tk class, which is the main window. In this case it is named master due to convention, but the name is arbitrary.

```python
master = Tk()
```

This is what widgets(the name for tkinter components) will be added to. Label is one of these widgets and can be added as such:

```python
l = Label(master, text="Hello, World!")
```

As you can see in the line above, we declare an object of the class Label and pass it the parameters that it requires, namely the window to display it on and then optional parameters such as the text to display.

Finally, we must call 

```python
master.mainloop()
```

to actually run the code that is written. This is about as simple as it gets in Tkinter. The lines that were not mentioned were simply to make the window look better and will be discussed in further sections.

## Widgets

Widgets are the building blocks of Tkinter interfaces. The best resource on widgets and pretty much anything Tkinter is [tkinterbook](https://effbot.org/tkinterbook/). You can find a list of all of the widgets used in Tkinter on this site. We will use the [button page](https://effbot.org/tkinterbook/button.htm) as an example of what you can find on the website.

The page begins with a simple explanation of what the button widget does and when to use it. After that it explains the parameters in human language. After that it comes to a section titled "Reference" which is more similar to other forms of documentation. It lists all of the options that a programmer can pass to the "Button()" initialization method to alter the appearance and behavior of the button.

## Geometry Managers

Now that we have a better understanding of what we put on screen in Tkinter, we need to know how to put them on screen. The program is not a mind reader and needs to be told exactly where and how to put the widgets that you specify. This is done with geometry managers.

There are three managers in Tkinter: Place, Pack, and Grid. The manager that we will be using is Grid, but we will still quickly go over the functions of the other two. 

Straight from the tkinterbook website "The Place geometry manager is the simplest of the three general geometry managers provided in Tkinter. It allows you explicitly set the position and size of a window, either in absolute terms, or relative to another window." Place is the most customizable of the managers, but with that lack of restraint comes a lack of guardrails. It is very easy to mess up when using the place geometry manager and is not very adaptable.

From tkinterbook "The Pack geometry manager packs widgets in rows or columns. You can use options like fill, expand, and side to control this geometry manager. The manager handles all widgets that are packed inside the same master widget. The packing algorithm is simple, but a bit tricky to describe in words; imagine a sheet of some elastic material, with a very small rectangular hole in the middle. For each widget, in the order they are packed, the geometry manager makes the hole large enough to hold the widget, and then place it against a given inner edge (default is the top edge). It then repeats the process for all widgets. Finally, when all widgets have been packed into the hole, the manager calculates the bounding box for all widgets, makes the master widget large enough to hold all widgets, and moves them all to the master." If this sounds rather complicated, it is because it is. In some situations and with enough experience it can be useful, but rather unintuitive. 

Finally, the grid geometry manager. Tkinterbook states that "The grid manager is the most flexible of the geometry managers in Tkinter. If you don’t want to learn how and when to use all three managers, you should at least make sure to learn this one." Imagine there is a grid with cells of infinitesimal size, but when you put a widget in one of the cells it expands to the size of the widget. Placing a widget in the grid is done in this format:

```python
widgetName.grid(row=rowNumber, column=columnNumber)
```

Or using our code from earlier as an example:

```python
l.grid(row=0,column=0,sticky=N+W+E+S)
```

sticky simply tells the widget which directions to expand. (North, West, east, South)

## Blockage

As you remember from earlier, we call master.mainloop() to run our GUI, the problem with that is that mainloop is a blocking function. (it does not run any code after it until it is done) This can be solved by taking away mainloop and manually writing out what it consists of in our own while loop.

```python
master.mainloop()
```

is equivalent to

```python
while(True):
    master.update_idletasks()
    master.update()
```

This lets the programmer interface with outside data (such as the time) while the GUI is running. This will be crucial and we will use the latter from now on rather than the former.

## The Program

Now that you have a basic understanding of Tkinter we can create the project that was stated above. Let's recall the three features and program them in order.

## Clock

```python
from tkinter import *
import time

master = Tk()
master.geometry("512x256")
master.grid_rowconfigure(0,weight=1)
master.grid_columnconfigure(0,weight=1)

timeVar = StringVar()

label = Label(master, textvariable=timeVar)
label.grid(row=0,column=0,sticky=N+W+E+S)

while(True):
    timeVar.set(time.strftime("%I:%M:%S %m/%d/%Y"))
    master.update_idletasks()
    master.update()
```

This is what the program will look like after clock functionality has been added. We declare a string variable (a concept added by tkinter to allow the alteration of text in the GUI) and continually set that to the time formatted as "hour:minute:second month/day/year" with

```python
timeVar.set(time.strftime("%I:%M:%S %m/%d/%Y"))
```

One must also set the Label to be linked to the stringVar by setting the textvariable parameter to the name of the stringVar (in this case "timeVar")

And that is it! You should see the time displayed in the middle of the window.

## Hex colors

Now we need a way to show the color a triple-hex value such as "#00FF88". We will do this by creating a frame, adding an entry box, and a button to update it. The completed code will look like this:

```python
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

def updateColor():
    colorEntry = Entry(colorFrame, textvariable=colorVar, bg=colorVar.get())
    colorButton = Button(colorFrame, text="Update Color", bg=colorVar.get(), command=updateColor)
    colorEntry.grid(row=0, column=0, sticky=N + E + W + S)
    colorButton.grid(row=1, column=0, sticky=N + E + W + S)

label = Label(master, textvariable=timeVar)
label.grid(row=0,column=0,sticky=N+W+E+S)

colorFrame = Frame(master)
colorEntry = Entry(colorFrame, textvariable=colorVar, bg=colorVar.get())
colorButton = Button(colorFrame, text="Update Color", bg=colorVar.get(), command=updateColor)
colorFrame.grid(row=1,column=0,sticky=N+E+W+S)
colorFrame.grid_rowconfigure(0,weight=1)
colorFrame.grid_rowconfigure(1,weight=1)
colorFrame.grid_columnconfigure(0,weight=1)
colorEntry.grid(row=0, column=0,sticky=N+E+W+S)
colorButton.grid(row=1, column=0,sticky=N+E+W+S)

while(True):
    timeVar.set(time.strftime("%I:%M:%S %m/%d/%Y"))
    master.update_idletasks()
    master.update()
```

This may seem complicated, but it is very simple in reality. We create a frame, which is basically a window within the window, to house the entry and button because they can be thought of as one component rather than two because they are both part of the color picker. We then set the frame on the master, and then the entry and button on the frame. We also make another stringVar to hold the value of the entry widget and set the background color of the two widgets to be that color.

##Reminders

Now we must crown our program with the most complicated module yet: the reminder system! To create this we will make a frame to fill the right side of the screen and put another frame along with an entrybox and a button. The frame within the frame will hold the reminders, while the entry and the button will allow us to add new ones. The complete code looks like this:

```python
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
reminders = ["Test Reminder"]
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
```

Let's go through this slowly to make sure that it is understood. First, we create a frame called reminderFrame and we place it on the grid as well as configuring it to display it's contents properly.

```python
reminderFrame = Frame(master, relief=RAISED)
```
```python
reminderFrame.grid(row=0,column=1,rowspan=2,sticky=N+E+W+S)
reminderFrame.grid_rowconfigure(0, weight=9)
reminderFrame.grid_rowconfigure(1, weight=1)
reminderFrame.grid_columnconfigure(0,weight=1)
```

After this, we create the frame that will only hold the reminders and we place it on the grid.

```python
reminderList = Frame(reminderFrame, relief=RAISED)
```
```python
reminderList.grid(row=0,column=0,columnspan=2,sticky=N+E+W+S)
reminderList.grid_columnconfigure(0,weight=1)
```

Then we make the entry and the button for interactivity.

```python
reminderEntry = Entry(reminderFrame, textvariable=reminderVar, relief=RAISED)
reminderButton = Button(reminderFrame, text='Add Reminder', relief=RAISED, command=addReminder)
```
```python
reminderEntry.grid(row=1,column=0,sticky=N+E+W+S)
reminderButton.grid(row=1,column=1,sticky=N+E+W+S)
```

We then make two new functions that will handle when a new reminder is added and will tell the program how to show the reminders

```python
def addReminder():
    reminders.append(reminderVar.get())
    reminderVar.set('')
```
```python
def updateReminderList():
    for reminder in reminders:
        l = Label(reminderList, text=reminder, relief=RAISED)
        l.grid(row=reminders.index(reminder),column=0,sticky=N+E+W+S)

while(True):
    timeVar.set(time.strftime("%I:%M:%S %m/%d/%Y"))
    updateReminderList()
    master.update_idletasks()
    master.update()
```

Finally, we make the string variable to attach the entry to and then we make an array to store the reminder text

```python
reminderVar = StringVar()
```
```python
reminders = ["Test Reminder"]
```

And there it is! You now have a program that shows the time, allows you to set reminders, and displays colors!