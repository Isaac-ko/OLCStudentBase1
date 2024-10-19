# '''
# (a)
# You are required to create a dictionary variable name_score using the 2 variables below.
# the key is the name of the student, and the value is the math score.
# '''
# names = "jack,mary,john,kevin,leon,noel,chloe,phoebe,emma"
# mathscore = "67,56,45,2,88,75,96,92,83"
# name_score = {}
# # name_score = {}

# # namelist = names.split(",") # 
# # mathscorelist = mathscore.split(",")
# # print(namelist)

# # for i in range(len(namelist)):
# #     currentname = namelist[i] # retrieving the item at the ith index
# #     currentscore = mathscorelist[i] # retrieving the item at the ith index
# #     name_score[currentname] = currentscore

# # print(name_score)
# namelist = names.split(",")
# mathscorelist = mathscore.split(",")

# for i in range(len(namelist)):
#     current_name = namelist[i]
#     current_score = mathscorelist[i]
#     name_score[current_name] = current_score # add toa dictioary
#     print(name_score)


# '''
# (b)
# Write code to determine the name and score of the highest scorer
# '''
# # write and test your code here


# '''
# (c)
# Write code to determine the average score of the class.
# '''
# # write and test your code here

# '''
# (d)
# Write a function called output_message() with 2 parameters, the name and the score
# Your function will return the string "[Student name]'s score is [score]"
# e.g. "jack's score is 67"
# '''
# # write and test your code here



# '''
# (e)
# Program that makes use of dictionary

# - Imagine you are writing a program to record student's mark
# - THe pogram consist of a dictionary of students name and their marks

# Your program have the option to add new student, delete existing student, and update student mark
# Your program can extract all the marks and calculdate the average mark

# a) create a dictionary called student_mark
# b) Ask for a student's name
# c) Ask for the student's score
# d) add this to the dictionary
# e) keep asking until the teacher say stop

# '''


# #Write and test your code here
# student_mark = {}

# while True:
#     choice = int(input("enter 1 to add new student, 2 to delte existing student, 3 to update student mark, 4 to stop adding :"))

#     if choice == 1:
#         while True: #infinite loop
#             names = input("What is the student's name? ")
#             mark = input("What is student's mark ")
#             student_mark[names] = mark

#             tocontinue = input("Any more students? Y or N").lower() # .upper(), .lower()
#             if tocontinue == "n":
#                 break # break to stop the loop
#             else:
#                 continue # continue with the loop

#     elif choice == 2:
#         # remove who??
#         remove = input("who to remove ")
        
#         if remove in student_mark:
#             # remove the student
#             del(student_mark[remove])
#         else:
#             # print("{} is not in the dictionary".format(remove))
#             print(remove, " is not in the dictionary.")

#     elif choice == 3:
#         student = input("Who to update? ")
#         if student in student_mark:
#             new_mark = input("What is the new mark? ")
#             student_mark[student] = new_mark # update the new mark
#         else:
#             print(student, " is not in the dictionary.")

#     elif choice == 4:
#         print("Ok bye bye")
#         break

#     else:
#         print("Invalid option: ", choice)
        
#     print(student_mark)

# for sm in student_mark: #sm is the key (student's name)
#     print(sm, "'s mark is :", student_mark[sm]) # student_mark[sm] retrieves the value
''''
Program that makes use of dictionary

- Imagine you are writing a program to record student's mark
- THe pogram consist of a dictionary of students name and their marks

Your program have the option to add new student, delete existing student, and update student mark
Your program can extract all the marks and calculdate the average mark

a) create a dictionary called student_mark
b) Ask for a student's name
c) Ask for the student's score
d) add this to the dictionary
e) keep asking until the teacher say stop
'''
student_mark = {}

while True:
    choice = int(input("type 1 to add a student mark into the dictionary 2 to remove a name and 3 to modify the name and 4 to stop the programme: "))
    if choice == 1:
        while True:
            names = input("what is students name: ")
            mark = input("what is student mark: ")
            student_mark[names] = mark
            tocontinue = input("type Y to continue and N to stop").lower()
print(student_mark)


