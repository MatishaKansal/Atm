class Atm :
    def __init__(self, atm_card_number, pin_number):
         self.atm_card_number = atm_card_number
         self.pin_number = pin_number

    def CashWithdrawl(self):
        print("Withdraw your cash")

    def BalanceEnquiry(self):
        print("Check your balance in your account")


Axis = Atm(123321123, 321)
print(Axis.CashWithdrawl())
print(Axis.BalanceEnquiry())