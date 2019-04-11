#Noah Bledsoe, Jayson Waters, Nathan Aguirre, and Bryce Harty
#Built in a windows environment using Geany
#Language: Python 3.6.7

#importing the modules needed
import unittest
import RockPaperScissors
import tkinter

#creating a class to test RockPaperScissors.py
class TestRockPaperScissors(unittest.TestCase):

#This function will test compareResults to see if the expected outcomes are correct.
 	#########IMPORTANT###########
		#When you run this, the dots before the test represent each test
		#If it is a "." that case passed
		#If it is a "F" that case failed
		#It also give the number of cases and if all cases pass it will give an "OK"
		#If a case fails or all of them it will say "Failure" and give which cases that were wrong. 
 	
 	#This are all three tests with Rock being playerOnesChoice
	def test_Rock_Paper(self):		
		self.assertEqual(RockPaperScissors.compareResultsConsole('rock', 'paper'), 2)
	def test_Rock_Scissors(self):
		self.assertEqual(RockPaperScissors.compareResultsConsole('rock', 'scissors'), 1)
	def test_Rock_Rock(self):
		self.assertEqual(RockPaperScissors.compareResultsConsole('rock', 'rock'), 0)


 	#This are all three tests with Paper being playerOnesChoice
	def test_Paper_Rock(self):		
		self.assertEqual(RockPaperScissors.compareResultsConsole('paper', 'rock'), 1)
	def test_Paper_Scissors(self):		
		self.assertEqual(RockPaperScissors.compareResultsConsole('paper', 'scissors'), 2)
	def test_Paper_paper(self):		
		self.assertEqual(RockPaperScissors.compareResultsConsole('paper', 'paper'), 0)
		
 	#This are all three tests with scissors being playerOnesChoice		
	def test_Scissors_Scissors(self):		
		self.assertEqual(RockPaperScissors.compareResultsConsole('scissors', 'scissors'), 0)
	def test_Scissors_Rock(self):		
		self.assertEqual(RockPaperScissors.compareResultsConsole('scissors', 'rock'), 2)
	def test_Scissors_Paper(self):		
		self.assertEqual(RockPaperScissors.compareResultsConsole('scissors', 'paper'), 1)


if __name__ == '__main__':
    unittest.main()
    
