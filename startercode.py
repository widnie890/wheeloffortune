from calendar import c
from config import dictionaryloc
from config import turntextloc
from config import wheeltextloc
from config import maxrounds
from config import vowelcost
from config import roundstatusloc
from config import finalprize
from config import finalRoundTextLoc

import random

players={0:{"roundtotal":0,"gametotal":0,"name":""},
         1:{"roundtotal":0,"gametotal":0,"name":""},
         2:{"roundtotal":0,"gametotal":0,"name":""},
        }

roundNum = 0
dictionary = []
turntext = ""
wheellist = []
roundWord = ""
blankWord = []
vowels = {"a", "e", "i", "o", "u"}
roundstatus = ""
finalroundtext = ""


def readDictionaryFile():
    global dictionary
    d = open(dictionaryloc)
    words = d.read().splitlines()
    d.close()

    for line in words:
        dictionary.append(line)
    # Read dictionary file in from dictionary file location
    # Store each word in a list.
      
    
def readTurnTxtFile():
    global turntext
    t = open(turntextloc)
    turn = t.read()
    t.close
  #read in turn intial turn status "message" from file

        
def readFinalRoundTxtFile():
    global finalroundtext
    f = open(finalRoundTextLoc)
    final = f.read()
    f.close
#read in turn intial turn status "message" from file

def readRoundStatusTxtFile():
    global roundstatus
    s = open(roundstatusloc)
    status = s.read()
    s.close
    # read the round status  the Config roundstatusloc file location 

def readWheelTxtFile():
    global wheellist
    w = open(wheeltextloc)
    wheel = w.read().splitlines()
    w.close()

    for line in wheel:
        wheellist.append(line)
    # read the Wheel name from input using the Config wheelloc file location 
    
def getPlayerInfo():
    global players
    players[0]["name"] = input("Player 0, What's your name?:")
    players[1]["name"] = input("Player 1,What's your name?:")
    players[2]["name"] = input("Player 2,What's your name?:")

    # read in player names from command prompt input


def gameSetup():
    # Read in File dictionary
    # Read in Turn Text Files
    global turntext
    global dictionary
        
    readDictionaryFile()
    readTurnTxtFile()
    readWheelTxtFile()
    getPlayerInfo()
    readRoundStatusTxtFile()
    readFinalRoundTxtFile() 
    
def getWord():
    global dictionary
    roundWord = random.choice(dictionary).lower()
    global roundUnderscoreWord
    roundUnderscoreWord = []
    print(roundWord)
    for i in range(0,len(roundWord)):
        roundUnderscoreWord.append("_")

    #choose random word from dictionary
    #make a list of the word with underscores instead of letters.
    return roundWord,roundUnderscoreWord

def wofRoundSetup():
    global players
    global roundWord
    global blankWord
    roundUnderscoreWord = []

    players[0]["roundtotal"] = 0
    players[1]["roundtotal"] = 0
    players[2]["roundtotal"] = 0
    initPlayer = random.choice([0,1,2])
    print(f"The first player is player {initPlayer}")
    roundWord, blankWord =getWord()
    # Set round total for each player = 0
    # Return the starting player number (random)
    # Use getWord function to retrieve the word and the underscore word (blankWord)

    return initPlayer


def spinWheel(playerNum):
    global wheellist
    global players
    global vowels

    stillinTurn = True
    spinvalue = random.choice(wheellist)
    round
# Check for bankrupcy, and take action.
    if spinvalue == "BANKRUPT":
        players[playerNum]["roundtotal"] = 0
        stillinTurn = False
        print("You landed on 'BANKRUPT'. Your bank has been reset to $0")
# Check for loose turn
    elif spinvalue == "LOSE A TURN":
        stillinTurn = False
        print("You landed on 'LOSE A TURN'. Sorry, better luck next time.")
# Get amount from wheel if not loose turn or bankruptcy
    else:
        spinvalue.isdigit() == True
        print(f"You landed on {spinvalue}!")
# Ask user for letter guess
        letter = input("What letter would you like to guess?:")
# Use guessletter function to see if guess is in word, and return count
        goodGuess, count = guessletter(letter,playerNum)
# Change player round total if they guess right.
        if goodGuess == True:
            players[playerNum]["roundtotal"] +=  int(spinvalue)
            print(f"There are {count} {letter}s in this word. You now have {spinvalue} in your bank.")
        else:  
            print(f"There are no {letter}s in this word")
    
    return stillinTurn


def guessletter(letter, playerNum): 
    global players
    global blankWord
 
    goodGuess = False
    count = 0
# parameters:  take in a letter guess and player number
# Change position of found letter in blankWord to the letter instead of underscore 
    for i in range(0,len(roundWord)):
        if letter == roundWord[i]:
            blankWord[i] = letter
    # return goodGuess= true if it was a correct guess
            goodGuess = True

    # return count of letters in word.
            count = roundWord.count(letter)
    if goodGuess:
        print(f"You have guessed a correct letter. It is in the word {count} times!")
        print(blankWord)
    else:
        print("That letter is not in the word.")
    return goodGuess, count

def buyVowel(playerNum):
    global players
    global vowels
    
    goodGuess = False 
# Ensure player has 250 for buying a vowelcost
    if players[playerNum]['roundtotal'] < 250:
        goodGuess = False
        print("Sorry, you don't have enough money to buy a vowel")
    else:
        while True:
            guessvowel = input("What vowel would you like to purchase?: ")
    # Ensure letter is a vowel
            if guessvowel not in vowels:
                print("Sorry, that's not a vowel")
            else:
                players[playerNum]['roundtotal'] -= 250
                goodGuess = True
                break
    # Use guessLetter function to see if the letter is in the file    
        goodGuess, count = guessletter(guessvowel, playerNum)
    
    return goodGuess      
        
def guessWord(playerNum):
    global players
    global blankWord
    global roundWord
    guessword = input("Guess the word!: ")
    
    if guessword == roundWord:
        blankWord = []
        for i in range(0,len(roundWord)):
            blankWord.append(roundWord[i])
        players[playerNum]["gametotal"] += players[playerNum]["roundtotal"]
        print("Congratulations! That was the word!")
        return False
    else:
        return True
    # Take in player number
    # Ask for input of the word and check if it is the same as wordguess
    # Fill in blankList with all letters, instead of underscores if correct 
    # return False ( to indicate the turn will finish)  
    
    
def wofTurn(playerNum):  
    global roundWord
    global blankWord
    global turntext
    global players

    readRoundStatusTxtFile()
    # and Ask to (s)pin the wheel, (b)uy vowel, or G(uess) the word using
    # Keep doing all turn activity for a player until they guess wrong
    # Do all turn related activity including update roundtotal 
    
    stillinTurn = True
    while stillinTurn:
        if '_' not in blankWord:
            stillinTurn = False
            break
        choice = input("Enter 'S' to spin, 'B' to buy a vowel, or 'G' to guess the word?: ")
        if(choice.strip().upper() == "S"):
            stillinTurn = spinWheel(playerNum)
        elif(choice.strip().upper() == "B"):
            stillinTurn = buyVowel(playerNum)
        elif(choice.upper() == "G"):
            stillinTurn = guessWord(playerNum)
        else:
            ("Not a correct option")        
    # Check to see if the word is solved, and return false if it is,
    # Or otherwise break the while loop of the turn.     
    
    endofturn = "".join(blankWord)
    if endofturn == roundWord:
        return False
    else:
        return True


def wofRound():
    global players
    global roundWord
    global blankWord
    global roundstatus
    initPlayer = wofRoundSetup()
    currentplayer = initPlayer
   
    
    # Keep doing things in a round until the round is done ( word is solved)
    # While still in the round keep rotating through players
    stillinTurn = True
    while stillinTurn:
        stillinTurn = wofTurn(currentplayer)
        if stillinTurn == False: 
            break
        if currentplayer == 2:
            currentplayer = 0
        else:
            currentplayer += 1
    print(f"It's player {currentplayer}'s turn. The word is {roundUnderscoreWord}.")
    # Use the wofTurn fuction to dive into each players turn until their turn is done.
    # Print roundstatus with string.format, tell people the state of the round as you are leaving a round.
    print(roundstatus.format(status = "is now over."))
    print(players)

def wofFinalRound():
    global roundWord
    global blankWord
    global finalroundtext
    winplayer = 0
    amount = finalprize
    revealed = ['r','s','t','l','n','e']
    consonantguess = 0
    vowelguess = 0


    # Find highest gametotal player. They are playing.
    for h in players.keys():
        if players[h]["gametotal"] > players[winplayer]["gametotal"]:
            winplayer = h
    # Print out instructions for that player and who the player is.
    print(f"Welcome to the final round player {winplayer}. Now in this round \
you will have the letters R,S,T,L,N and E revealed. You have the chance \
to guess 3 consonants and 1 vowel. Once that's done, you will be \
able to try to guess the word. If you guess the word you'll win \
an additional $10,000!")
    # Use the getWord function to reset the roundWord and the blankWord ( word with the underscores)
    roundWord, blankWord = getWord()
    # Use the guessletter function to check for {'R','S','T','L','N','E'}
    for i in revealed:
        guessletter(i,winplayer)
    # Print out the current blankWord with whats in it after applying {'R','S','T','L','N','E'}
    # Gather 3 consonats and 1 vowel and use the guessletter function to see if they are in the word
    while True:
        guesses = input("Guess a letter: ")
        if guesses in vowels:
            vowelguess += 1
        else:
            consonantguess += 1
        if vowelguess == 1 and consonantguess == 3:
            break
        elif vowelguess > 1:
            vowelguess -= 1
            print("You're only allowed to guess one vowel.")
        elif consonantguess > 3:
            consonantguess -= 1
            print("You're only allowed 3 consonants.")
        else:
            guessletter(guesses,winplayer)
    # Print out the current blankWord again
    # Remember guessletter should fill in the letters with the positions in blankWord
    # Get user to guess word
    finalguess = guessWord(winplayer)
    # If they do, add finalprize and gametotal and print out that the player won 
    if finalguess == False:
         players[winplayer]["gametotal"] += amount
         print("Congratulations. You've won Wheel of Fortune!")
         print(f"({players[winplayer]['gametotal']})")

def main():
    gameSetup()    

    for i in range(0,maxrounds):
        if i in [0,1]:
            wofRound()
        else:
            wofFinalRound()

if __name__ == "__main__":
    main()
    
    
