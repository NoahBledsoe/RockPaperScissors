#Noah Bledsoe, Jayson Waters, Nathan Aguirre, and Bryce Harty
#Built in a windows environment using Geany
#Language: Python 3.6.7

#importing the modules needed
import unittest
import RockPaperScissors

#creating a class to test RockPaperScissors.py
class TestRockPaperScissors(unittest.TestCase):

#This function will test compareResults to see if the expected outcomes are correct.
 	
	def test_compareResults(self):		
#		playerTwo_rock = playerTwo(0)
#		playerTwo_paper = playerTwo(1)
#		playerTwo_scissors = playerTwo(2)
		playerTwo = ['rock', 'paper', 'scissors']
		p2_rock = playerTwo[0]
		
		self.assertEqual(RockPaperScissors.compareResults('rock'), p2_rock)


if __name__ == '__main__':
    unittest.main()
    
