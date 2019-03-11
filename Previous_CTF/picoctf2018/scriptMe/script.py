#!/usr/bin/python3

'''
from pwn import *

conn = remote('2018shell1.picoctf.com', 8672)
'''

'''
() + () = ()()                                      => [combine]
((())) + () = ((())())                              => [absorb-right]
() + ((())) = (()(()))                              => [absorb-left]
(())(()) + () = (())(()())                          => [combined-absorb-right]
() + (())(()) = (()())(())                          => [combined-absorb-left]
(())(()) + ((())) = ((())(())(()))                  => [absorb-combined-right]
((())) + (())(()) = ((())(())(()))                  => [absorb-combined-left]
() + (()) + ((())) = (()()) + ((())) = ((()())(())) => [left-associative]
'''

'''
issue test cases
-same length of each len3 = len3 <-- sometimes works correctly
	-calc using some sort of precident
-one type is ()() the other is another type (((()))
- (()()) + (()()()) similar to my mod problem but encased
	- this works though  ()()() + (()())
'''

#solve 1 equation
def solver(equation):
	equation = equation.split('+')
	#the array is now split
	#define the rules
	first = 0
	second = 1
	#loop over the array
	for value in range(len(equation)-1):
		#if length of left is greater than right
		if(len(equation[first]) > len(equation[second])):
			print("~~~~~~~~~~~")
			print("left > right")
			print("1st operand: " + equation[first] + "  2nd operand: " + equation[second] + "\n~~~~~~~~~~~")
			#morph together-two morphs exist depending on operand length
			type1 = "base1"
			type2 = "base2"
			strip_equation1 = equation[first][1:len(equation[first])-1]
			strip_equation2 = equation[second][1:len(equation[second])-1]
			strip1 = "base3"
			strip2 = "base4"
			for x, s in enumerate(str(strip_equation1)):
				if(x % 2 == 0): #even
					if(s != "("):
						strip1 = "bad"
				if(x % 2 == 1):
					if(s != ")"):
						strip1 = "bad"
			for x, s in enumerate(str(strip_equation2)):
				if(x % 2 == 0): #even
					if(s != "("):
						strip2 = "bad"
				if(x % 2 == 1):
					if(s != ")"):
						strip2 = "bad"
			for x, s in enumerate(str(equation[first])):
				if(x % 2 == 0): #even
					if(s != "("):
						type1 = "bad"
				if(x % 2 == 1):
					if(s != ")"):
						type1 = "bad"
			for x, s in enumerate(str(equation[second])):
				if(x % 2 == 0): #even
					if(s != "("):
						type2 = "bad"
				if(x % 2 == 1):
					if(s != ")"):
						type2 = "bad"
			print(type1 + type2 + strip1 + strip2)
			if(type1 == "base1" and type2 == "base2"):
				print("case1.1")
				equation[second] = equation[first] + equation[second]
			elif(not(strip1 == "base3") and strip2 == "base4"):
				print("case2.2") #stripped right side so that ()() is true
				equation[first] = equation[second][1:]
				equation[second] = "(" + equation[first] + equation[second]
			elif(strip1 == "base3" and not(strip2 == "base4")):
				print("case3.2") #stripped left side so that ()() is true
				equation[first] = equation[first][0:len(equation[first])-1]
				equation[second] = equation[first] + equation[second] + ")"
			else:
				print("case3.1")
				equation[first] = equation[first][0:len(equation[first])-1] #right
				equation[second] = equation[first] + equation[second] + ")"

		 
		if(len(equation[first]) == len(equation[second])):
			print("~~~~~~~~~~~")
			print("left = right")
			print("1st operand: " + equation[first] + "  2nd operand: " + equation[second] + "\n~~~~~~~~~~~")
			#morph
			type1 = "base1"
			type2 = "base2"
			strip_equation1 = equation[first][1:len(equation[first])-1]
			strip_equation2 = equation[second][1:len(equation[second])-1]
			strip1 = "base3"
			strip2 = "base4"
			for x, s in enumerate(str(strip_equation1)):
				if(x % 2 == 0): #even
					if(s != "("):
						strip1 = "bad"
				if(x % 2 == 1):
					if(s != ")"):
						strip1 = "bad"
			for x, s in enumerate(str(strip_equation2)):
				if(x % 2 == 0): #even
					if(s != "("):
						strip2 = "bad"
				if(x % 2 == 1):
					if(s != ")"):
						strip2 = "bad"
			for x, s in enumerate(str(equation[first])):
				if(x % 2 == 0): #even
					if(s != "("):
						type1 = "bad"
				if(x % 2 == 1):
					if(s != ")"):
						type1 = "bad"
			for x, s in enumerate(str(equation[second])):
				if(x % 2 == 0): #even
					if(s != "("):
						type2 = "bad"
				if(x % 2 == 1):
					if(s != ")"):
						type2 = "bad"
			print(type1 + type2 + strip1 + strip2)
			if(type1 == "base1" and type2 == "base2"):
				print("case1.2") #
				equation[second] = equation[first] + equation[second]
			elif(not(strip1 == "base3") and strip2 == "base4"):
				print("case2.2") #stripped right side so that ()() is true
				equation[first] = equation[second][1:]
				equation[second] = "(" + equation[first] + equation[second]
			elif(strip1 == "base3" and not(strip2 == "base4")):
				print("case3.2") #stripped left side so that ()() is true
				equation[first] = equation[first][0:len(equation[first])-1]
				equation[second] = equation[first] + equation[second] + ")"
			else:
				print("case4.2")
				equation[second] = equation[first] + equation[second]

		#if length of right is greater than left
		else:
			print("~~~~~~~~~~~")
			print("left < right")
			print("1st operand: " + equation[first] + "  2nd operand: " + equation[second] + "\n~~~~~~~~~~~")
			#morph together-two morphs exist depending on operand length
			#if operand length is greater than two
			type1 = "base1"
			type2 = "base2"
			strip_equation1 = equation[first][1:len(equation[first])-1]
			strip_equation2 = equation[second][1:len(equation[second])-1]
			strip1 = "base3"
			strip2 = "base4"
			for x, s in enumerate(str(strip_equation1)):
				if(x % 2 == 0): #even
					if(s != "("):
						strip1 = "bad"
				if(x % 2 == 1):
					if(s != ")"):
						strip1 = "bad"
			for x, s in enumerate(str(strip_equation2)):
				if(x % 2 == 0): #even
					if(s != "("):
						strip2 = "bad"
				if(x % 2 == 1):
					if(s != ")"):
						strip2 = "bad"
			for x, s in enumerate(str(equation[first])):
				if(x % 2 == 0): #even
					if(s != "("):
						type1 = "bad"
				if(x % 2 == 1):
					if(s != ")"):
						type1 = "bad"
			for x, s in enumerate(str(equation[second])):
				if(x % 2 == 0): #even
					if(s != "("):
						type2 = "bad"
				if(x % 2 == 1):
					if(s != ")"):
						type2 = "bad"
			print(type1 + type2 + strip1 + strip2)
			if(type1 == "base1" and type2 == "base2"):
				print("case1.3") #right?
				equation[second] = equation[first] + equation[second]
			elif(not(strip1 == "base3") and strip2 == "base4"):
				print("case2.2") #stripped right side so that ()() is true
				equation[first] = equation[second][1:]
				equation[second] = "(" + equation[first] + equation[second]
			elif(strip1 == "base3" and not(strip2 == "base4")):
				print("case3.2") #stripped left side so that ()() is true
				equation[first] = equation[first][0:len(equation[first])-1]
				equation[second] = equation[first] + equation[second] + ")"
			else:
				print("case3.3")
				equation[second] = equation[second][1:] #wrong
				equation[second] = "(" + equation[first] + equation[second]
		first += 1
		second += 1
	
	lastIndex = len(equation)
	equation = str(equation[lastIndex-1])
	return equation

x = "(())+()()"
y = "(((())))+(())"
z= "(())(())+()()"
print(solver(x))
print(solver(y))
print(solver(z))

'''
for testSolveRun in range(1):
	question = conn.recvline_contains('?')
	equation = question.split('=')[0]
	solved = solver(equation.replace(" ", ""))
	sleep(1)
	conn.sendline(solved)
	print("++++++++++++++++++++++++++++")
	print("ITERATION COMPLETE: " + str(testSolveRun))
	print("++++++++++++++++++++++++++++")
	sleep(1)

print("original: " + equation)
print("solved: " + solved)
conn.interactive()
'''