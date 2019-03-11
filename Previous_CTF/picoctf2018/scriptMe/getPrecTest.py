#!/usr/bin/python3

import time

'''
def maxPred(equation):
    predIndexs = []
    for x, index in enumerate(equation):
        string = equation[x]
        count = predString(string)
        predIndexs.append(count)
    return predIndexs

def predString(string):
    strLen = len(string)
    count = 1
    cur = 1
    for i in range(strLen): 
        if(i < strLen -1 and string[i] == string[i+1]):
            cur += 1
        else:
            if(cur > count):
                count = cur
            cur = 1
    return count
'''

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



debug1 = "((())())"
debug2 = "(()(()))"

#take the outside +1 (xxx)
    #get rid of outer ()
    #take outside +1
    #if all are ()()() then end and +1

print(trimPrec(debug1))
print(trimPrec(debug2))
print(getPrecFromTrim(debug1))
print(getPrecFromTrim(debug2))


#print("2nd" + str(get_pred(first)))

'''
expect = "(()(((()()())()())()()))"
solved = "(((()())()())())(()(((()()())()())()())(()())(())())"


equation = "()+((())())+(())"
equation = equation.split('+')
'''

