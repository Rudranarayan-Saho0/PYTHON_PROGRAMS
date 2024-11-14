while True:
    q = input('Add (a) \nSearch(s)\nQuit(q)\nEnter Your Choice: ')
    if q=='a':
        with open('contact.txt','a') as f:
            name = input('Name: ')
            number = int(input('Number: '))
            f.writelines(f"{name} : {number}\n")

    elif q == 's':
        search = input('Enter name or number for search')
        with open('contact.txt','r') as f:
            found = False
            for i in f:
                if search in i:
                    print(i.strip())
                    found = True
                if not found:
                    print('No Match Found.')

    elif q == 'q':
        break

    else:
        print("Invalid Choice, No Match Found")

#This is a simple Contact Book Application .
#It allow Users To Add Contacts And Search for Contacts By Name Or Number.
