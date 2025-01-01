Start = input("Do You Want To Start The Quiz game: (Yes/No)").strip().lower()
Score = 0
#print(f"Debug: Start value is '{start}'")
if Start == 'yes':
    Quiz1 = input(' Q1. Who Discover Python Language?').strip().lower()
    if Quiz1 == 'guido van rossum':
        print('Good')
        Score= Score+1
    else:
        print("Try Next Question")

    Quiz2 = input('What Type Of Languagen Is Python?')
    if Quiz2.lower() == 'interpreted':
        print('Good')
        Score= Score+1
    else:
        print("Try Next Question")

    Quiz3 = input('Which Keyword Is Used For Function In Python?')
    if Quiz3.lower() == 'def':
        print('Good')
        Score= Score+1
    else:
        print("Try Next Question")

    Quiz4 = input('Q4. Is Python Case Sensitive?')
    if Quiz4.lower() == 'yes':
        print('Good')
        Score= Score+1
    else:
        print("Try Next Question")

    Quiz5 = input('What is The Extension Of Python file?')
    if Quiz5.lower() == '.py':
        print('Good')
        Score= Score+1
    else:
        print("Try Next Question")

    Quiz6 = input('Q6. What Are Two Main Type Of Function In Python?')
    if Quiz6.lower() == 'built in & user defined':
        print('Good')
        Score= Score+1
    else:
        print("Try Next Question")

    Quiz7 = input('Q7. In Which Year Python 3.0 version developed?')
    if Quiz7 == '2008':
        print('Good')
        Score= Score+1
    else:
        print("Try Next Question")

    Quiz8 = input('Q8. What do You Define a Block Of Code in Python Language?')
    if Quiz8.lower() == 'indentation':
        print('Good')
        Score= Score+1
    else:
        print("Try Next Question")

    Quiz9 = input('Q9. What is The method In The Class in python?')
    if Quiz9.lower() == 'function':
        print('Good')
        Score= Score+1
    else:
        print("Try Next Question")

    Quiz10 = input('In Which language is python Written?')
    if Quiz10.upper() == 'C':
        print('Good')
        Score= Score+1
    else:
        print("Try Next Question")
    print(f'Your Total Score = {Score}/10')
else:
 print("Play Next Time")

