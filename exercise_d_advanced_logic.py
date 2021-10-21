# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

ls = []
for number in numbers:
    if number % 2 == 0:
        ls.append(number)
print(ls)

# 2. Print the difference between the largest and smallest value:

largest = numbers[1]
smallest = numbers[1]

for number in numbers:
    if number > largest:
        largest = number
    elif number < smallest:
        smallest = number
print(largest - smallest)


# 3. Print True if the list contains a 2 next to a 2 somewhere.

for idx, number in enumerate(numbers):
    if number == 2 and numbers[idx-1] == 2:
        print('True')
        break

    

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22

numbers2 = [11, 6, 4, 99, 7, 11]

stopped = False
total = 0
for number in numbers:
    if number == 6:
        stopped = True
    elif number == 7:
        stopped = False
    elif stopped == False:
        total += number
    elif stopped == True:
        pass

print(total)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 


stopped = False
total = 0
for number in numbers:
    if number == 13:
        stopped = True
    elif stopped == True:
        stopped = False
    else:
        total += number

print(total)

total2 = 0
for idx, number in enumerate(numbers):
    if number == 13 or numbers[idx-1] == 13:
        pass
    else:
        total2 += number

print(total)