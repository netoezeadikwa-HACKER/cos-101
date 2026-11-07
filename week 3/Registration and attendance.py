print("       THIS IS TO CHECK IF YOUR REGISTRATION AND ATTENDANCE IS COMPLETE ")
print("                =============================================")
print()
print()
print()


registration_status = input("Registration complete? Enter yes or no:   ")

if registration_status == "no":
    print("You cannot participate")

else:
    
    attendance = float(input("Enter attendance percentage:   "))

    if registration_status != "yes" and registration_status !="no":
        print("Invalid response")



    elif attendance < 0 or attendance > 100:
        print("Invalid attendance percentage")

    elif registration_status == "yes" and attendance >= 75:
        print("You may participate in the practical assessment")

    else:
        print("You may not participate in the practical assessment")




















