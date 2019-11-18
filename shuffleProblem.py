import copy
import csv
import time

# Inserts every number between 1 and maxNumber into myList in reverse order
# i.e. 5, 4, 3, 2, 1
def populateList(myList, maxNumber):
    for number in range(1, maxNumber + 1):
        myList.append(number)

# Removes every other number and appends it to the bottom starting with the first number.
# This does not resemble the actual shuffling algorithm in the problem, but it gets the same result.
# I love this function because I found it by accident.     
def shuffle(deck):
    for index in range(0, len(deck)):
        temp = deck.pop(index)
        deck.append(temp)
    # The list is backwards, so we reverse it
    deck.reverse()  
    
def trackNumber(trackedNumber, shuffledDeck1, shuffledDeck2 = [], shuffledDeck3 = []):
    result = []
    
    # if 
    for index in range(0, len(shuffledDeck1)):
        if shuffledDeck1[index] == trackedNumber:
            result.append(index + 1)
    
    if (shuffledDeck2):
        for index in range(0, len(shuffledDeck2)):
            if shuffledDeck2[index] == trackedNumber:
                result.append(index + 1)
    else:
        return result[0]
                
    if (shuffledDeck3):
        for index in range(0, len(shuffledDeck3)):
            if shuffledDeck3[index] == trackedNumber:
                result.append(index + 1)
    else:
        return "({}, {})".format(result[0], result[1])
        
    return "({}, {}, {})".format(result[0], result[1], result[2])
            
def binaryForm(number):
    return str(bin(number))[2:]
    
def partC(size):
    deck = []
    populateList(deck, size)
    
    for num in range(0,3):
        shuffle(deck)
        
    print(deck[0])
    
def partD(size):
    deck = []
    result = []
    # Populate the deck
    populateList(deck, size)
    
    # Shuffle the deck 'size' number of times
    for num in range(1, size + 1):
        shuffle(deck)
        # Store the number at the top of the deck after each shuffle
        result.append(trackNumber(1, deck))
        
    # If the number at the top of the deck is 1, check if it's a one cycle
    if deck[0] == 1:
        result.sort()
        
        # Check if each number from 1 to size is in result
        # If true, size is an answer for part D
        # If false, size is not an answer for partD
        for index in range(0, size):
            if result[index] != (index + 1):
                return False
        return True
    else:
        return False             
   
def writeToCSV(n):
    startTime = time.clock() 
        
    with open('/Users/blakehillier/programs/miscPython/shuffleData.csv','wb') as shuffleFile: #finds csv file 'shuffleData'
        shuffleWriter = csv.writer(shuffleFile) #creates writing object to write to drinkData, delimiter defaulted to ','
        shuffleWriter.writerow(('Size of Deck (n)', 'Binary form of n', 'Part A', 'Part B', 'Part C', 'Part D', 'Cycle of 1 after 3 Shuffles', 'Deck after 1 Shuffle', 'Deck after 2 Shuffles', 'Deck after 3 Shuffles'))
    
        for num in range(1, n + 1):
            deckA = []
            populateList(deckA, num)
            shuffle(deckA)
            
            deckB = copy.deepcopy(deckA)
            shuffle(deckB)
    
            deckC = copy.deepcopy(deckB)
            shuffle(deckC)
        
            cycle = trackNumber(1, deckA, deckB, deckC)
    
            shuffleWriter.writerow((num, binaryForm(num), deckA[0], deckB[0], deckC[0], partD(num), cycle, deckA, deckB, deckC))
        
        shuffleFile.close()
        
    endTime = time.clock()
    print "Done"
    print endTime - startTime