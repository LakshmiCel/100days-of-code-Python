# to find the maximum and sum without using sum() and max() function 

scores = [11, 3, 4, 7, 8, 34, 65, 233]
sum = 0
for score in scores:
    sum += score

print("The sum of scores is: ", sum)

max = 0
for score in scores:
    if (max < score):
        max = score

print("The maximum score is: ", max)

#gauss challenge - sum of numbers from 1- 100
sum = 0
for num in range(0, 101):
    sum += num
print("Gaussian challenge: ", sum)
     