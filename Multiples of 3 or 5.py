sum_3=0
sum_5=0
print("to find the sum of all the multiples of 3 or 5 below 1000")
for i in range(1,1000):
    if i%3==0:
        sum_3+=i
    if i%5==0:
        sum_5+=i
    if i%3==0 and i%5==0:
        sum_3-=i
print("The sum of all the multuplies of 3 or 5:",sum_3+sum_5)   
 
