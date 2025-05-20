from datetime import datetime, date

# class Person:

#     def __init__(self, name, last_name, birthd_date):
#         self.name = name
#         self.last_name  = last_name
#         self.birth_date = self.parse_birthday(birthd_date)

#     @classmethod
#     def from_age(cls, name, last_name, age):
#         current_year = datetime.today().year
#         birth_year = current_year - age
#         birth_date = date(birth_year, 1, 1)
#         return cls(name, last_name, birth_date)
#         # Return Person (name, last_name, birth_date)


#     @staticmethod
#     def parse_birthday(date_string):
#         return datetime.strptime(date_string, '%y-%m-%d').date()
    


# p1 = Person('Alice', 'Wonder', '1990-02-05')
# p2 = Person.from_age('Bob', 'Smith', 30)
# print(p2.birth_date)
# # print(p1.name)
# # print(type(p1.parse_birthday))

# # p2 = Person('Bob', 'Smith', 30)

# # print(datetime.today().year)

class Person:

    def __init__(self, name, last_name, birth_date):
        self.name = name
        self.last_name = last_name
        self.birth_date = self.parse_birthdate(birth_date)

    @classmethod
    def from_age(cls, name, last_name, age):
        current_year = datetime.today().year
        birth_year = current_year - age
        birth_date = f'{birth_year}-1-1'
        return cls(name, last_name, birth_date)

    @staticmethod
    def parse_birthdate(date_string):
        return datetime.strptime(date_string, '%Y-%m-%d').date()
    # @staticmethod
    # def parse_birthdate(date_string):
    #     return datetime.strptime(date_string, '%y-%m-%d').date()
    
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        return age # because a property method - the age can be accessed as an attribute

    

p1 = Person('Alice', 'Wonder', '1990-02-05')
# p2 = Person.from_age('Bob', 'Smith', 30)
# print(p2.birth_date)
# print(p1.name)
# print(type(p1.parse_birthday))

# p2 = Person('Bob', 'Smith', 30)

# print(datetime.today().year)

print(type(p1.age))
print(p1.age)


# create a static method that format the name and last name in case the first latter is not upper
# usage example:
p1 = Person('juliana', 'shmidt', 35)
# the static method will change it to capital case