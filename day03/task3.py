user_input=int(input("Enter the year :"))

if user_input%4==0:
    if user_input%100==0:
        if user_input%400==0:
            print("{} is a LEAP YEAR".format(user_input))
        else:
            print("{} is not a LEAP YEAR".format(user_input))
    else:
        print("{} is a LEAP YEAR".format(user_input))        
else:
    print("{} is not a LEAP YEAR".format(user_input))