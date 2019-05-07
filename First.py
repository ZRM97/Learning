price = 50
apple = 4.2
print('Hello World!')
print(price)
print(price * 2)
print(price * apple)

name = input('What is your name? ')
favourite_color = input('What is your favourite color? ')
print(name + ' likes ' + favourite_color)

birth_year = input('Enter your birth year: ')
age = 2019 - int(birth_year)
print(age)

weight_pounds = input('Enter your weight in Pounds: ')
weight_kilograms = float(weight_pounds) / 2.2046
print(weight_kilograms)

alphabets = "abcdefghijklmnopqrstuvwxyz"
print(alphabets.upper()[0:6])

first = input('Enter your First Name: ')
last = input('Enter your Last Name: ')
msg = f'{first} [{last}] is a coder'
print(msg)