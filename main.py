MAX_LINES=3
MAX_BET=100
MIN_BET=1





def deposit():
    while True:
        amount= input("Enter the amount you want to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("The value must be greater than 0.")
        else:
            print("Enter the number")

    return amount

def get_number_of_lines():
    while True:
        lines= input(
            "Enter the number of lines(1-" + str{MAX_LINES} + ")? $")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("The value must be between {MAX_LINES} than 0.")
        else:
            print("Enter the number")

    return lines

def get_bet():
    while True:
        amount= input("Enter the amount you want to bet on each line? $")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"The value must between {MIN_BET} - {MAX_BET}.")
        else:
            print("Enter the number")

    return amount


def main():
    balance=deposit()
    lines=get_number_of_lines()
    bet=get_bet()
    total_bet=bet*lines
    print("")
            
            