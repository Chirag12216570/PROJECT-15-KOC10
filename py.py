a=int(input("enter your starting range"))
b=int(input("enter your ending range"))
for i in range(a,b+1):
    for l in range(2,int(i/2)+1):
        if i%l==0:
            print(i," is a composite number")
            break
        else:
            print(i," is a prime number")
else:
    print(i," is a composite number")

            
 
