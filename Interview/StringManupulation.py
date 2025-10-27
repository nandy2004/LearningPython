string=input("Enter the string : ")
vowels="aeiouAEIOU"
for i in string:
    if i in vowels:
        string=string.replace(i, "")
print(string)

string1=input("Enter the string: ")
frequency={}
for char in string1:
    if char in string1:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Frequency of Character in string")
for key , value in frequency.items():
    print(f"{key},{value}")
    