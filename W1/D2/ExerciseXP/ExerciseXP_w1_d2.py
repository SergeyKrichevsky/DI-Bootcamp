#EX1

my_fav_numbers = {1, 23, 12, 1981}
print(f'my fav numbers Set:', my_fav_numbers)
my_fav_numbers.update([42,40])
print(f'My updatet num st:', my_fav_numbers)
my_fav_numbers.remove(40)
# Aditional way - will not return an error if 40 is not present in the set:
# my_fav_numbers.discard(40)
print(f'my new set without number 40: "', my_fav_numbers)

friend_fav_numbers = set()
friend_fav_numbers.update([1,2,3,4,5])
print(f'friend_fav_numbers set: ', friend_fav_numbers)

our_fav_numbers = my_fav_numbers|friend_fav_numbers
# different way:
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(f'our_fav_numbers: ', our_fav_numbers)


#EX2

given_tuple_of_integers = tuple(our_fav_numbers)
print(f'Given tuple of integers is: ', given_tuple_of_integers)

temp_list = list(given_tuple_of_integers)
temp_list.extend([100, 200, 300])
given_tuple_of_integers = tuple(temp_list)
print(f'Updated Given tuple of integers : ', given_tuple_of_integers)


#EX3

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
print(f'Given list of items in the basket: ', basket)

basket.remove('Banana')
print(f'We ate the banana. This is what left: ', basket)

basket.remove('Blueberries')
print(f'We ate the Blueberries. This is what left: ', basket)

basket.append('Kiwi')
print(f'We added Kiwi. This is what we have now in the basket: ', basket)

basket.insert(0, 'Apples')
print(f'We added Apples. This is what we have now in the basket: ', basket)
print(f'Pay attention: we have', basket.count('Apples'), 'portions os Apples in the basket right now')

basket.clear()
print(f"Sorry, you`re to late. We are out of food. The basket is empty :", basket)
print('We hope to see you next time!')


#EX4

list_ex4 = []
x = 1.5
while x <= 5:
    list_ex4.append(x)
    x += 0.5

#list_ex4 =[x/2 for x in range(3, 11)]

print(list_ex4)


#EX5


for i in range(1, 21):
     print(i)

numbers_list = list(range(1, 20))

# works if there are no multiple similar elements:

# for i in numbers_list:
#     if numbers_list.index(i) % 2 == 0:
#         print(i)

# for index, value in enumerate(numbers_list):
#      if index % 2 == 0:
#           print(value)

for a, b in enumerate(numbers_list):
     if a % 2 == 0:
          print(b)


#EX6

my_name = 'Sergey'
user_input = input('What is your name? ')

while user_input.lower() != my_name.lower():
     user_input = input('What is your name? ')

print("Hello, Sergey! I was waiting for you!")


#EX7

users_favotite_fruits_list = []
user_input = input('What are your favorite fruits? (input several fruits, separated by spaces)')
users_favotite_fruits_list = user_input.split()

sole_fruit = input('Name any fruit ')

if sole_fruit in users_favotite_fruits_list:
     print('You chose one of your favorite fruits! Enjoy!')
else:
     print('You chose a new fruit. I hope you enjoy it!')
      

#EX8

pizza_price = 10
topping_price =2.5
list_of_toppings_ordered = []

user_input = input('What topping do you want to Add? (Write "quit" to finish)')

if user_input.lower() != 'quit':
     list_of_toppings_ordered.append(user_input)

while user_input.lower() != 'quit':
     user_input = input('What topping do you want to Add? (Write "quit" to finish)')
     if user_input.lower() == 'quit':
          break
     list_of_toppings_ordered.append(user_input)

final_price = pizza_price + len(list_of_toppings_ordered) * topping_price

print()
print('Great! Here is the list of toppings you ordered:')
print()
for topping in list_of_toppings_ordered:
     print(f'- {topping}')

print()
print(f'Total Price: $ {final_price:.2f}')
print()


#EX9

list_of_watchers = []

def get_valid_age(prompt):
     while True:
          age_input = input(prompt)
          try:
               return int(age_input)
          except ValueError:
               print('Please enter a valid number.')

age = get_valid_age("What is your age? ")
list_of_watchers.append(age)

user_input = input('Do you want additional ticket to someone else (Y or N)? ')
while user_input.lower() != 'n':
     age = get_valid_age('What is his/her age? ')
     list_of_watchers.append(age)
     user_input = input('Anyone else (Y or N)? ')
     if user_input == "N".lower:
          break

infant_ticket_price = 0
child_ticket_price = 10
adult_ticket_price = 15

total_tickets_price = 0

for i in list_of_watchers:
     if i <= 3:
          total_tickets_price += infant_ticket_price
     elif i <= 12:
          total_tickets_price += child_ticket_price
     else:
          total_tickets_price += adult_ticket_price

print(f'Total Cost is: $ {total_tickets_price:.2f}')


#EX9 #2

attendees = []

def get_valid_age(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

name = input("What is your name? ")
age = get_valid_age("What is your age? ")

attendees.append({"name": name, "age": age})

while input("Anyone else with you? (Y/N): ").lower() != "n":
    name = input("What is their name? ")
    age = get_valid_age("What is their age? ")
    attendees.append({"name": name, "age": age})

allowed = [f"{p['name']} ({p['age']})" for p in attendees if 16 <= p["age"] <= 21]


if allowed:
    print("\nAllowed attendees:")
    for entry in allowed:
        print(f"- {entry}")
else:
    print("\nSorry, no one is allowed to attend.")


#EX 10

sandwich_orders = ["Tuna", "Pastrami", "Avocado", "Pastrami", "Egg", "Chicken", "Pastrami"]

# other method. but i decided to keep the original list of orders:

# updated_sandwich_orders = []
# while 'Pastrami' in sandwich_orders:
#     sandwich_orders.remove('Pastrami')

updated_sandwich_orders = [s for s in sandwich_orders if s != 'Pastrami']

finished_sandwiches = []

for sandwich in updated_sandwich_orders:
     finished_sandwiches.append(sandwich)
     print(f'I made your {sandwich} sandwich.')

print(f"\nGood Job!\nHere's what we made: {finished_sandwiches}")

# print("\nGood job! Here's what we made:")
# for sandwich in finished_sandwiches:
#     print(f"- {sandwich}")

