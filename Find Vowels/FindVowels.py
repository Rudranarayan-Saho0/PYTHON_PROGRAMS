#A Python Program That Check The Vowels In An Inputed String.
Ch_vowel=input("Enter A String: ").lower()
Vowel = "aeiou"
print("Vowel In The string are: ")
i = 0
while i<len(Ch_vowel):
    if Ch_vowel [i] in Vowel:
        print(Ch_vowel[i],end=" ")
    i+=1    
print()