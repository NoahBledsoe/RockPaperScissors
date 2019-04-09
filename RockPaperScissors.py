#Noah Bledsoe, Jayson Waters, Nathan Aguirre, and Bryce Harty
#Built in a windows environment using Geany
#Language: Python 3.6.7
#As of right now, the game is only between the player and the computer but the client-server functionalities should be ready by the next phase
#For unit testing, we are using the built in 'unittest' module that comes with python




#These are the needed moduels that we imported
from tkinter import *
from random import *
import unittest

#Creating the window for the game
window = Tk()
window.title("Rock Paper Scissors")
window.geometry("1600x500")


#Creating functions for when the user hits either the Rock, Paper, or Scissors buttons to call the compare function to see who won
#These functions also configure the image for whatever button they press
def playerChoosesRock():
	playerOneChoice = "rock"
	compareResults(playerOneChoice)
	playerOneImage.configure(image = rockImage)

def playerChoosesPaper():
	playerOneChoice = "paper"
	compareResults(playerOneChoice)
	playerOneImage.configure(image = paperImage)

def playerChoosesScissors():
	playerOneChoice = "scissors"
	compareResults(playerOneChoice)
	playerOneImage.configure(image = scissorsImage)
	
#Creating the buttons that the user presses and activating each function that corresponds with it      
rockButton = Button(window, width = 50, height = 5, font = ("Times New Roman", 15), text = "Rock", justify = CENTER, command = playerChoosesRock, bg = 'green', activebackground = 'gray', activeforeground = 'white')
paperButton = Button(window, width = 50, height = 5, font = ("Times New Roman", 15), text = "Paper", justify = CENTER, command = playerChoosesPaper, bg = 'green', activebackground = 'gray', activeforeground = 'white')
scissorsButton = Button(window, width = 50, height = 5, font = ("Times New Roman", 15), text = "Scissors", justify = CENTER, command = playerChoosesScissors, bg = 'green', activebackground = 'gray', activeforeground = 'white')

#Setting the images and label used in the GUI and placing them in the grid correctly
rockImage = PhotoImage(file = "rockPicture.png")
rockButton.grid(row = 2, column = 1)
paperImage = PhotoImage(file = "paperPicture.png")
paperButton.grid(row = 2, column = 2)
scissorsImage = PhotoImage(file = "scissorsPicture.png")
scissorsButton.grid(row = 2, column = 3)
playerOneImage = Label(image = rockImage)
playerOneImage.image = rockImage
playerOneImage.grid(row = 3, column = 1)
playerTwoImage = Label(image = paperImage)
playerTwoImage.image = paperImage
playerTwoImage.grid(row = 3, column = 3)
turnResult = Label(window, width = 20, justify = CENTER, font = ("Times New Roman", 20))
turnResult.grid(row = 3, column = 2)
playerOne = Label(window, text = "Player One", width = 20, justify = CENTER, font = ("Times New Roman", 20))
playerOne.grid(row = 4, column = 1)
playerTwo = Label(window, text = "Player Two", width = 20, justify = CENTER, font = ("Times New Roman", 20))
playerTwo.grid(row = 4, column = 3)
	
	
#Function to compare both the player's choice and the computer's random choice to see who won 
def compareResults(playerOneChoice):
	playerTwo = ['rock', 'paper', 'scissors']
	playerTwoChoice = playerTwo[randint(0,2)]

	if(playerTwoChoice == 'rock'):
		playerTwoImage.configure(image = rockImage)
	elif(playerTwoChoice == 'paper'):
		playerTwoImage.configure(image = paperImage)
	else:
		playerTwoImage.configure(image = scissorsImage)

	if(playerTwoChoice == playerOneChoice):
		turnResult.configure(text = "It's a draw.", fg = "black")
	elif((playerTwoChoice == 'rock' and playerOneChoice == 'scissors') or (playerTwoChoice == 'paper' and playerOneChoice == 'rock') or (playerTwoChoice == 'scissors' and playerOneChoice == 'paper')):
		turnResult.configure(text = "Player Two has won.", fg = "red")
	else:
		turnResult.configure(text = "Player One has won.", fg = "green")

#Closing the process
window.mainloop()
