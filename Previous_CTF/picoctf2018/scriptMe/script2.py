#!/usr/bin/python3

from pwn import *

conn = remote('2018shell1.picoctf.com', 8672)

'''
Rules:
() + () = ()()                                      => [combine]
((())) + () = ((())())                              => [absorb-right]
() + ((())) = (()(()))                              => [absorb-left]
(())(()) + () = (())(()())                          => [combined-absorb-right]
() + (())(()) = (()())(())                          => [combined-absorb-left]
(())(()) + ((())) = ((())(())(()))                  => [absorb-combined-right]
((())) + (())(()) = ((())(())(()))                  => [absorb-combined-left]
() + (()) + ((())) = (()()) + ((())) = ((()())(())) => [left-associative]

Pseudocode:
ok I think I somewhat get this
	so () is 1, (()) is 2, and so forth
	((())()) has a precendence of 3 for example
if an expression is of equal precedence, combine: () + ()() = ()()()
							(()) + (()) = (())(())

@TODO:
	-write 
		-combineTest function
		-absorb_combine function
	-uncomment the socket and try to solve

'''

def get_pred(string):
	count = 1
	total = 1
	#convert from array to string index
	for char in range(1, len(string)):
		if string[char-1] == string[char]:
			count += 1
      	else:
      		if(count > total):
      		 	total = count
      		count = 1
	return total

#1
def combineTest(first, second):
	combineTest = True
	#mod first and second
	for x, s in enumerate(str(first)):
				if(x % 2 == 0): #even
					if(s != "("):
						combineTest = False
				if(x % 2 == 1):
					if(s != ")"):
						combineTest = False
	for x, s in enumerate(str(second)):
				if(x % 2 == 0): #even
					if(s != "("):
						combineTest = False
				if(x % 2 == 1):
					if(s != ")"):
						combineTest = False
	print(combineTest)
	#combine and return true or false
	return combineTest

#2-5
def absorb_combine(first, second, precFirst, precSecond):
	#remove outer parenthesis on smaller precidence then absorb then readd out parthensis opposite of higher
	#return string
	firstLen = len(first)
	secondLen = len(second)
	
	if(precSecond < precFirst):
		#print("precidentSecond < precidentFirst")
		#(()()()()) + ((()))
		first = first[0:len(first)-1]
		second = first + second + ")"
	elif(precSecond > precFirst):
		#print("precidentSecond > precidentFirst")
		#((()))  + (()()()())
		second = second[1:] #wrong
		second = "(" + first + second
	#precident is equal
	else:
		#print("precidentSecond = precidentFirst")
		second = first + second
	return second

#solve 1 equation
def solver(equation):
	equation = equation.split('+')
	#the array is now split
	#define the rules
	first = 0
	second = 1
	#loop over the array
	for value in range(len(equation)-1):
		#find precident of first
		#find precident of second
		precFirst = get_pred(equation[first])
		precSecond = get_pred(equation[second])

		#Determine if combined RULE 1
		combine = combineTest(equation[first], equation[second])

		absorbed = ""
		#determine absorb_combine
		if(combine == False):
			absorbed = absorb_combine(equation[first], equation[second], precFirst, precSecond)

		#determine to finally absorb or combine
		if(combine == True):
			#print("first + second")
			equation[second] = equation[first] + equation[second]
		else:
			#print("first absorbed second")
			equation[second] = absorbed

		print("debug: " + equation[second])
		first += 1
		second += 1

	lastIndex = len(equation)
	equation = str(equation[lastIndex-1])
	return equation

#DEBUG AND MAIN START BELOW

'''
actual = ( 1(()()()()()()()()()()())1 ()()()(())()())(()()()(())()())(()(()))
input = (()()()()()()()()) + ()()() + (()()()(())()()) + (()()()(())()()) + (()(()))
debug = (()()()()()()()()()()()) + (()()()(())()()) + (()()()(())()()) + (()(()))
***IF CANNOT BE COMBINED BUT HAVE EQUAL PRECEDENCE THEN USE LEN TO DETERMINE

#things with equal equivalnce are not combined for some reason
equation = "(()()()()()()()()()()()) + (()()()(())()())"
answer = "((()()()()()()()()()()())()()()(())()())(()()()(())()())(()(()))"
solved = solver(equation.replace(" ", ""))
print("input  --> " + equation)
print("answer --> " + answer)
print("solved --> " + solved)
if(answer == solved):
	print("YOU SOLVED IT GG EZ")
else:
	print("YOU FAILED, WE'LL GET THEM NEXT TIME")
'''


for testSolveRun in range(4):
	question = conn.recvline_contains('?')
	equation = question.split('=')[0]
	solved = solver(equation.replace(" ", ""))
	#TESTING
	#expected = conn.recvline_contains('=>')
	#expected = expected.split(' => ')[1]
	#TESTING
	sleep(1)
	conn.sendline(solved)
	print("								input  --> " + question)
	#print("								expected --> " + expected)
	print("								solved --> " + solved)

	#if( == solved):
		#print("YOU SOLVED IT GG EZ")
	#else:
		#print("YOU FAILED, WE'LL GET THEM NEXT TIME")

	print("++++++++++++++++++++++++++++")
	print("ITERATION COMPLETE: " + str(testSolveRun))
	print("++++++++++++++++++++++++++++")
	sleep(1)


'''
print("original: " + equation)
print("solved: " + solved)
'''
conn.interactive()