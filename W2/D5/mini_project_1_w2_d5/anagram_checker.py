import os


class AnagramChecker:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        with open(f"{dir_path}/sowpods.txt", 'r', encoding='utf-8') as f:
            words_database = f.read()
        self.words_database = words_database.split()
    
    
    def is_valid_word(self, word):
        if word.upper() in self.words_database:
            return True
        else:
            return False

    def get_anagrams(self, word):
        anagrams = []
        for w in self.words_database:
           if sorted(word.upper()) == sorted(w) and word.upper() != w:
               anagrams.append(w)
        if not anagrams:
            return "No anagrams found"               
        return ", ".join(anagrams)
               
           


    
ac_1 = AnagramChecker()
# => Chech "__init__"
# print(ac_1.words_database)

# => Check "is_valid_word(self, word)"
# print(ac_1.is_valid_word('AARDVARKS'))
# print(ac_1.is_valid_word('AARDVARKS_'))

# => Check "get_anagrams(self, word)"
# print(ac_1.get_anagrams('HUH'))
# print(ac_1.get_anagrams('abc'))


