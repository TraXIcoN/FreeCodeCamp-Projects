# This program figures out the lowest number of coins should be given for change
def main():
    change = get_positive()

    # Converting change to cents
    cents = round(change * 100)

    # Counting the coins
    # Quarters
    quarters = cents // 25
    cents = cents - quarters * 25

    # Dimes
    dimes = cents // 10
    cents = cents - dimes * 10

    # Nickels
    nickels = cents // 5
    cents = cents - nickels * 5

    # Pennies
    pennies = cents // 1

    # Giving change to the user
    if quarters > 0:
        print(f"{quarters} quarters", end=" ")
        
    if dimes > 0:
        print(f",{dimes} dimes", end=" ")

    if nickels > 0:
        print(f",{nickels} nickels", end=" ")

    if pennies > 0:
        print(f",{pennies} pennies", end=" ")

# Creating a get postitive function
def get_positive():
    while True:
        n = float(input("Change owed: "))
        if n > 0:
            break
    return n

# Calling main function
main()
