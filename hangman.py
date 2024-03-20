# Coding Challenge 3, hangman.py
# Name:Hridaya Bhattarai
# Student No: 2065693

# Hangman Game

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
# -----------------------------------
import random
import string
import os

WORDLIST_FILENAME = "words.txt"

# Responses to in-game events
# Use the format function to fill in the spaces
responses = [
    "I am thinking of a word that is {0} letters long",
    "Congratulations, you won!",
    "Your total score for this game is: {0}",
    "Sorry, you ran out of guesses. The word was: {0}",
    "You have {0} guesses left.",
    "Available letters: {0}",
    "Good guess: {0}",
    "Oops! That letter is not in my word: {0}",
    "Oops! You've already guessed that letter: {0}",
]


def choose_random_word(all_words):
    """
    Chooses a random word from those available in the wordlist
    
    Args:
        all_words (list): list of available words (strings)
    
    Returns:
        a word from the wordlist at random
    """
    let=True
    while let:
        random.choice(all_words)
        if random.choice(all_words) in random_letters:
            pass
        else:
            let=False
            return random.choice(all_words)

def load_words():
    """
    Generate a list of valid words. Words are strings of lowercase letters.

    Returns:
        A list of valid words.
    """
    file_text=open(WORDLIST_FILENAME,"r")
    all_words=file_text.read().split()
    file_text.close()
    
    return all_words
    

# Load the list of words into the variable wordlist
# Accessible from anywhere in the program
# TODO: uncomment the below line once
# you have implemented the load_words() function

def is_word_guessed(word, letters_guessed):
    """
    Determine whether the word has been guessed

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): the letters guessed so far
    
    Returns: 
        boolean, True if all the letters of word are in letters_guessed; False otherwise
    """
    
    if letters_guessed in word:
        used_letters.append(letters_guessed)
        get_remaining_letters(used_letters)
        return True
    else:
        used_letters.append(letters_guessed)
        get_remaining_letters(used_letters)
        return False


def get_guessed_word(word, letters_guessed):
    """
    Determines the current guessed word, with underscores

    Args:
        word (str): the word the user is guessing
        letters_guessed (list): which letters have been guessed so far
    
    Returns: 
        string, comprised of letters, underscores (_), and spaces that represents which letters have been guessed so far.
    """

    if len(text)==0:
        for char in word:
            if letters_guessed==char:
                text.append(letters_guessed)
            else:
                text.append("_")

    else:
        i=0
        for e in word:
            if letters_guessed==e:
                text[i]=e
            i+=1
            
    return text


def get_remaining_letters(letters_guessed):
    """
    Determine the letters that have not been guessed
    
    Args:
        letters_guessed: list (of strings), which letters have been guessed
    
    Returns: 
        String, comprised of letters that haven't been guessed yet.
    """
    from string import ascii_lowercase
    string=ascii_lowercase
    for elem in letters_guessed:
        string=string.replace(elem,"")
    return string

def get_score():
    
    ranking={}

    if not os.path.isfile("score.txt"):
        message="No Score exists"
        return message
        
    else:
        scr=open("score.txt","r")
        for lines in scr:
            ln=lines.strip("\n").split(" ")
            score=ln[0]
            name=ln[1]
            ranking.update({name:score})
        return ranking
    


def save_score(name, score):
    lst=[]
    while True:
        if os.path.isfile("score.txt")==True:
            if not os.stat("score.txt").st_size == 0:
                file=open("score.txt","r")
                lines=file.readlines()
                for line in lines:
                    stripped=line.strip("\n")
                    u_score,u_name=stripped.split(" ")
                    if name==u_name:
                        if score>=int(u_score):
                            rev=str(score)+" "+name
                            lst.append(rev)
                    else:
                        striped=line.strip("\n")
                        lst.append(striped)
                        rev=str(score)+" "+name  
                        if rev not in lst:
                            rev=str(score)+" "+name    
                            lst.append(rev)
            else:
                file=open("score.txt","w")
                rev=str(score)+" "+name
                file.write(rev)
                file.write("\n")
                lst.append(rev)
                
                
            break
        else:
            file=open("score.txt","w")
            rev=str(score)+" "+name
            file.write(rev)
            file.write("\n")
            lst.append(rev)
            
    file=open("score.txt","w")
    for elem in lst:
        file.write(elem)
        file.write("\n")
        
    file.close()

        
wordlist = load_words()
print("Loading words..")
print(len(wordlist))
print("Welcome to Hangman Ultimate Edition")


def hangman(word):
    """
    Runs an interactive game of Hangman.
    Args:
        word: string, the word to guess.
    """
    game_mech=False
    attempts=6
    
    

    #Game Menu
    while True:
        menu_input=str(input("Do you want to Play (p) view the leaderboard (l) or quit (q):").lower())

        if menu_input!="p" and menu_input!="l" and menu_input!="q":
            print("Invalid Input!")
        else:
            break
   #User_Name
    if menu_input=="p":
        print("------------")
        print("Note:Please provide full name!")
        while True:
            user_name=str(input("What is your name:").lower())
            if user_name=="":
                print("Invalid Input!")
            else:
                break
        print(responses[0].format(len(word)))
        print("------------")
        # Game UI
        while not game_mech:
            print(responses[4].format(attempts))
            print(responses[5].format(get_remaining_letters(used_letters)))
            while True:
                guessed_letter=str(input("Please guess a letter:").lower())
                if len(guessed_letter)>1 or guessed_letter==" " or guessed_letter=="":
                    print("Invalid!")
                else:
                    break
                
            if guessed_letter not in used_letters:
                if is_word_guessed(word, guessed_letter)==True:
                    get_guessed_word(word, guessed_letter)
                    print(responses[6].format(" ".join(text)))
                    print("------------")
                    
                    #Game Won!
                    if "".join(text)==word:
                        print(responses[1])
                        score=len(word)*attempts
                        print("Your total score for this game is:{}".format(score))
                        random_letters.append(word)
                        game_mech=True
                        rounds[0]+=1
                        if rounds[0]>0:
                            empty_word.clear()
                            text.clear()
                            used_letters.clear()
        
                        loop=True
                        while loop:
                            end_input=str(input("Would you like to save your score(y/n):").lower())
                            if end_input !="y" and end_input !="n":
                                print("Invalid Input")
                            else:
                                loop=False
                            if end_input=="y":
                                save_score(user_name, score)
                                print("------------")
                                intp=str(input("Would you like to restart?(y/n)").lower())
                                if intp=="y":
                                    word = choose_random_word(wordlist)
                                    hangman(word)
                                else:
                                    print("Thanks for playing, goodbye!")
                            else:
                                intp=str(input("Would you like to restart?(y/n)").lower())
                                if intp=="y":
                                    word = choose_random_word(wordlist)
                                    hangman(word)
                                else:
                                    print("Thanks for playing, goodbye!")
                                
                        
                        if end_input=="y":
                            pass
                        else:
                             print("------------")
                             word = choose_random_word(wordlist)
                             hangman(word)
                        
                # Wrong Guess! 
                else:
                    if not text:
                        print(responses[7].format(" ".join(empty_word)))
                        print("------------")
                    else:
                        print(responses[7].format(" ".join(text)))
                        print("------------")
                    vowel="aeiou"
                    if guessed_letter in vowel:
                        attempts-=2
                    else:
                        attempts-=1  
            # Guessed Repeat!   
            else:
                print(responses[8].format(" ".join(text)))
                print("------------")
                
            #Game Lost!
            if attempts<=0:
                random_letters.append(word)
                print(responses[3].format(word))
                game_mech=True
                rounds[0]+=1
                if rounds[0]>0:
                    empty_word.clear()
                    text.clear()
                    used_letters.clear()
                intp=str(input("Would you like to restart?(y/n)").lower())
                if intp=="y":
                    word = choose_random_word(wordlist)
                    hangman(word)
                else:
                    print("Thanks for playing, goodbye!")
                    
    elif menu_input=="l":
        
        ranks=get_score()
        
        if len(ranks)==0:
            print("========================")
            print("\n")
            print("   "+"No saved progress!")
            print("\n")
            print("========================")
            intp=str(input("Would you like to restart?(y/n)").lower())
            if intp=="y":
                word = choose_random_word(wordlist)
                hangman(word)
            else:
                print("Thanks for playing, goodbye!")
            
        else:   
            ranks=get_score()
            sort= sorted(ranks.items(), key=lambda t:t[1], reverse=True)
    
            print("{:<15}{:<15}".format("Score","Names"))
            print("--------------------")
            for i in range(0,len(sort)):
                print("{:<15}{:<15}".format(sort[i][1],sort[i][0]))
            print("--------------------")
            intp=str(input("Would you like to restart?(y/n)").lower())
            if intp=="y":
                word = choose_random_word(wordlist)
                hangman(word)
            else:
                print("Thanks for playing, goodbye!")
        
    else:
        print("Thanks for playing, goodbye!")
       
       
            
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the last lines to test
# (hint: you might want to pick your own
# word while you're doing your own testing)
# -----------------------------------
empty_word=[]
text=[]
used_letters=[]
rounds=[0]
random_letters=[]

# Driver function for the program
if __name__ == "__main__":
    word = choose_random_word(wordlist)
    for i in range(0,len(word)):
        empty_word.append("_")
    hangman(word)
