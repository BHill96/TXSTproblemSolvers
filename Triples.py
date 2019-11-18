"""This program will find all real numbers that is the sum of A**2 + B**2 where
A and B are all real numbers between 0 and the user's choice. If a number
matches this criteria the program will add it to a dictionary with its formula.
The program will then search for a triplet of consecutive numbers and print that
set to the screen."""

realNumD = {} #This will be used just to sort the numbers in numerical order
realNumL = [] #This will store just the numbers
formula = [] #This will store the formula's for each number
sortedIndex = [] #This will store the index of the numbers once they are sorted
                 #so the program can call the correct formula and number
count = 0 #This will count the numbers in the dictionary minus one
maxNum = int(raw_input("Enter the max number: "))

#this will find A and B, calculate the number and store it in myDict
for a in range(maxNum + 1): 
    for b in range(a + 1): 
        rNum = a**2 + b**2
        realNumD[rNum] = count
        realNumL.append(rNum)
        formula.append('%s + %s' % (a, b))
        count +=1

#sorts the numbers and then stores their corresponding index in a list
for key in sorted(realNumD):
    sortedIndex.append(realNumD[key])

"""This will check for consecutive triples that meet the criteria and print them
to the screen. It takes the first three indexs and finds those numbers in
realNumL. If the three numbers are consecutive integers then it prints to the
screen."""
for i in range(count + 1):
    ip1 = i + 1
    ip2 = i + 2
    if ip2 < len(sortedIndex):
        rNum1 = realNumL[sortedIndex[i]]
        rNum2 = realNumL[sortedIndex[ip1]]
        rNum3 = realNumL[sortedIndex[ip2]]
        if rNum2 == rNum1 + 1 and rNum3 == rNum2 + 1:
            print "%s = %s" % (rNum1, formula[sortedIndex[i]])
            print "%s = %s" % (rNum2, formula[sortedIndex[ip1]])
            print "%s = %s" % (rNum3, formula[sortedIndex[ip2]])
            print " "

