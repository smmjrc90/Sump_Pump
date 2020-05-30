#This module will contain custom functions written to perform tasks that can be used throughout the Home BAS code base
from datetime import datetime
import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "home.bas.system@gmail.com"  # Enter your address
password = "@1uMnu57"


def timestamp():  # function that handles all queries of what time it is
    timestampvar = datetime.now()  # gets current date and time
    return timestampvar  # reports current date and time to whatever called the function


def duration(param1, param2):  # function that handles all queries of how long something lasted, requires start and
    # end times
    end_time = param2  # sets local variable for end time
    start_time = param1  # sets local variable for start time
    elapsed_time = end_time - start_time  # calculates elapsed time base on start/end times
    return elapsed_time  # reports elapsed time to whatever called the function

def sendEmail(param1,subject,body):
    receiver_email = param1  # Enter receiver address
    message = "Subject: {}\n\n{}".format(subject,body)

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

print("Custom Functions imported at ", end="")  #terminal confirmation that the GUI was shutdown
print(timestamp())                      #timestamp of when the GUI was shutdown