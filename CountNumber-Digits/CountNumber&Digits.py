#A Simple Python program To Count The Number & digits Inside A String.
string = input("Enter A String: ")
Digits = 0
Alphabets = 0
i = 0
while i<len(string):
    if string[i].isdigit():
        Digits+=1
    elif string[i].isalpha():
        Alphabets+=1
    i+=1
print(f"The Number Of Digits = {Digits} & Number Of Alphabets = {Alphabets}.")