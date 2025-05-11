#CONDITIONALS: IF STATEMENTS

#SYNTAX (STRUCTURE OF LOGIC)
# IF CONDITION
#       <indented block of code>

#secret_number = 55
#user_number = int(input('Guess a number'))

#if user_number == secret_number:
#    print('Congrats, you won!')

#elif user_number == 7:
#    print("Oh, that's my fav number") 

#else:
#    print('Sorry, not the same number')


#Esersize:
user_number = int(input('Enter a nubber from 1 to 100 => '))

# if user_number%3 + user_number%5 == 0:
if user_number%3 == 0 and user_number%5 == 0:
    print('FizzBuzz')
elif user_number%3 == 0:
    print('Fizz')
elif user_number%5 == 0:
    print('Buzz')

