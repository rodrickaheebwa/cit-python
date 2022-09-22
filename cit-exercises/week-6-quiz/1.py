# create a credit card class with the following attributes: card number, expiration date, and security code. Create a method that will print out the card number, expiration date, and security code. Create an instance of the class and call the method.

class CreditCard:
    def __init__(self, card_number, exp_date, security_code):
        self.card_number = card_number
        self.exp_date = exp_date
        self.security_code = security_code

    def print_card_attributes(self):
        print(f"Card Number: {self.card_number}")
        print(f"Card Expiry Date: {self.exp_date}")
        print(f"Card Security Code: {self.security_code}")

my_card = CreditCard('4215472218458145', 'May 2024', 1234)

my_card.print_card_attributes()