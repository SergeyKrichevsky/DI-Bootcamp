myList = [10, 25, 17, 9, 30, -5]
# Filters the elements which are not multiples of 5
myList2 = filter(lambda n : n%5 == 0, myList)
print(list(myList2))


# The code is longer!

# def multipleOf5(n):
#   if(n % 5 == 0):
#     return n

# myList = [10, 25, 17, 9, 30, -5]

# myList2 = filter(multipleOf5, myList)
# print(myList2)


# def multipleOf5(n):
#     if n % 5 == 0:
#         return True  # лучше явно вернуть логическое значение

# myList = [10, 25, 17, 9, 30, -5]
# myList2 = filter(multipleOf5, myList)

# print(list(myList2))  # обязательно оберни в list()!
