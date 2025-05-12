#CH1


def get_valid_number(prompt):
     while True:
          user_input = input(prompt)
          try:
               return int(user_input)
          except ValueError:
               print('Please enter a valid number.')

user_number = get_valid_number('Give me a number')
user_length = get_valid_number('How long the list should be?')

final_list = []

x = user_number

for i in range(user_length):
     final_list.append(x)
     x += user_number

print(final_list)


#CH2

user_input = input("Enter a word: ")
result = ""

previous_char = None
for char in user_input:
    if char != previous_char:
        result += char
    previous_char = char

print(result)

# alternative way:
# (less friendly for reading, if the logic is not obvious)

# user_input = input("Write something: ")
# result = ""

# for i in range(len(user_input)):
#     if i == 0 or user_input[i] != user_input[i - 1]:
#         result += user_input[i]

# print(result)
