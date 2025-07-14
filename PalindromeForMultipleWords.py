value=input("Enter the word:")
x=value.replace(" ","")
y=x[::-1]
if x==y:
    print("Palindrome")
else:
    print("Not Palindrome")
    