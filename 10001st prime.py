count=0
a=2
while True:
    for i in range(2, a):
        if a%i==0:
            break
    else:
        count+=1
        if count==10001:
            print("the 10001st prime is:",a)
            break
    a+=1
