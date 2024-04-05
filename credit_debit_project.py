# CREATING BANK DETAILS 
class bank_details:
    def __init__(self,name,balance,acc_no):
        self.bankname=name
        self.balance=balance
        self.acc_no=acc_no

    def credit(self,amount):
        self.balance+=amount
        print(c1.bankname,"acc number :",c1.acc_no,"your amount was credited :",amount)
        print("total balance :",self.get_balance())

    def debit(self,amount):
        self.balance-=amount
        print(c1.bankname,"acc number",c1.acc_no,"your amount was debited :",amount)
        print("total balance :",self.get_balance())

    def get_balance(self):
        return self.balance

c1=bank_details("PNB",10000,146010611213)
c1.credit(1000)
c1.debit(500)
