'''
Practice 1

list1 = 
## Question: Find the maximum number in this list
1. find max in the list
2. find min in the list
3. find sum of all the items in the list
4. find count of all items in the list
5. find average of all items in the list
6. find position of max in the list
... all the above without using in-built functions
'''
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]
num1 = 1000000000000000000
num = 0
count = 0
count1 = 0
for i in list1:
    if i > num:
        num = i
    if i < num1:
        num1 = i
    
print(num)
print(num1)

# counter variable

for i in list1:
    count = count + 1
print(count)
average = num / count
print(average)

# count = 0
for i in list1:
    if i == num:
        break # stop the loop
    count1 += 1
print(count1)


