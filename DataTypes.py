""" x = 3
y = float(3)
print(x, y) """


""" values = [1,2.23,5,7,2,30,15]
print(values[0])
print(values[6])
values.append("32")
print(values[7]) """


""" x = "this is a thing"
y = x.split( )
z = y[0]
print(y)
print(z) """

""" #Create an input function to ask the user for a sentence (inputs output strings).
sentence = input("Give me a sentence")
def count_words(sentence):
    words = sentence.split( )
    return len(words)
word_count = count_words(sentence)
print("Your sentence has", word_count, "words.") """

""" print(len(x)) """

""" day_of_week = input("What day is it? ")
if day_of_week == "Friday":
    print("correct")
else:
    print("incorrect") """

""" x = "test"
print(f"hello {x}") """

""" temp = 75
if temp > 68:
    print('warm')
elif temp == 68:
    print('perfect')
else:
    print('cold')
 """
""" friend_comes = True
money = True
def and_movies(friend, money):
    if friend == True and money == True:
        print("Going to the movies")
    else:
        print("I have no friends or I have no money")
and_movies(friend_comes, money) """

""" print( 5 %2) """

""" def factor(x, y):
    if x % y == 0:
        print(f"{y} is a factor of {x}")
factor(25, 5) """

""" friend = False
money = False
def or_movies(friend, money):
    if friend or money:
        print("Going to the movies")
    else:
        print("I have no money or I have no friends")
or_movies(friend, money) """

""" number = 8
def odd_or_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
odd_or_even(number) """


""" def calculate_tip():
    tip = input("How was our service?")
    if tip == "bad":
        tip = 0
    elif tip == "okay":
        tip = 0.15
    elif tip == "good":
        tip = 0.2
    elif tip == "great":
        tip = 0.25
    else:
        print("Invalid")


    bill = input("How much is the bill? ")
    bill = float(bill)
    tip_total = tip*bill
    total = bill + tip_total
    print(total)
calculate_tip()
 """

""" def factors_of(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)

n = int(input("Give me a number: "))
factors_of(n) """


""" x = input("Give me a number: ")
y= input("Give me another number: ")
x = int(x)
y = int(y)
z = x+y
for i in range(z):
    if x%z == 0 and y%z == 0:
        print(z)
        break
    else:
        z -=1 """

""" x = int(input("Give me a number: "))
y = int(input("Give me a number: "))
z = x+y
for i in range(z):
    if x%z == 0 and y%z == 0:
        print(z)
        break
    else:
        z -=1 """

""" def factors_of(n):
    for i in range(1, n + 1):
        if n%i == 0:
            print(i)
n = int(input("Give me a number: "))
factors_of(n) """


""" def calculate_tip():
    tip = input("How was our service?")
    if tip == "bad":
        tip = 0
    elif tip == "okay":
        tip = 0.15
    elif tip == "good":
        tip = 0.2
    elif tip == "great":
        tip = 0.25
    else:
        print("Invalid")


    bill = input("How much is the bill? ")
    bill = float(bill)
    tip_total = tip*bill
    total = bill + tip_total
    print(total)
calculate_tip() """


""" def calculate_tip():
    tip = input("How was our service?")
    if tip == "bad":
        tip = 0
    elif tip == "okay":
        tip = 0.15
    elif tip == "good":
        tip = 0.2
    elif tip == "great":
        tip = 0.25
    else:
        print("Invalid")


    bill = input("How much is the bill")
    tip_total = tip*bill
    Total = bill + tip_total
    print(Total)
calculate_tip() """

""" def calculate_tip():
    tip = input("How was our service? ")
    if tip == "Bad":
        tip = 0
    elif tip == "Okay":
        tip = 0.15
    elif tip == "Good":
        tip = 0.2
    elif tip == "Great":
        tip = 0.25
    else:
        print("Invalid")

    bill = input("How much is the bill? ")
    bill = float(bill)
    tip_total = tip*bill
    total = tip_total + bill
    total = float(total)
    print(total)
calculate_tip()
 """

""" def odd_or_even():
    number = input("Give me a number: ")
    number = int(number)
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")
odd_or_even() """

""" def factors_of():
    n = input("Give me a number: ")
    n = int(n)
    for i in range(1, n+1):
        if n%i == 0:
            print(i)
factors_of() """

""" def factors_of():
    factors = []
    n = int(input("Give me a number: "))
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    print(factors)
factors_of() """

""" x = int(input("Give me a number: "))
y = int(input("Give me a number: "))
z = x+y
for i in range(z):
    if x%z == 0 and y%z == 0:
        print(z)
        break
    else:
        z -=1 """

""" name = input("What is your name? ")
print(f"Your name is {name}.")
 """

""" students = ["Cadee", "Andy", "Mason"]
students.append("Alina")
for student in students:
    print(student) """

""" students = ["Cadee", "Andy", "Mason"]
if "Alina" in students:
    print("She's here!")
else:
    students.append("Alina")
    print("We added Alina")
for student in students:
    print(student) """

""" x = int(input("Give me a number: "))
if x < 25:
    print("Less")
elif x == 25:
    print("Equal")
else:
    print("Greater than 10") """

""" students = ["Cadee", "Andy", "Mason", "Alina"]
for student in students:
    found = False
    if student == "Mason":
        print("Found Mason")
        found = True """

name = "Cadee"
print(name[0])
for letter in name:
    print(letter)

