# Coding Challenge 2





# A Morse code encoder/decoder

MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"), 
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!")
)
#morse code input into dictionary for later calling
MORSE_CODE_decoding = dict(MORSE_CODE)
MORSE_CODE_encode = {}                                                                                           
for keywrd, val in MORSE_CODE_decoding.items():
    MORSE_CODE_encode[val] = MORSE_CODE_encode.get(val, keywrd)
MORSE_CODE_encoding = MORSE_CODE_encode
#introduction for whole code
def print_intro():
    print("Welcome to Wolmorse")
    print("This program encodes and decodes Morse code.")
print_intro()
# choosing message for user to encode and decode 
def get_input():
    pass
    if selec == "e":
        user_input = input("What is the  message that you like to encode: ")
    elif selec == "d":
        user_input = input("What is the message that you like to decode: ")
    user_input = str.upper(inp_user)
    arry_choice = (inp_select, inp_user)
    return arry_choice

# code for encoding the user provided input and decoding  it with above given  morse_code 
def encode(message):
    for characters in message:
        characters = characters.upper()
        if characters != " ":
            enc = MORSE_CODE_encoding[characters]
            print(enc, "", end = "")
        elif characters == " ":
            print(" ", end = "" )

# For decoding the message which was input by user and encoding it with above given  morse_code
def decode(message):
    message += " "
    key_morse = list(MORSE_CODE_encoding.keys())
    val_morse = list(MORSE_CODE_encoding.values())
    temp = ""
    decryptor = ""
    for mors_words in message:
        if mors_words != " ":
            temp = temp + mors_words
            spaces = 0
        else:
            spaces += 1
            if spaces == 2:
                decryptor = decryptor + " "
            else:
                decryptor = decryptor + key_morse[val_morse.index(temp)]
                temp = ""
    print(decryptor)      
 
# ---------- Challenge Functions (Optional) ----------
# import the file from the os path
import os.path

def check_file_exists(filename):
    if os.path.isfile(filename) == True:
        y_n = True
    else:
        y_n = False
    return y_n
#choosing encode and decode and performing the tasl with file and console MORSE code processing

def get_filename_input():
    selec = input("Would you like to encode (e) or decode (d): ")
    while selec != "e" and selec != "d":
        print("Invalid Mode")
        selec = input("Would you like to encode(e) or decode(d) :")
    if selec == "e":
        choice = "e"
    else:
        choice = "d"
    selec = input("Would you like to like to read from a file (f) or the console (c)? ")
    if selec == "f":
        user = "None"
        fname = input("Enter Filename: ")
        while check_file_exists(fname) != True:
            print("Invalid Filename")
            fname = input("Enter Filename: ")
    else:
        fname = "None"
        if choice == "e":
            user = input("What is the  message that  you like to encode: ")
            encode(user)
            print("")
        else:
            user = input("What is message that  you like to decode: ")
            decode(user)
        user = str.upper(user)
    fin_list = (choice, user, fname)
    return fin_list

#process line file code 
def process_lines(filename, mode):
    if filename != "None":
        if mode == "e":
            empty = ""
            read_file = open(filename, "r")
            empty = ""
            for linear in read_file:
                    linear = linear.upper()
                    for char in linear:
                        if char != "\n":
                            if char != " ":
                                encode = MORSE_CODE_encoding[char]
                                empty = empty + encode + " "
                            elif char == " ":
                                empty = empty + " "
                        elif char == "\n":
                            empty = empty + "\n"
            conv = empty
            read_file.close()
        else:
            read_file = open(filename, "r")
            key_morse = list(MORSE_CODE_encoding.keys())
            val_morse = list(MORSE_CODE_encoding.values())
            temp = ""
            empty = ""
            for linear in read_file:
                linear = linear.replace('\n', ' \n')
                linear = linear + ""
                for char in linear:
                    if char != "\n":
                        if char != " ":
                            temp = temp + char
                            spaces = 0
                        else:
                            spaces = spaces + 1
                            if spaces == 2:
                                empty = empty + " "
                            else:
                                empty = empty + key_morse[val_morse.index(temp)]
                                temp = ""
                    else:
                        empty = empty + "\n"
            conv = empty
            read_file.close()
        return conv
    elif filename == "None":
        pass




def write_lines(lines):
    if lines != None:
        result = open("results.txt", "w")
        result.writelines(lines)
        result.close()
    elif lines == None:
        pass







"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encode (e) or decode (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encode/decode.
    • Encode/decode the message as appropriate and print the output.
    • Prompt the user whether they would like to encode/decode another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment specification.

Hints:
    • Use the tuple MORSE_CODE above to convert between plain text/Morse code
    • You can make use of str.split() to generate a list of Morse words and characters
      by using the spaces between words and characters as a separator.
    • You will also find str.join() useful for constructing a string from a list of strings.
    • You should use a loop to keep the programming running if the user says that would like to
      encode/decode another message after the first.
    • Your program should handle both uppercase and lowercase inputs. You can make use of str.upper()
      and str.lower() to convert a message to that case.
    • Check the assessment specification for code examples.
"""
def main(hridaya):
    if hridaya != "y":
        print_intro()
        opt = get_filename_input()
        user_choice = opt[0]
        input_user = opt[1]
        file = opt[2]
        if file != "None":
            print("Output written to results.txt")
        outputs = process_lines(file, user_choice)
        write_lines(outputs)
    else:
        opt = get_filename_input()
        user_choice = opt[0]
        input_user = opt[1]
        file = opt[2]
        if file != "None":
            print("Output written to results.txt")
        outputs = process_lines(file, user_choice)
        write_lines(outputs)

# Program execution begins here
#main code for the program execution using the function and all..

if __name__ == '__main__':
    main("y")
    selec = input('Would you like to encode/decode another message? (y/n): ')
    while selec == "y":
        main("y")
        selec = input('Would you like to encode/decode another message? (y/n): ')
    if selec == "n":
        print("Thanks for using the program, goodbye!")
