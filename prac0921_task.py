total = 0
a = 0
highest = 0
days = int(input("please enter the number of days: "))
for i in range(days):
    rainfall = float(input("Enter the amount of rainfall: "))
    total = total + rainfall
    if rainfall == 0:
        a=a+1
    if rainfall > highest:
        highest = rainfall
highest = round(highest, 1)
average = total/days
average = round(average, 2)


print("Total weekly rainfall is %d mm."%total)
print(a)
print(highest)
print(average)