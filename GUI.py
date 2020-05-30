#This module creates a GUI for interaction with the Home BAS system
from Steve_functions import *
from tkinter import *
from tkinter import ttk
from equipment import *
from MS_SQL_Interface import *

def new_window(parent, title, width, height):
    new_window = Toplevel(parent)
    new_window.title(title)
    screen_width = new_window.winfo_screenwidth()
    screen_height = new_window.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)
    new_window.geometry(
        "%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))
    return new_window

def newTool(parent, title, width, height):
    window = new_window(parent, title, width, height)
    Name, Description, Manufacturer, RetailPrice, PurchasePrice, Vendor, PurchaseDate



def toggle(param):
    if param.state == False:
        param.state = True
        param.on()
    else:
        param.state = False
        param.off()
        param.record()

def gui_start(sql_connection):
    from lists import root_button_list
    root = Tk()
    root.title("Debugging GUI")
    ms_sql_select('startup', 'n/a', 'n/a', 'n/a', sql_connection, 'RootButtons', 'root_button_selections.txt')
    root_button_file = open('root_button_selections.txt')
    for line in root_button_file: # reads text file line by line and enters contents into a list
        root_button_list.append(line.replace("\n", ""))
    root_button_file.close()
    for entry in range(0, len(root_button_list)): # reads list of buttons, parses the comma delimited entries, and creates widgets from each parsed piece of data
        parsed = root_button_list[entry].split(",")
        root_button = ttk.Button(root, text=parsed[2], command=lambda:parsed[3]) #FIXME: commands are being truncated by parsing
        root_button.grid(row=entry, column=0)
    mainloop()

print("GUI imported at ", end="")  #terminal confirmation that the GUI was shutdown
print(timestamp())                      #timestamp of when the GUI was shutdown