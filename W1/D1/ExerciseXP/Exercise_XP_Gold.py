#EX1

#greeting = 'Hello world'
#p_love = 'I love python'
#print(f'{greeting}\n' * 4)
#print(f'{p_love}\n' * 4)

#EX2

spring_months = ['march', 'april', 'may']
summer_months = ['june', 'july', 'august']
autumm_months = ['september', 'october', 'november']
winter_months = ['december', 'january', 'fabuary']

current_month = input('What monthh is it now? ')
if current_month.lower() in spring_months:
    print("It's spring!")
elif current_month.lower() in summer_months:
    print("It's summer!")
elif current_month.lower() in autumm_months:
    print("It's autum!")
elif current_month.lower() in winter_months:
    print("It's winter!")
else:
    print('Wrong month name')

