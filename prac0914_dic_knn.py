'''
Task 1.1

The serial numbers and specifications 
(brand, model, type, width, length, height, max_speed) of several
mobility devides are saved in two separate lists as shown
'''
serial_nos = ['523WR','924MN','1903MW','420QK','8421AB','92VC','292KS','32XC']

# [brand, model, type, width, length, height, max_speed]
details = [
['Telmo','Speed23','PMD',0.7,1.1,1.33,9],
['Nimbus','SmooXth','Scooter',0.3,0.5,1.5,10],
['Lambo','Comfit1','PMD',0.5,1.15,1.35,8],
['Stylo','CoolD','PMD',0.6,1.2,1.4,10],
['Nimbus','SailX','PMD',0.55,0.95,1.3,9.5],
['Lambo','Zipline','Scooter',0.25,1.2,1.3,10],
['Telmo','Coastie','PMD',0.7,1.1,1.33,10],
['Telmo','Wheeler5','PMD',0.6,0.9,1.3,9]
]

'''
Edit the program so that it

(a) Creates a dictionary registered, and saves the serial numbers of the 
mobility devides as the key of a dictionary and its corresponding
list of specifications or details as its values. [2]
'''
# Write and test your code here
registered = {}

for i in range(len(serial_nos)):
    thisno = serial_nos[i]
    thisdetails = details[i]
    registered[thisno] = thisdetails
'''
(b) delete the records for serial number '1903MW' from registered. [1]
'''
# Write and test your code here
del(registered['1903MW'])



'''
(c) adds a new record to registered for serial number '842AB' with
the following list ['Telmo', 'Roadster', 'PMD', 0.55, 1.12, 1.45, 10] [1]
'''
# Write and test your code here
registered['842AB']
x = ['Telmo', 'Roadster', 'PMD', 0.55, 1.12, 1.45, 10]
registered[x] = 
'''
Task 1.4
The file mobilitydevices.csv contains data of registered mobility devices 
and their respective specifications. Write a program code to read and 
extract the data into a list. [2]
'''
# Write and test your code here
# mobilitydevices.csv

'''
brand,model,type,width,length,height,max_speed
Telmo,Speed23,PMD,0.7,1.1,1.33,9
Nimbus,SmooXth,Scooter,0.3,0.5,1.5,10
Lambo,Comfit1,PMD,0.5,1.15,1.35,8
Stylo,CoolD,PMD,0.6,1.2,1.4,10
Nimbus,SailX,PMD,0.55,0.95,1.3,9.5
Lambo,Zipline,Scooter,0.25,1.2,1.3,10
Telmo,Coastie,PMD,0.7,1.1,1.33,10
Telmo,Wheeler5,PMD,0.6,0.9,1.3,9

'''



'''
Task 1.5
Write a program code that uses the K-Nearest Neighbour (k=1) algorithm to 
predict the type of a mobility device given its width and length.
The program should prompt the user to input the width and length of an
unknown mobility device and display the predicted type of the device
based on the algorithm.

Test your program using the following values: 
width = 0.8 and length = 0.4 [5]
'''
# Write and test your code here

'''
Task 1.6
Copy and paste your program from sub-task 1.5 into a new code cell.

Edit your program so that it uses the K-Nearest Neighbour (k=1) algorithm 
to predict the type of a mobility device given three parameters, 
the length, width and height of the device. 

The program should prompt the user to input the length, width and height 
of an unknown mobility device and display the predicted type of the 
device based on the algorithm.

Test your program using the following values: 
width = 0.8 and length = 0.4 and height = 1.2.
[2]
'''
# Write and test your code here