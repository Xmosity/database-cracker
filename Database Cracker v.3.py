# Database Cracker Version 3.
# DISCLAIMER: Not a real hacking device obviously, sort of a password guessing game.
# Made by Xmosity.
# Dumb console game.

# Imports (why is Python so dependent on these.)
from time import sleep
import sys
import random

# Function Setups
def Setup_Database_Cracker_v3():
    sleep(1.5)
    print("Database Cracker v.3.")
    sleep(1.5)
    print("DISCLAIMER: Obviously not a real hacking device, sorry to break the mood, this is a game thing.")
    sleep(1.5)
    print("(We lost the first 2 versions of it.)")
    sleep(1.5)
    print("Made by Xmosity.")
    sleep(1.5)
    print("Case sensitive: always use all lower-case, no puncuation.")
    sleep(1.5)
    print("https://discord.gg/Y6zqBgBQWS")
    sleep(1.5)
    Main_Command_Prompt()

def Main_Command_Prompt():
    sleep(1.5)
    print("Type cmds for a list of commands!")
    sleep(1.5)
    User_Main_Command_Prompt_Input = input("Command Line: ").strip()
    def User_Main_Command_Prompt_Input_Check():
        if User_Main_Command_Prompt_Input == "cmds":
            sleep(1.5)
            print("databases: Get a list of every database.")
            sleep(0.5)
            print("cmds: Bring up the list your currently on.")
            sleep(0.5)
            print("kill: Close this program.")
            sleep(0.5)
            print("tkill: Trigger a testing kill, closes the program in style.")
            sleep(0.5)
            print("crack (database): Crack a certain database.")
            Main_Command_Prompt()
        elif User_Main_Command_Prompt_Input == "databases":
            sleep(1.5)
            print("16923328 (Username Database)")
            sleep(0.5)
            print("35530505 (Password Database)")
            sleep(0.5)
            print("70678485 (Email Database)")
            Main_Command_Prompt()
        elif User_Main_Command_Prompt_Input == "kill":
            sys.exit()
        elif User_Main_Command_Prompt_Input == "tkill":
            sleep(1.5)
            print("Killing off the program... :(")
            sleep(1.5)
            sys.exit()
        elif User_Main_Command_Prompt_Input.startswith("crack" or "crack"):
            if User_Main_Command_Prompt_Input.endswith("16923328"):
                print("Getting Username Database 16923328...")
                sleep(1.5)
            elif User_Main_Command_Prompt_Input.endswith("35530505"):
                sleep(1.5)
                print("Getting Password Database 35530505...")
            elif User_Main_Command_Prompt_Input.endswith("70678485"):
                sleep(1.5)
                print("Getting Email Database 70678485...")
                sleep(1.5)
            else:
                sleep(1.5)
                print("Invalid database.")
                Main_Command_Prompt()
        else:
            print("Invalid command, type cmds for a list of commands.")
            Main_Command_Prompt()
    User_Main_Command_Prompt_Input_Check()

# Main Code
Setup_Database_Cracker_v3()
