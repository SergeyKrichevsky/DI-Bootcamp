#CH1

# Instructions:
# Write a Python program that takes a single string of words as input, 
# where the words are separated by commas (e.g., ‘apple,banana,cherry’). 
# The program should output these words sorted in alphabetical order, 
# with the sorted words also separated by commas.

# Step 1: Get Input
# Use the input() function to get a string of words from the user.
# The words will be separated by commas.

user_input = input('Write a string of words, seperated by coma')

# Step 2: Split the String

user_words = user_input.split(',')

# Step 3: Sort the List

user_words_sorted = sorted(user_words)

# Step 4: Join the Sorted List

sorted_input = ','.join(user_words_sorted)

# Step 5: Print the Result

print(sorted_input)

# Print the resulting comma-separated string.
# Expected Output:
# If the input is without,hello,bag,world, the output should be 
# bag,hello,without,world.

#CH2

# Instructions:

# Write a function that takes a sentence as input and 
# returns the longest word in the sentence. 
# If there are multiple longest words, 
# return the first one encountered. 
# Characters like apostrophes, commas, and periods 
# should be considered part of the word.

# Step 1: Define the Function
# Define a function that takes a string (the sentence) as a parameter.
# Step 2: Split the Sentence into Words
# Step 3: Initialize Variables
# Step 4: Iterate Through the Words
# Step 5: Compare Word Lengths
# Step 6: Return the Longest Word

def longest_word (string):
    '''longest_word (string)'''
    words = string.split(' ')
    longest_word = ''
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

# ==> Testing Variants:
# print(longest_word("Margaret's toy is a pretty doll."))
# print(longest_word("A thing of beauty is a joy forever."))
# print(longest_word("Forgetfulness is by all means powerless!"))

# Expected Output:
# longest_word("Margaret's toy is a pretty doll.") should return "Margaret's".
# longest_word("A thing of beauty is a joy forever.") should return "forever.".
# longest_word("Forgetfulness is by all means powerless!") should return "Forgetfulness".