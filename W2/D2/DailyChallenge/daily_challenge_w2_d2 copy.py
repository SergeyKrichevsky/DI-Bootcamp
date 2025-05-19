# CH

import math

class Pagination:
    def __init__(self, items = None, page_size = 10):
        if items == None:
            self.items = []
        else:
            self.items = items
        self.page_size = page_size
        self.current_idx = 0
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx
        end = self.current_idx + self.page_size
        current_page = self.items[start : end]
        return current_page
    
    def go_to_page(self, page_num):
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f'The number is out of range. There are {self.total_pages} pages')
        else:
            self.current_idx = self.page_size * (page_num -1)

    def first_page(self):
        self.go_to_page(1)
        return self
    
    def last_page(self):
        self.go_to_page(self.total_pages)
        return self
    
    def next_page(self):
        current_page_number = self.current_idx // self.page_size + 1
        if current_page_number == self.total_pages:
            raise ValueError ('There is no next page.')
        else:
            self.current_idx = self.current_idx + self.page_size
            return self

    def previous_page(self):
        current_page_number = self.current_idx // self.page_size + 1
        if current_page_number == 1:
            raise ValueError ('There is no previous page')
        else:
            self.current_idx = self.current_idx - self.page_size
            return self
        
    def __str__(self):
        lines = [item for item in self.items[self.current_idx : self.current_idx + self.page_size]]
        return '\n'.join(lines)

# Previous version of ""__str__(self) function. Does`nt works correctly with last page, if the page is not full:
    # def __str__(self):
    #     current_page = ''
    #     for i in range(self.current_idx, self.current_idx + self.page_size):
    #         if i <= len(self.items - 1)
    #             current_page += self.items[i]
    #             current_page += '\n'
    #         else:
    #             return current_page
    #     return current_page


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

print(p.__str__())

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

print(p.__str__())

p.last_page()
print(p.get_visible_items())
# # ['y', 'z']

print(p.__str__())

p.go_to_page(2)
print(p.current_idx + 1)

p.go_to_page(10)
print(p.current_idx + 1)
# # Output: 7
# => Mistake in excercise discription: "p.go_to_page(10)" with the corrent example list - should Raises ValueError (not "Output: 7")

p.go_to_page(0)
# # Raises ValueError