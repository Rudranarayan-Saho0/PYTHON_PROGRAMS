string = input("Enter a String For Check Palindrom Or Not: ")
reverse= string[::-1]
if string==reverse:
    print(f"{string} is Palindrom.")
else:
    print(f"{string} is not Palindrom.")