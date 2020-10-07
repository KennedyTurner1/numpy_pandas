'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in original_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

# [ expression for item in list if conditional ]

# This is equivalent to:

'''for item in list:
    if conditional:
        expression '''
		
		


#Which corresponds to:

#*result*  = [*transform*    *iteration*         *filter*     ]

#The * operator is used to repeat. The filter part answers the question if the
#item should be transformed. '''

#new way
x = [i for i in range(10)]

print(x)

my_list = []

#old way
for x in range(10):
    my_list.append(x)

print(x)

#adding an expression 

squares = [x**2 for x in range(10)]

print(squares)

#you can multiply to elements in a list
list1 = [3,4,5]

multiplied = [item*3 for item in list1]

print(multiplied)

#strings

list_of_words = ['this', 'is', 'a', 'list', 'of', 'words.']

items = [word[0] for word in list_of_words]

print(items) #takes the first character in each word and shows it in a list

upper = [x.upper() for x in ['a','b','c']]

print(upper)

lower = [x.lower() for x in ['a','b','c']]

print(lower)

##if filter

new_range = [i * i for i in range(5) if i % 2 == 0] #if the remainder of i divided by 2 is 0

print(new_range) #[0, 4, 16]

#extract within string

string = 'Hello 12345 World'

numbers = [x for x in string if x.isdigit()]

print(numbers)

#extract alphabet in string

letters = [x for x in string if x.isalpha()]

print(letters)

myfile = open('test.txt', 'r')

result = [i for i in myfile if "line2" in i]

print(result)

def double(x): 
    return x*2

print(double(10)) #20

result1 = [double(x) for x in range(10)]

print(result1) #[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

result2 = [x + y for x in [10,20,30] for y in [40,50,60]]

print(result2) #[50, 60, 70, 60, 70, 80, 70, 80, 90]

### self exercises 
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

newlist = [i for i in numbers if i > 0]

print(newlist) #[34.6, 44.9, 68.3, 44.6, 12.7]

#2 

sentence = 'the quick brown box jumps over the lazy dog'
words = sentence.split()

int_list = [len(word) for word in words  if word != 'the']

print(int_list) #[5, 5, 3, 5, 4, 4, 3]













## Exercise ##

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]




## 2 create a list of integers which specify the length of each word in
## a sentence except for the word 'the'

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()



## Given dictionary is consisted of vehicles and their weights in kilograms. 
## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
## In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}