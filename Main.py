#This module will be the main executable file which will in turn call on other modules to perform tasks
#from SQL_Interface import *     #imports custom module for writing to SQL Server
print("Program Started...")
print("Importing Modules")
from Steve_functions import *   #imports custom functions
from GUI import * #starts the GUI, no code after this will run until the GUI is shut down
from MS_SQL_Interface import *
print("Imports completed at ", end="")
print(timestamp())
print("Starting SQL Connection at ", end="")  #terminal confirmation that the GUI was shutdown
print(timestamp())                      #timestamp of when the GUI was shutdown
ms_sql_connection_config = ms_sql_connect('MILLER-2019-002\SQLEXPRESS', 'BASConfig',  'smiller', 'GWm50s50') #connect to MS SQL
print("SQL connection completed at ", end="")  #terminal confirmation that the GUI was shutdown
print(timestamp())                      #timestamp of when the GUI was shutdown
gui_start(ms_sql_connection_config)     #starts GUI
print("GUI was shut down at ", end="")  #terminal confirmation that the GUI was shutdown
print(timestamp())                      #timestamp of when the GUI was shutdown

print("Program Ended at ", end="")      #terminal confirmation that the program has reached the end
print(timestamp())                      #timestamp of when the GUI was shutdown