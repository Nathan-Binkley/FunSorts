#Fun Sorts.py
#Idea is to take a bunch of funny sorts found on r/programmerhumor and make them real


import random, time

def check(nums:list) -> bool:

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

# O(1) Optimization Sort: Delete the whole list, an empty list is sorted list.
#
def optimization(nums:list) -> list:
    newList = nums[:] #if just normal list = list, memory values are the same
                # ^^^ allows splicing from beginning to end
    newList.clear()
    return newList

# O(-1) Sort: Fuck off, I'm not sorting your list.
#
def no_sort(nums:list) -> list:
    return nums

# StalinSort: You iterate down the list of elements checking if they're in order. An element which is out of order is eliminated. At the end you have a sorted list.
#
def stalin_sort(nums:list) -> list:
    newList = nums[:]
    nextList = []
    while(not check(newList)):
        for i in range(len(newList)-1):
            if newList[i] > newList[i+1]:
                newList[i] = None
        #print(nextList) #debugging
        nextList = []
        for i in newList:
            if i != None:
                nextList.append(i)
        #print(nextList) #debugging
        newList = nextList[:]
    print("end of loop")
    return nextList

# GenghisKhanSort: delete all elements except for the first, repopulate the list with successors of the first element.
#

def genghis_khan_sort(nums:list) -> list:
    newList = nums[:1]
    number = 0
    for i in range(99):
        newList.append(newList[-1]+1)
    return newList

# HitlerSort: pick the value that you like, declare it as the highest, and then delete all other values.
#
def hitler_sort(nums:list) -> list:
    newList = nums[:]
    favorite = newList[random.randint(0, len(newList))]
    for i in range(len(newList)):
        if newList[i] != favorite:
            newList[i] = None
    while i < len(newList):
        if newList[i] == None:
            del newList[i]
            i-=1
        else:
            i+=1
    nextList = []
    for i in newList:
        if i != None:
            nextList.append(i)
    return nextList

# AmishSort: Turn off computer, then you won't even need sorting.
#
def AmishSort(nums:list) -> list:
    print("Why are you here? We're Amish. We don't use computers")
    print("Well now we're gonna sort anyway")
    print("Sorting")
    for i in range(5):
        print(".")
        time.sleep(1)

# Communist Sort: Wait for the list to sort itself. Act upset when it doesn't happen until a tyrannical dictatorship shows up and forces the list into sorted order.
#

# Capitalist Sort: The first 3 elements in the list remain in their position, every iteration through they subtract 1 from all of the other elements and add it to themselves, until the rest of the list is destroyed and they are the only ones left.
#
def capitalist(nums:list) -> list:
    newList = nums[:]
    first = newList[0]
    second = newList[1]
    third = newList[2]
    done = False
    while (not done):
        for i in range(len(newList)):
            if i <= 2:
                pass
            elif newList[i] == 0:
                newList[i] = None
            else:
                newList[i] -= 1
                if i % 3 == 0:
                    first += 1
                elif i % 3 == 1:
                    second += 1
                elif i% 3 == 2:
                    third += 1
        nextList = []
        for i in newList:
            if i != None:
                nextList.append(i)
        newList = nextList[:]
        newList[0] = first
        newList[1] = second
        newList[2] = third
        if len(newList) <= 3:
            return newList


# Thanos Sort: Randomly delete half the elements in the list over and over until the list happens to be sorted.
#

# TrumpSort O(0): the array is always sorted. Anyone who says otherwise is fake news.
#

# LiberalSort: each element is declared to be out of order for moral reasons and committing moral crimes, elements have 1 subtracted from them at semi-random. The sort never actually ends as the narrative needs to keep going to maintain political power.
#

# Republic Sort: Look at the first 5 elements. Choose the highest one no matter how much lower that is than other elements in the list past that. Declare that the new top value, the list never gets sorted because it would upset the newly declared top element.
#


init = []
for i in range(100):
    f = random.randint(0,100)
    init.append(f)
print("Basic list: " + str(init))

# O(1) Optimization Sort: Delete the whole list, an empty list is sorted list.
#
print("Optimization Sort:")
best = optimization(init)
print("This is the outcome of Optimization sort: " + str(best))
print()
print()

# O(-1) Sort: Fuck off, I'm not sorting your list.
#
print("No sort: ")
best = no_sort(init)
print("This is the outcome of no sorting: " + str(best))
print()
print()

# StalinSort: You iterate down the list of elements checking if they're in order. An element which is out of order is eliminated. At the end you have a sorted list.
#
print("Stalin Sort: ")
best = stalin_sort(init)
print("This is the outcome of stalin sort: " + str(best))
print()
print()


# GenghisKhanSort: delete all elements except for the first, repopulate the list with successors of the first element.
#
print("Genghis Khan Sort: ")
best = genghis_khan_sort(init)
print("This is the outcome of Genghis Khan sort: " + str(best))
print("Way to go Genghis")
print()
print()

# HitlerSort: pick the value that you like, declare it as the highest, and then delete all other values.
#
print("Hitler Sort: ")
best = hitler_sort(init)
print("This is the outcome of Hitler Sort: " + str(best))
print()
print()

# AmishSort: Turn off computer, then you won't even need sorting.
#
print("Amish Sort: ")
best = AmishSort(init)
print("Amish sort doesn't sort. It just turns off your PC (if it actually worked the way I wanted it to).")
print("Here's the outcome: " + str(best))
print()
print()

# Communist Sort: Wait for the list to sort itself. Act upset when it doesn't happen until a tyrannical dictatorship shows up and forces the list into sorted order.
#

# Capitalist Sort: The first 3 elements in the list remain in their position, every iteration through they subtract 1 from all of the other elements and add it to themselves, until the rest of the list is destroyed and they are the only ones left.
#
print("Capitalist Sort: ")
best = capitalist(init)
print("This is the outcome of capitalist sort: " + str(best))
print()
print()
# Thanos Sort: Randomly delete half the elements in the list over and over until the list happens to be sorted.
#

# TrumpSort O(0): the array is always sorted. Anyone who says otherwise is fake news.
#

# LiberalSort: each element is declared to be out of order for moral reasons and committing moral crimes, elements have 1 subtracted from them at semi-random. The sort never actually ends as the narrative needs to keep going to maintain political power.
#

# Republic Sort: Look at the first 5 elements. Choose the highest one no matter how much lower that is than other elements in the list past that. Declare that the new top value, the list never gets sorted because it would upset the newly declared top element.
#
