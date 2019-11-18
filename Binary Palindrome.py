"""This program is going to check for all the numbers between the start number and the end number where the
binary form is a  palindrome and where that number squared is also a palindrome and print that number to the
screen if it is true."""

import time
startTime = time.clock()
start = raw_input("Start: ")
end = raw_input("End: ")

#makes them integers
start = int(start)
end = int(end)

#this will run as long as the start number is less than or equal to the end number
while start <= end:
    binStart = bin(start) #converts start number into binary number
    binStart = str(binStart) #converts binary number into string
    binStart = binStart[2:] #removes '0b' from start of binary number
    flipBinStart = binStart[::-1] #flips the binary number

    if binStart == flipBinStart: #checks if binary number is same forwards and backwards
        start2 = start ** 2 #squares start
        binStart2 = bin(start2) #converts squared start to binary number
        binStart2 = str(binStart2) #converts binary number to string
        binStart2 = binStart2[2:] #removes '0b' from start of binary number
        flipBinStart2 = binStart2[::-1] #reverses binary number

        if binStart2 == flipBinStart2: #checks if binary number is same forwards and backwards
            print "Number: " + str(start)
            print binStart
            print flipBinStart
            print "Square: " + str(start2)
            print binStart2
            print flipBinStart2
            print " "
            start += 1
        else: #squared binaries don't match
            start += 1
            
    else: #binaries don't match
        start +=1

endTime = time.clock()
print "Done"
print endTime - startTime
