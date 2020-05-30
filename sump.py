# this module is for handling the calculations regarding the sump pump. Will only run on Raspberry Pi

from gpiozero import Button as currentSwitch  # using gpiozero's button class for all current switch devices
from signal import pause  # used to keep the program running without a loop
import Steve_functions
from equipment import *


############################################################################################
# this section of code makes a timestamp on the terminal of when the program started running
print("Sump module started running at ", end="")
program_start = timestamp()
############################################################################################

############################################################################################
# this section of code sets up the digital input for the sump pump current switch
sumpPumpSwitch = currentSwitch(23, pull_up=False)  # using gpiozero imported button as current switch
sumpPumpSwitch.when_pressed = sumpPump.on  # runs when the pump turns on
sumpPumpSwitch.when_released = lambda: sumpPump.off()  # runs when the pump turns off
#############################################################################################
pause()
