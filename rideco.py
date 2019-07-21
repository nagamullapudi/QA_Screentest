"""
RideCO QA Screener Test

Program = testme.exe
Coding Platform = python
Experience level = beginner
Test runner used = unittest

Code:
- Had the choice of using os.system or subprocess to run the program
- subprocess was chosen run the program because it was easier to pass in arguments and capture output
- Wrote convenience methods for each different type of test scenerios
- Create UnitTest class and check the result of the above mentioned scenarios using assertions.
- Frameworks used:
	- unittest
	- subprocess
	- random
- String Comparison

Level of Difficulty of the program:
- From the concept point of view it is rather easier
- From my level of knowledge in windows and python coding perspective, it is on a harder scale.

Challenges:
- Learn Python Scripting as I am very new at it
- calling an executable from python
- Capturing output from the executable

Takeaways
- Python programming
- Windows automation
- Opened my mind to new areas as I was very narrowed down to mobile testing
  and manual testing to the most extent in my professional career.

References used: 
- Stackoverflow: obviously no coder goes without using this.
- This fine tutorial explaining the unittesting in python
	- https://realpython.com/python-testing/#automated-vs-manual-testing
"""

import subprocess
import random
import unittest

#Please note the script and testme program should be in the same folder
prg = 'testme' 

#CALLING PRG WITH AN ARGUMENT
def callPrg(anInt):
	#takes in an int and return an array of bytes
	result = subprocess.Popen([prg, str(anInt)], stdout=subprocess.PIPE).communicate()[0]
	strResult = result.decode("utf-8")
	print (strResult)
	return strResult;

#CALLING PRG WITHOUT AN ARGUMENT
def callPrgNoArgs():
	#takes in an int and return an array of bytes
	result = subprocess.Popen((prg), stdout=subprocess.PIPE).communicate()[0]
	strResult = result.decode("utf-8")
	print (strResult)
	return strResult;

#RETURN AN ALPHANUMERIC CHARACTER
def getAlpaNumberic():
	return "a10";

#STRING COMPARISON
def isEqual(str1, str2):
	if str1 == str2:
		return 1
	else:
		return 0

#CONVENIENCE METHODS FOR TESTME CALLS
"""
This method checks for consistency.
Passes in same arguemnt twice and checks their output
True if both are same otherwise false
"""		
def forConsistency():
	one = random.randint(2,99)
	oneOutput = callPrg(one)
	twoOutput = callPrg(one)
	comparsion = isEqual(oneOutput, twoOutput)
	if comparsion == 1:
		print ("testme is consistent for: " + str(one))
		return True;
	else:
		print ("testme is not consistent for: " +  str(one) + "This is a serious bug")
		return False;
   
"""
This method checks for uniqueness.
Passes in two different arguemnts and checks their output
True if both are different otherwise false
"""	
def forUniqueness():
	one = random.randint(2,99)
	two = 100
	oneOutput = callPrg(one)
	twoOutput = callPrg(two)
	comparsion = isEqual(oneOutput, twoOutput)
	if comparsion == 1:
		print ("testme is not unique for: " + str(one) + " & " + str(100))
		return False
	else:
		print ("testme is unique")
		return True

"""
This method checks for consistency of the app with 1.
Passes in 1 twice and checks their output
True if both are same otherwise false

we already know that there is a bug with this. so ya.
"""	
def withOne():
	oneOutput1 = callPrg(1)
	oneOutput2 = callPrg(1)
	comparsion = isEqual(oneOutput1, oneOutput2)
	if comparsion == 1:
		print ("testme is consistent: 1") 
		return True;
	else:
		print ("testme is not consistent for: 1. This is a serious bug")	
		return False;

"""
This method checks for output with no arguments passed.
True if output length = 0 otherwise false
"""	
def noArgs():
	oneOutput1 = callPrgNoArgs()
	if len(oneOutput1) == 0:
		return True;
	else:
		return False;

"""
This method checks for output when an alphanumeric value is given.
Passes in an alphanumeric value and checks their output
True if output length == 0 otherwise false
"""	
def withAlphaNumberic():
	number = getAlpaNumberic()
	output = callPrg(number)
	if len(output) == 0:
		return True;
	else:
		return False;
   
   
"""
unittest framework is used as a TestRunner. This is built-in so I chose to go with this.
nose or pytest need separate installation.
"""
class TestRideCo(unittest.TestCase):

	def test_withOne(self):
		self.assertEqual(withOne(), True, "Testme fails when passed in an argument of 1")
		
	def test_noArgs(self):
		self.assertEqual(noArgs(), True, "Should be True")
		
	def test_forConsistency(self):
		self.assertEqual(forConsistency(), True, "Testme should be consistent")
		
	def test_forUniqueness(self):
		self.assertEqual(forUniqueness(), True, "Testme should be unique")
		
	def test_withAlphaNumberic(self):
		self.assertEqual(withAlphaNumberic(), True, "Testme should not work for alphanumeric")

if __name__ == '__main__':
    unittest.main()