x=[7,5,6,5,7,1,5,3,9,5]
counter=0
dictionary={}
for i in x:
    counter=0
    for y in x:
        if i==y:
            counter=counter+1
    dictionary[i]=counter
print(dictionary)
temp_value=0
temp_key=0
for a,b in dictionary.items():
    if temp_value < b:
        pass
    else:
        temp_value=b
        temp_key=a
print(temp_key)
    