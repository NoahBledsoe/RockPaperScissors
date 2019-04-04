#Importing the modules necessary for the game
from random import *
from tkinter import *

#Creating functions for each option a user can choose
def userChoiceRock():
    userChoice = "rock"
    turn(userChoice)
    userImage.configure(image = rockImage)

def userChoicePaper():
    userChoice = "paper"
    turn(userChoice)
    userImage.configure(image = paperImage)

def userChoiceScissors():
    userChoice = "scissors"
    turn(userChoice)
    userImage.configure(image = scissorsImage)

#gameplay setion
def turn(userChoice):
    opponent = ['rock', 'paper', 'scissors']
    opponentChoice = opponent[randint(0,2)]

    if(opponentChoice == 'rock'):
        opponentImage.configure(image = rockImage)
    elif(opponentChoice == 'paper'):
        opponentImage.configure(image = paperImage)
    else:
        opponentImage.configure(image = scissorsImage)

    if(opponentChoice == userChoice):
        turnResult.configure(text = "It's a draw.", fg = "gray")
        compare.configure(text = "=")
    elif((opponentChoice == 'rock' and userChoice == 'scissors') or (opponentChoice == 'paper' and userChoice == 'rock') or (opponentChoice == 'scissors' and userChoice == 'paper')):
        turnResult.configure(text = "You are defeated!", fg = "red")
        compare.configure(text="<")
    else:
        turnResult.configure(text = "You win!", fg = "green")
        compare.configure(text = ">")

#main program
mainWindow = Tk()
mainWindow.title("Rock Paper Scissors")
rockButton = Button(mainWindow, width = 50, height = 10, text = "Rock", justify = CENTER, command = userChoiceRock, activebackground = 'black', activeforeground = 'white')
paperButton = Button(mainWindow, width = 50, height = 10, text = "Paper", justify = CENTER, command = userChoicePaper, activebackground = 'black', activeforeground = 'white')
scissorsButton = Button(mainWindow, width = 50, height = 10, text = "Scissors", justify = CENTER, command = userChoiceScissors, activebackground = 'black', activeforeground = 'white')

#images
rockImage = PhotoImage(file = "rockPicture.png")
paperImage = PhotoImage(file = "paperPicture.png")
scissorsImage = PhotoImage(file = "scissorsPicture.png")
#userImage = Label(image = rockImage)
#userImage.image = rockImage
compare = Label(mainWindow, justify = CENTER, font = ("Helvetica", 30) )
#opponentImage = Label(image = paperImage)
#opponentImage.image = paperImage
turnResult = Label(mainWindow, width = 20, justify = CENTER, font = ("Helvetica", 20) )
playerOne = Label(mainWindow, text = "Player One", width = 20, justify = CENTER, font = ("Helvetica", 20) )
playerTwo = Label(mainWindow, text = "Player Two", width = 20, justify = CENTER, font = ("Helvetica", 20) )

#Tk GUI grid
rockButton.grid(row = 2, column = 1)
paperButton.grid(row = 2, column = 2)
scissorsButton.grid(row = 2, column = 3)
userImage.grid(row = 3, column = 1)
compare.grid(row = 3, column = 2)
opponentImage.grid(row = 3, column = 3)
turnResult.grid(row = 4, column = 2)
playerOne.grid(row = 4, column = 1)
playerTwo.grid(row = 4, column = 3)

#mainloop
mainWindow.mainloop()
