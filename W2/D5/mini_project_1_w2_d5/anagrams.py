from anagram_checker import AnagramChecker


def print_menu():
    return ("""
Please either:
1. Enter a single word
   OR   
2. Exit (Enter: 2 )\n
""")
# print_menu()


def print_answer(valid_word, checker):
    return (f"""
\033[1mYOUR WORD: {valid_word.upper()}
This is a valid English word.
Anagrams for your word: {checker.get_anagrams(valid_word)}\033[0m
""")


def valid_input():
    user_input = input(print_menu()).strip()
    if user_input == '2':
        return 'exit'
    if " " in user_input:
        return "not a single word"
    if not user_input.isalpha():
        return "Only alphabetic characters are allowed"
    return user_input

def main_function():
    print("\nWelcome to the Anagram Checker!")
    while True:
        checker = AnagramChecker()
        user_input = valid_input()
        if user_input == 'exit':
            print("\nGoodbye!\n")
            break
        elif user_input in ["not a single word", "Only alphabetic characters are allowed"]:
            print(f"Not valid input: {user_input}")
        else:
            print(print_answer(user_input, checker))


main_function()


word = "Test"

# print("=" * 40)
# print(f"""\033[1mYOUR WORD: {word.upper()}
# This is a valid English word.
#       """)
# print("=" * 40)



