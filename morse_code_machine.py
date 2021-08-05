#!/usr/bin/env python3
#==============================================================================
# Title          : morse_code_machine
# Git            : https://github.com/user3xample/morse_code_machine
# Author         : User3xample
#
# Date           : AUG 2021
#==============================================================================
# Version        : 0.1.0
# Language       : Python3
# Licence        : For personal use only.
#==============================================================================
# Description    : Morse-code converter and decoder
# Notes          : limited to one long line of text and all uppercase.
#                  Use at your own risk.
# Usage          : $sudo python3 morse_code_machine.py
#==============================================================================


line = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

print(line)

print("Please select mode\nConvert text = 0\nDecode text = 1\n")
mode_choice = input ("Mode (0/1): ")

# Convert #########################################################################################

if mode_choice == "0":
    message_to_code = input("\nPlease enter text to encode to Morse Code:\n\n")  # Grab user input
    message_to_code = message_to_code.upper()  # Convert to UPPERCASE
    print("\n")

    def convert_to_morse(message):  # Conversion block
        #message = message.replace (" ", "/")
        message = message.replace ("1", ".----")
        message = message.replace ("2", "..---")
        message = message.replace ("3", "...--")
        message = message.replace ("4", "....-")
        message = message.replace ("5", ".....")
        message = message.replace ("6", "-....")
        message = message.replace ("7", "--...")
        message = message.replace ("8", "---..")
        message = message.replace ("9", "----.")
        message = message.replace ("0", "-----")
        message = message.replace ("A", ".-___")
        message = message.replace ("B", "-..._")
        message = message.replace ("C", "-.-._")
        message = message.replace ("D", "-..__")
        message = message.replace ("E", ".____")
        message = message.replace ("F", "..-._")
        message = message.replace ("G", "--.__")
        message = message.replace ("H", "...._")
        message = message.replace ("I", "..___")
        message = message.replace ("J", ".---_")
        message = message.replace ("K", "-.-__")
        message = message.replace ("L", ".-.._")
        message = message.replace ("M", "--___")
        message = message.replace ("N", "-.___")
        message = message.replace ("O", "---__")
        message = message.replace ("P", ".--._")
        message = message.replace ("Q", "--.-_")
        message = message.replace ("R", ".-.__")
        message = message.replace ("S", "...__")
        message = message.replace ("T", "-____")
        message = message.replace ("U", "..-__")
        message = message.replace ("V", "...-_")
        message = message.replace ("W", ".--__")
        message = message.replace ("X", "-..-_")
        message = message.replace ("Y", "-.--_")
        message = message.replace ("Z", "--.._")
        return message

    print(line)
    print(f"Initial Message:\n##{message_to_code}##\n")  # Print original message

    print(line)
    morse = convert_to_morse(message_to_code)

    print (f"Morse Code:\n##{morse}##\n")  # Print our Morsecode.

# Decode ###################################################################################

elif mode_choice == "1":
    message_to_code = input("\nPlease enter text to decode to text:\n\n")  # Grab user input
    message_to_code = message_to_code.upper()  # Convert to UPPERCASE
    print("\n")

    def convert_from_morse(message):  # Conversion block
        #message = message.replace ("/",   " ")
        message = message.replace (".----", "1")
        message = message.replace ("..---", "2")
        message = message.replace ("...--", "3")
        message = message.replace ("....-", "4")
        message = message.replace (".....", "5")
        message = message.replace ("-....", "6")
        message = message.replace ("--...", "7")
        message = message.replace ("---..", "8")
        message = message.replace ("----.", "9")
        message = message.replace ("-----", "0")
        message = message.replace (".-___", "A")
        message = message.replace ("-..._", "B")
        message = message.replace ("-.-._", "C")
        message = message.replace ("-..__", "D")
        message = message.replace (".____", "E")
        message = message.replace ("..-._", "F")
        message = message.replace ("--.__", "G")
        message = message.replace ("...._", "H")
        message = message.replace ("..___", "I")
        message = message.replace (".---_", "J")
        message = message.replace ("-.-__", "K")
        message = message.replace (".-.._", "L")
        message = message.replace ("--___", "M")
        message = message.replace ("-.___", "N")
        message = message.replace ("---__", "O")
        message = message.replace (".--._", "P")
        message = message.replace ("--.-_", "Q")
        message = message.replace (".-.__", "R")
        message = message.replace ("...__", "S")
        message = message.replace ("-____", "T")
        message = message.replace ("..-__", "U")
        message = message.replace ("...-_", "V")
        message = message.replace (".--__", "W")
        message = message.replace ("-..-_", "X")
        message = message.replace ("-.--_", "Y")
        message = message.replace ("--.._", "Z")
        return message

    print(line)
    print(f"Initial Message:\n##{message_to_code}##\n")  # Print original message

    print(line)
    morse = convert_from_morse(message_to_code)

    print (f"Morse Code:\n##{morse}##\n")  # Print our text.

print(line)
print(line)
print("Created by User3xample\n")