from tkinter import *
from tkinter.filedialog import *

filename = None
def newFile():
    global filename #Using the global varibale
    filename = "Untitled" #Because whenever you create a new file it is untitled
    text.delete(0.0, END)    #we're creating our main textbox for entering the text, by creating a variable called text
    #row and column, 0.0
def saveFile():
    global filename
    t = text.get(0.0, END) # Going to get all the text
    f = open(filename, 'w') #end the modew w for write
    f.write(t)
    f.close

    #Opens all the text with the textbox
    #And then opens file with the file name

def saveAs():
    f = asksaveasfile(mode = 'w', defaultextension = '.txt')#Existing in the tkinter file dialog
    t = text.get(0.0, END)  # Going to get all the text
    try: #try and except statement
        f.write(t.rstrip()) #Cuts off the whitespace underneath the text that we write into the file
    except:
        showerror(title= 'Oops!', message = "Unable to save file..") #showerror is a function of tkinter

def openfile():
    f = askopenfile(mode = 'r') #r for read
    t = f.read()
    text.delete(0.0, END) #get rid of all the text in the textbox
    text.insert(0.0, t)

root= Tk()
root.title("My Personal Text Editor")
root.minsize(width = 400, height = 400)
root.maxsize(width = 400, height = 400)

text = Text(root, width = 400, height= 400) #creating textbox finally
text.pack() #Display textbox

#Creating menu  bar
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As..", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()