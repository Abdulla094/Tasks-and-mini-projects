# Make LENA BANK with withdraw deposit accNumber BAlance holdername type 
#also have mini statements(last 5 transaction) and account summary(all transaction)
import random as r

class Lenabank():
    def _init_(self):
        print("Welcome to lena bank\t")
        self.name=input("Enter your name\t")
        self.balance=int(input("Enter your initial balance\t"))
        self.accNumber=r.randint(100,999)
        self.type="Savings"
        self.summary=[]
        

        
    def deposit(self):
        print("Deposit")
        self.Damount=int(input("Enter the amount to deposit"))
        if self.Damount<=20000:
            print("Amount deposited",self.Damount)
            self.balance=self.balance+self.Damount
            print("your new balance is",self.balance)
            self.summary.append(self.Damount)
        else:
            print("you cannot deposit more than 20000")
    
    def withdraw(self):
            print("withdraw")
            self.Wamount=int(input("Enter the amount to withdraw"))
            if self.Wamount>=10000:
                print("you cannot withdraw more than 10000")
            elif self.Wamount>self.balance:
                print("withdraw failed you don't have enough funds")
            else:
                print("withdraw successful",self.Wamount)
                self.balance=self.balance-self.Wamount
                print("your new balance is",self.balance)
                self.summary.append(self.Wamount)
    def printSummary(self):
        print("Summary")
        self.summary.reverse()
        print(self.summary)

    def display(self):
        print("DETAILS")
        print("Name : " + self.name)
        print("Balance : ",self.balance)
        print("ACCOUNT NUMBER : ",self.accNumber)
        print("TYPE : "+self.type)


        
        
            
abd=Lenabank()
print("-----------------------------------------")
abd.display()
print("-----------------------------------------")
abd.deposit()
print("-----------------------------------------")
abd.deposit()
print("-----------------------------------------")
abd.display()
print("-----------------------------------------")
abd.withdraw()
print("-----------------------------------------")
abd.withdraw()
print("-----------------------------------------")
abd.withdraw()
print("-----------------------------------------")
abd.display()
abd.printSummary()