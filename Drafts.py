# myList = [10, 25, 17, 9, 30, -5]
# # Filters the elements which are not multiples of 5
# myList2 = filter(lambda n : n%5 == 0, myList)
# print(list(myList2))


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


# def multiply(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result

# to_print = multiply(multiply(2, 3, 4))
# # to_print = multiply(args=(2, 3, 4))
# # to_print = multiply(multiply(*args=(2, 3, 4)))
# # to_print = multiply(multiply(args=[2, 3, 4]))

# print(multiply(2, 3, 4))

# print((x^2 for x in range(1, 6)))
print([x^2 for x in [1, 2, 3, 4, 5]])
print([x*2 for x in range(1, 5)])
print([x*x for x in range(1, 6)])