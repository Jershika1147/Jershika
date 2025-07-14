a=input("Enter the text:")
vowels=["a","e","i","o","u"]
vowelscounter=0
consonantscounter=0
for i in a:
    if i in vowels:
        vowelscounter=vowelscounter+1
    else:
        consonantscounter=consonantscounter+1
print("Vowels:",vowelscounter,end=" ")
print("Consonants:",consonantscounter)

print(f"Vowels:{vowelscounter}    Consonants:{consonantscounter}")

