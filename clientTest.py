#Noah Bledsoe, Jayson Waters, Nathan Aguirre, and Bryce Harty
#Built in a windows environment using Geany 1.33
#Language: Python 3.7.0

#importing the modules needed
import unittest
import client
import tkinter

#Creating a class to test RockPaperScissors.py
class TestRockPaperScissors(unittest.TestCase):
	
	#After executing this file and then closing the GUI, you will see 9 dots in the console; each representing a test case that passed (this is just how the unittest module works)
	#If a test fails, instead of a dot, you will see the letter "F" signifying that it failed and an error message explaing why (change some of the numbers below if you want to see that)
	#You will also see how long it took for the tests to complete and if all tests pass, an "OK" will be printed to the screen
 	
 	#This unit tests all combinations of outputs for when player one (the user) chooses Rock
 	#Date tested: April 4, 2019
 	#Engineers: Bryce Harty 
 	#Inputs: player one always chooses rock, player two chooses rock, paper, and scissors and the numbers at the end represent cases of draw (input = 0), 
 	#player one winning (input = 1), and player two winning (input = 2)
 	#Expected outputs: Test case 1 in this unit should pass since player two wins by using paper and 2 represents player two winning, 
 	#Test case 2 in this unit should pass since player one wins by choosing rock over scissors and 1 represents player one winning,
 	#Test case 3 in this unit should pass since both players choose rock and 0 represents a draw
 	#Actual outputs: 3 dots are printed to the console signifying that all 3 tests in this unit pass (both parameters are equal)
 	#Testing methodology: Equivalence classes
	def test_Rock_Paper(self):		
		self.assertEqual(client.compareResultsConsole('rock', 'paper'), 2)
	def test_Rock_Scissors(self):
		self.assertEqual(client.compareResultsConsole('rock', 'scissors'), 1)
	def test_Rock_Rock(self):
		self.assertEqual(client.compareResultsConsole('rock', 'rock'), 0)


 	#This unit tests all combinations of outputs for when player one (the user) chooses Paper
 	#Date tested: April 4, 2019
 	#Engineers: Bryce Harty 
 	#Inputs: player one always chooses paper, player two chooses rock, paper, and scissors and the numbers at the end represent cases of draw (input = 0), 
 	#player one winning (input = 1), and player two winning (input = 2)
 	#Expected outputs: Test case 1 in this unit should pass since player one wins by using paper over rock and 1 represents player one winning, 
 	#Test case 2 in this unit should pass since player two wins by choosing scissors over paper and 2 represents player two winning,
 	#Test case 3 in this unit should pass since both players choose paper and 0 represents a draw
 	#Actual outputs: 3 additional dots are printed to the console signifying that all 3 tests in this unit pass (both parameters are equal)
 	#Testing methodology: Equivalence classes
	def test_Paper_Rock(self):		
		self.assertEqual(client.compareResultsConsole('paper', 'rock'), 1)
	def test_Paper_Scissors(self):		
		self.assertEqual(client.compareResultsConsole('paper', 'scissors'), 2)
	def test_Paper_paper(self):		
		self.assertEqual(client.compareResultsConsole('paper', 'paper'), 0)
		
 	#This unit tests all combinations of outputs for when player one (the user) chooses Scissors
 	#Date tested: April 4, 2019
 	#Engineers: Bryce Harty 
 	#Inputs: player one always chooses scissors, player two chooses rock, paper, and scissors and the numbers at the end represent cases of draw (input = 0), 
 	#player one winning (input = 1), and player two winning (input = 2)
 	#Expected outputs: Test case 1 in this unit should pass since both players choose scissors and 0 represents a draw, 
 	#Test case 2 in this unit should pass since player two wins by choosing rock over scissors and 2 represents player two winning,
 	#Test case 3 in this unit should pass since player one wins by choosing scissors over paper choose rock and 1 represents player one winning
 	#Actual outputs: 3 additional dots are printed to the console signifying that all 3 tests in this unit pass (both parameters are equal)
 	#Testing methodology: Equivalence classes	
	def test_Scissors_Scissors(self):		
		self.assertEqual(client.compareResultsConsole('scissors', 'scissors'), 0)
	def test_Scissors_Rock(self):		
		self.assertEqual(client.compareResultsConsole('scissors', 'rock'), 2)
	def test_Scissors_Paper(self):		
		self.assertEqual(client.compareResultsConsole('scissors', 'paper'), 1)

#Ending the tests
if __name__ == '__main__':
    unittest.main()

    
