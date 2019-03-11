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

@TODO/notes:
    fails basic test case 
    (()()) + (()(())) + (()()) --> ((()()(()(())))()())
    ((((()))

'''

#def onePred(string)

def getPred(equation):
    predIndexs = []
    for x, index in enumerate(equation):
        string = equation[x]
        count = getPrecFromTrim(string)
        predIndexs.append(count)
    return predIndexs

def trimPrec(string):
    
    addString = 0
    try:
        total = string.count("(())")
        if(total > 1 and len(string) > 4):
            addString = 1
    except:
        addString = 0

    string = string.replace("()", "")

    if(addString == 1):
        string = "(" + string
    return string

def getPrecFromTrim(string):

    total = 0
    string = trimPrec(string)
    for x, index in enumerate(string):
        if(string[x] == "("):
            total += 1          

    return total
    

#2-5
def absorb_combine(first, second, precFirst, precSecond):
    #remove outer parenthesis on smaller precidence then absorb then readd out parthensis opposite of higher
    #return string
    
    print("1st:" + str(precFirst) + "2nd: " + str(precSecond))

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

def find_max(a, b):
    if(a > b):
        return a
    else:
        return b

#solve 1 equation
def solver(equation):
    equation = equation.split('+')
    #the array is now split
    #define the rules
    first = 0
    second = 1
    #loop over the array
    #predList = maxPred(equation)
    for value in range(len(equation)-1):
        #find precident of first
        #find precident of second
        precFirst = getPrecFromTrim(equation[first])
        precSecond = getPrecFromTrim(equation[second])

        absorbed = absorb_combine(equation[first], equation[second], precFirst, precSecond)

        #print(predList)
        equation[second] = absorbed
       #predList[second] = predString(equation[second])
       #predList[second] = find_max(precFirst,precSecond)

        print("debug: " + equation[second])
        first += 1
        second += 1

    lastIndex = len(equation)
    equation = str(equation[lastIndex-1])
    return equation

#DEBUG AND MAIN START BELOW


#actual = ( 1(()()()()()()()()()()())1 ()()()(())()())(()()()(())()())(()(()))
#input = (()()()()()()()()) + ()()() + (()()()(())()()) + (()()()(())()()) + (()(()))
#debug = (()()()()()()()()()()()) + (()()()(())()()) + (()()()(())()()) + (()(()))

#things with equal equivalnce are not combined for some reason


equation = "(()()) + () + (((()())()())()) + () + ((())())"
#((()()()()()()()())((()())()())())
#((()()()()()()()())((()())()())()) (()(()))
man = "(((()()()()()()()())((()())()())())(()(()))((())())()(((()()())()())()()))"
#actual (((()()()())()()()()()()()())(()()())()(()))
answer = "((()()())((()())()())()()((())()))"
kc = "((()()())((()())()())()()((())()))"

'''
solved = solver(equation.replace(" ", ""))
print("input  --> " + equation)
print("answer --> " + answer)
print("solved --> " + solved)
print("kc     --> " + kc)
if(answer == solved):
    print("                 YOU SOLVED IT GG EZ")
else:
    print("                 YOU FAILED, WE'LL GET THEM NEXT TIME")
'''


for testSolveRun in range(3):
    question = conn.recvline_contains('?')
    equation = question.split('=')[0]
    solved = solver(equation.replace(" ", ""))
    #TESTING
    #expected = conn.recvline_contains('=>')
    #expected = expected.split(' => ')[1]
    #TESTING
    sleep(1)
    conn.sendline(solved)
    print("                             input  --> " + question)
    #print("                                expected --> " + expected)
    print("                             solved --> " + solved)

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