# Robert Massaroni
import math #"""for use of the sqrt() method"""

#""" returns average length of strings in list to the nearest integer.
 #if the lists consists of numbers, it returns the average number of digits."""
def getAverageLength(list):
    sum = 0
    for i in list:
        sum += len(i)
    return round(sum / len(list))

#"""returns the square root of number"""
def getSquareRoot(number):
   # """ check for non-negative number"""
    if number >= 0:
        return math.sqrt(number)
  #  """otherwise return error statement"""
    return "Error: Cannot return square root of negative parameter"





assert getAverageLength({"pig","cow","sheep"}) == 4, "Incorrect"
print("correct")
assert getAverageLength({"dog","cat","blue"}) == 3, "Incorrect"
print("correct")
assert getAverageLength({"12","1","12"}) == 2, "Incorrect"
print("correct")

assert getSquareRoot(4) == 2, "Incorrect"
print("correct")
assert getSquareRoot(16) == 4, "Incorrect"
print("correct")
assert getSquareRoot(-2) == "Error: Cannot return square root of negative parameter", "Incorrect"
print("correct")
