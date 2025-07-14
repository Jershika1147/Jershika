for x in range(2,100):
    prime=False
    for i in range(2,x):
        if x % i == 0:
            prime=False
            break
        else:
            prime=True
    if x==2:
         print(f"{x} is a prime")
    elif prime==True:
         print(f"{x} is a prime")
    else:
         print(f"{x} is not a prime")
        
        