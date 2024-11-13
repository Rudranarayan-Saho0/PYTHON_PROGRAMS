while True:
    with open('contact.txt','a') as f:
        name = input('Name: ')
        number = input('Number: ')
        f.writelines((name,' : ',number,'\n'))