class Purchase:
    def __init__(self, cash_amount, card_number, expiration, cvv, check_number):
        self.cash_amount = cash_amount
        self.card_number = card_number
        self.expiration = expiration
        self.cvv = cvv
        self.check_number = check_number

    def payment_info(self):
        payment_type = input(
            "How would you like to pay?\nEnter 'Cash', 'Credit', 'Check', or 'Return' to return to menu: ")

        if payment_type.lower() == 'cash':
            cash_amount = float(input("Enter cash amount: $"))
            # Checks to see if amount paid is over or under the item price
            # if item_price < cash_amount:
            #     change = cash_amount - item_price
            #     print(f"Your change: ${change}")
            # elif item_price > cash_amount:
            #     print("Insufficient funds, please try again.")
            #     payment_type = input("Cash, Credit, or Check? ")
        elif payment_type.lower() == 'credit':
            card_number = int(input("Enter card number: "))
            expiration = int(input("Enter expiration date: "))
            cvv = int(input("Enter CVV: "))
        elif payment_type.lower() == 'check':
            check_number = int(input("Enter check number"))
        elif payment_type.lower() == 'return':
            main()

        redisplay_menu()
