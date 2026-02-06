class bank:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposite(self,amount):
        self.balance+=amount
        print("balance:",self.balance)
    def with_draw(self,amount):
        self.balance-=amount
        print("balance:",self.balance)
    def account_detailes(self):
        print("Account_holder:",self.account_holder)
        print("Account_balance:",self.balance)
class savings(bank):
    def __init__(self,account_holder,balance):
        super().__init__(account_holder,balance)
    def add_interest(self):
        interest=self.balance*0.05
        self.balance=self.balance+interest
        print("Interest is:",interest)
class current(bank):
    def __init__(self,account_holder,balance,overlimit):
        super().__init__(account_holder,balance)
        self.overlimit=overlimit
    def withdraw_overlimit(self, amount):
        if amount<self.balance+self.overlimit:
            self.balance-=amount
            print("OverLimit:",self.overlimit)
        else:
            print("invalid overlimit")
obj=savings("nisarga",1000)
obj.account_detailes()
obj.deposite(200)
obj.with_draw(100)
obj.add_interest()
obj.account_detailes()
print("------------------------------")
obj1=current("nisarga",3000,2000)
obj1.account_detailes()
obj1.deposite(500)
obj1.with_draw(2000)
obj1.withdraw_overlimit(2000)