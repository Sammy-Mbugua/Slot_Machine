def deposit():
    while True:
        amount=input("Enter amount you want to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("The value must be greater than 0.")
        else:
            print("Enter a number.")
    return amount

deposit()