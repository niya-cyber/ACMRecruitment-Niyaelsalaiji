n=20
print("to calculate the smallest multiple")
while True:
    count=0
    for i in range(1,21):
        if n%i==0:
            count+=1
        else:
            n+=20
            break
        
    if count==20:
        print("smallest positive number that is evenly divisible by all of the numbers from 1 to 20:",n)
        break
