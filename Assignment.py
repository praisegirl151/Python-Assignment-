#creating a String using single quotes, double quotes and triple quotes
word1 = 'Hello '
word2 = "Welcome"
word3 = """ to Python Class"""
print(f"{word1}{word2}{word3}")

#variable assignment and printing
sentence = "Python is fun to learn!"
print(sentence)

#Using a Multiline string
multiline_string = """
Python is powerful.
Its easy to learn. 
Its loved by developers
"""
print(multiline_string)

#Section B – Strings as Arrays

#creating a variable text and printing the first, third and last characters
text =("PYTHON")

print(text[0])  #first character
print(text[2])  #third character
print(text[5]) #last character

#looping through a string using for loop
language = "Python"
for letter in language:
    print(letter)

#length of a string
fruits = "Banana"
print(len(fruits))

#Creating a variable called word and assign the string
word = "Learning Python is cool"

if "Python" in word:
    print("Yes, 'Python' is found!.")
if "Java" in word:
    print("Yes, 'Java' is found!.")
else:
    print("No, 'Java' is not found in the sentence.") 

#Bonus Task
message = "Coding is fun"
count = 0

for letter in message:
    if letter == "n":
        count += 1
print(count)

#poem using a multiline string 
poem = """
Python whispers, sleek and bright,
Guiding coders through the night.
Loops and functions, clear and neat,
Every bug it helps defeat.
In its code, the world feels light.
 """
print(poem)

#This is the Second Assignment
name = "Ada"
age = "18"
school = "Bright Future Academy"

print(f"My name is {name}. I am {age} years old and I attend {school}.")

country = "Nigeria"
capital = "Abuja"
print(f"The capital of {country} is {capital}")

first_name = "John"
middle_name = "Paul"
last_name = "Okoro"

print(f"{first_name} {middle_name} {last_name}")

food = "Rice"
drink = "Juice"
print(f"I love eating {food} with {drink}")
