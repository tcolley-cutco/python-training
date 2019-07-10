#!/usr/bin/python
# ------------------------------------------------
# Script name: pyrun01cl.py
#
# Description:
# This script will take in 2 parm values and
# return those parms so they can be consumed from
# a calling CL or RPG program.
# The sample is kept very simple by design
#
# Parameters
# P1=Incoming parameter value 1
# P2=Incoming parameter value 2
# ------------------------------------------------
# ------------------------------------------------
# Imports
# ------------------------------------------------
import sys
import time
import traceback

# ------------------------------------------------
# Script initialization
# ------------------------------------------------
# Initialize or set variables
exitcode = 0  # Init exitcode
exitmessage = ''
parmsexpected = 2
# Output messages to STDOUT for logging
print("-------------------------------------------------------------------------------")
print("Sample Call from CL Program ")
# ------------------------------------------------
# Main script logic
# ------------------------------------------------
try:
    # Try to perform main logic
    # Check to see if all required parms were passed
    if len(sys.argv) < parmsexpected + 1:
        raise Exception(str(parmsexpected) + ' required parms -[Parm1] [Parm 2].Process cancelled.')
    # Set parameter work variables from command line args
    parm1 = sys.argv[1]
    parm2 = sys.argv[2]
    # Set return parm values
    print("PARM1: " + parm1)
    print("PARM2: " + parm2)
    # Set success info
    exitcode = 0
    exitmessage = 'Completed successfully'
    # ------------------------------------------------
    # Handle Exceptions
    # ------------------------------------------------
except Exception as ex:  # Catch and handle exceptions
    exitcode = 99  # set return code for stdout
    exitmessage = str(ex)  # set exit message for stdout
    # Set empty return parm values
    print("PARM1:")
    print("PARM2:")
    print('Traceback Info')  # output traceback info for stdout
    traceback.print_exc()
    # ------------------------------------------------
    # Always perform final processing
    # ------------------------------------------------
finally:  # Final processing
    # Do any final code and exit now
    # We log as much relevent info to STDOUT as needed
    print('ExitCode:' + str(exitcode))
    print('ExitMessage:' + exitmessage)
    print("End of Main Processing - " +
          time.strftime("%H:%M:%S"))
    print("-------------------------------------------------------------------------------")
    # Exit the script now
    sys.exit(exitcode)
