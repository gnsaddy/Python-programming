import sys

class Customer:
    '''Customer class with related details'''
    bankName = "UKO Bank"

    def __init__(self,name,balance = 0):
        self.name = name
        self.balance = balance

    def deposite(self,amounr):
            self.balance = self.balance+amount
            print("After deposite the balance: ", self.balance)


    def withdraw(self,amount):
            if amount > self.balance:
                print("Insufficinet funds")
                sys.exit()
            self.balance = self.balance-amount
            print("afte withdraw the balance amount :",self.balance)

print("welcome to ", Customer.bankName)

name=input("enter your name:")
c=Customer(name)
while True:
    print('d-Deposite\n w-withdraw \n e-Exit')
    option = input("chose your option:")
    if option == 'd' or option =='D':
        amount = float(input("entr the amount to deposite"))
        c.deposite(amount)


    elif option == 'w' or option == 'W':
        print("how much amount to withdraw")
        amount = float(input("Enter amount to withdraw"))
        c.withdraw(amount)

    elif option == 'e' or option == 'E':
        print("Thanks for Banking")
        sys.exit

    else:
        print("Choose valid option")

