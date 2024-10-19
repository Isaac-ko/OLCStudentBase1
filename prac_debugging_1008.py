'''
Mock Task 3 Question 1
A library program needs to keep track of books being borrowed and returned. 
Each book has a unique ID and a title. The program allows a user to 
input the book ID and whether the book is being borrowed or returned. 
The program updates the status of the book accordingly and displays a message. 
There are several syntax and logic errors in the program.
'''
### DO NOT CHANGE the first 3 lines of code.
# books = {"1": "AVAILABLE", "2": "AVAILABLE", "3": "AVAILABLE", "4":"BORROWED"}
# action = input("Enter 'B' to borrow a book or 'R' to return a book: ")
# book_id = input("Enter the book ID: ")
# ### Make your code fixes after this

# if action == "B":       #1.add colon and change = to ==#
#     if books[book_id] == "AVAILABLE":#chnage to upper case#
#         books[book_id] = "BORROWED"#change upper to lowercase and book_id#
#         print("You have borrowed the book.")
#     else:
#         print("The book is already borrowed.")
# elif action == "R":          #2.change = to == and capitalise#
#     if books[book_id] == "BORROWED":#chnge to upper case#
#         books[book_id] = "AVAILABLE"     #7. chnage to square bracket and change to book_id#
#         print("You have returned the book.")    #3.add " at start of print#
#     else:
#          print("The book is already available.")#4.add indentation#
# else:       #6.remove indentation#
#     print("Invalid action.")   #5.add " at the start#

# print(books) # this is for checking


# foods = {"burger":"$5", "pasta":"$10"}
# print(foods)
# foods["pizza"] = "$15 "# to add a new item 
# print(foods)
# foods["pizza"] = "$20 "# to edit a new item 
# print(foods)

# '''
# Open the file LIBRARY.py. Save the file as 
# MYLIBRARY_<your name><center number><index number>.py.
# Identify and correct the errors in the program so that it works according to 
# the requirements given. Save your program.
# [10 marks]
# '''
# if action == "b":       
#     if books[book_id] == "Available":
#         books["B"] = "borrowed"
#         print("You have borrowed the book.")
#     else:
#         print("The book is already borrowed.")
# elif action = "r":
#     if books[book_id] == "borrowed":
#         books("R") = "available"
#         print(You have returned the book.")
#     else:
#     print("The book is already available.")
#     else:
#         print("Invalid action.)




########################answer


# if action == "B": # 3. added = and colon
#     if books[book_id] == "AVAILABLE":
#         #print("a")
#         books[book_id] = "BORROWED" # change to upper case, and book_id
#         print("You have borrowed the book.")
#     else:
#         #print("b")
#         print("The book is already borrowed.")
# elif action == "R": # 4. added =
#     if books[book_id] == "BORROWED": # change to capital letters
#         print("cccc")
#         #books("R") = "available"  # 5. round bracket is wrong way to call dictionary
#         books[book_id] = "AVAILABLE" # change to all capitals for AVAILABLE
#         print("You have returned the book.") #1. add quotation mark
#     else:
#         print("dddd")
#         print("The book is already available.") # 6. indentation error
# else: # 7. wrong indentation for else, should be part of if on line 15
#     print("Invalid action.") # 2 missing quotation

# print(books)


###########################################

'''
Mock Task 3 Question 2
A program calculates the total cost of items bought by a customer in a 
grocery store. Each item has a price and quantity. The program should 
allow the user to input the price and quantity of each item, 
calculate the total cost, apply a discount if applicable, 
and display the final cost. 

A discount of 10% is applied if the total cost of the items is more than $100
A discount of 15% is applied if the total cost of the items is more than $200

There are several syntax, logic, and runtime errors in the program.
'''

total_cost = 0

while True:
    price == input("Enter the price of the item: ")
    quantity = input("Enter the quantity of the item: ")
    cost = price + total_cost
    
    more_items = input("Do you have more items? (Y/N): ")#added "#
    
    if more_items == "n":#chnaged == and added collon#
        continue

if total_cost > 100:
    reduced_cost = total_cost/100 * 10
    cost = total_cost - reduced_cost

print("A 10% discount has been applied.")
else:
total_cost = total_cost * 20%
print("A 20% discount has been applied.")
    
print("The total cost is:" total_cost)

'''
Open the file GROCERY.py. Save the file as 
MYGROCERY_<your name><center number><index number>.py.
Identify and correct the errors in the program so that it 
works according to the requirements given. Save your program.
[10 marks]
'''

# total_cost = 0

# while False:
#     price == input("Enter the price of the item: ")
#     quantity = input("Enter the quantity of the item: ")
#     cost = price + total_cost
    
#     more_items = input("Do you have more items? (Y/N): )
    
#     if more_items = "n"
#         continue

# if total_cost > 100:
#     total_cost = total_cost * 10%
# print("A 10% discount has been applied.")
# else:
#     total_cost = total_cost * 20%
# print("A 20% discount has been applied.")
    
# print("The total cost is:" total_cost)
