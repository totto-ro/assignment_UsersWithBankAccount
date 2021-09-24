from BankAccount import BankAcount

class User:
    def __init__(self, firstName):
        self.firstName = firstName
        self.account = {
            "Savings" : BankAcount (.005, 0 ),
            "OtherSavings" : BankAcount (.02, 0 )
        }

    def printInfo( self ):
        print( f"OtherSavings Account\nUser: {self.firstName}, Balance: {self.account['OtherSavings'].yieldInterest().accountInfo()}")
        print( f"Savings Account:\nUser: {self.firstName}, Balance: {self.account['Savings'].yieldInterest().accountInfo()}")
        return self
    

