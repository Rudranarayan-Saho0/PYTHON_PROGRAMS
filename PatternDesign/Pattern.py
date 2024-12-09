n = int(input("Enter Number Of rows: "))
ch = input("Enter a Character: ")
i = 1
while i<=n:
    j = 1
    while j <=i:
        print(ch, end = " ")
        j = j+1
    print()
    i +=1