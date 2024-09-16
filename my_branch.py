
# Variables
# display_again = input("Redisplay menu? (y/n) ")
# main_menu = input("Return to main menu? (y/n)")
# Needs to be product price
item_price = 150

# Prompts the user to redisplay menu and complete purchase
# if "y" in display_again:
#     print("Redisplay menu")
# elif "n" in display_again:
#     print("Proceed to checkout")

# Prompts the user to select a payment type
payment_type = input("Cash, Credit, or Check? ")
if "cash" in payment_type:
    print("Cash")
    cash_amount = float(input("Enter cash amount: $"))
    # Checks to see if amount paid is over or under the item price
    if item_price < cash_amount:
        change = cash_amount - item_price
        print(f"Your change: ${change}")
    elif item_price > cash_amount:
        print("Insufficient funds, please try again.")
        payment_type = input("Cash, Credit, or Check? ")
elif "credit" in payment_type:
    print("Credit")
    card_number = int(input("Enter card number: "))
    expiration = int(input("Enter expiration date: "))
    cvv = int(input("Enter CVV: "))
elif "check" in payment_type:
    print("Check")
    check_number = int(input("Enter check number"))


# Function displays receipt
def display_receipt():
    print("Total is: ")
    print("Payment info: ")
    if "cash" in payment_type:
        print(f"Cash amount used: ${cash_amount}")
    elif "credit" in payment_type:
        print(f"Card number used: {card_number}")
    elif "check" in payment_type:
        print(f"Check number used: {check_number}")


# display_receipt()

