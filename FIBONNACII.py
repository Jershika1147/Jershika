print("Choose one Option")
print("1. Nth Fibonacci Number")
print("2. 0 to N Fibonacci Numbers")
print("3. First N Fibonacci Numbers")

choice = int(input("Enter your option (1/2/3): "))
n = int(input("Enter the value: "))

a = 0
b = 1
if choice == 1:
        for i in range(2,n):
            temp = a + b
            a = b
            b = temp
        print("Nth Fibonacci number is:", b)
elif choice == 2:
    print("Fibonacci sequence from 0 to n:")
    print(a)
    print(b)
    for i in range(2,n):
        if b<=n:
            temp = a + b
            a = b
            b = temp
            print(b)
        else:
            break
elif choice == 3:
    print("First", n, "Fibonacci numbers:")
    print(a)
    print(b)
    for i in range(2, n):
        temp = a + b
        a = b
        b = temp
        print(b)
else:
     print("Error!")
