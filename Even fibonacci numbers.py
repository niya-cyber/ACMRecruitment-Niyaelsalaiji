total=0
print("to print all the even fibonacci numbers")
a,b=0,1
while a<=4000000:
    c=a+b
    if c%2==0:
      total+=c
    a,b=b,c
print("Sum of the even valued terms:",total)
