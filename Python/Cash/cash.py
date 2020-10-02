#this program figures out the lowest number of coins should be given for change

def main():
    change = get_positive()

    # converting change to cents
    cents = round(change * 100)

    # counting the coins
    # quaters
    quaters = cents // 25
    cents = cents - quaters * 25

    # dimes
    dimes = cents // 10
    cents = cents - dimes * 10

    #nickels
    nickels = cents // 5
    cents = cents - nickels * 5

    # pennies
    pennies = cents // 1

    # giving a change to user
    if quaters > 0:
        print(f"{quaters} quaters", end=" ")
        
    if dimes > 0:
        print(f",{dimes} dimes", end=" ")

    if nickels > 0:
        print(f",{nickels} nickels", end=" ")

    if pennies > 0:
        print(f",{pennies} pennies", end=" ")

# creating a get postitive function
def get_positive():
    while True:
        n = float(input("Change owed: "))
        if n > 0:
            break
    return n

# calling main function
main()