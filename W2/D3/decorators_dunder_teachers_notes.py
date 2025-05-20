from datetime import datetime, date

class Person:

    def __init__(self, name, last_name, birth_date):
        self.name = self.format_name(name)
        self.last_name = self.format_name(last_name)
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
    
    @staticmethod
    def format_name(name):
        if not name[0].isupper():
            return name.capitalize()
        else:
            return name
        
    @property
    def age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        return age
    
    def __str__(self):
        return f'{self.name} {self.last_name} was borned on {self.birth_date}, \n age {self.age}'
    
    def __repr__(self):
        return f'{self.__dict__}'
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __lt__(self, other):
        return self.age < other.age
    

p1 = Person('Alice', 'Wonder', '1990-02-05')
# print(type(p1.birth_date))
# print(p1.age) #because I have @property method, the age can be accessed as an atribute
print(p1.age)
print(repr(p1))


p2 = Person.from_age('Bob', 'Smith', 55)
# print(p2.birth_date)
print(p1 == p2)
print(p1 < p2)


#create a static method that format the name and last name 
# in case the first letter is not upper case
#usage example: 
# print(Person('john','snow',32))
# print()

#the static method will change it to capital case.