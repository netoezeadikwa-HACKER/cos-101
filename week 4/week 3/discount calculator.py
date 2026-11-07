print("               LOOK HERE FOR DISCOUNT PRICES")
print()
print()
print("NGN10,000 and below:  0%")
print()
print("NGN10,000 - NGN50,000:  5%")
print()
print("NGN50,000 and above:   10%")
print()
print()


amount = float(input("Enter amount you bought: "))

if amount < 10000:
    print("There is no discount for this amount")

    if amount < 50000:
        print("Your discount is 5%")
        discount = (amount * 5)/100
        print(f"Your final amount is: {discount}")


else:
    print("Your discount is 10%")
    discount_2 = (amount * 10)/100
    print(f"Your final amount is: {discount_2}")
















