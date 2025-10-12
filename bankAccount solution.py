# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 14:15:40 2025

@author: Moreblessing
"""

class BankAccount:
    
    def __init__(self):# default constructor
      
        self.balance=0 #private variable
        
    def deposit(self,amount):# deposit function
        if amount>0:
            self.balance+=amount
            print(f"a deposit of {amount} was successful" )
        else:
            self.balance+=0
            print('Invalid amount')
    
    def withdraw(self,amount):#witdraw function
        if self.balance>amount: # checking for sufficient balance
            self.balance-=amount
            print(f"a Withdrawal of {amount} was successful" )
        else:
            print("YOU you have insufficient funds. Check your balance")
    def diplay_balance(self):
        print('Your balance is: ', self.balance)
        



account =BankAccount() # creating the account object

while True: # test code in a loop
  print("Pease what you want to do\n 1- Deposit\n 2-withdraw \n 3-check balance \n 0 to quit") 
  choice=int(input("MY ACTION: "))  
  if choice ==1:  
    print('==========You making a deposit========')
    amount=float(input("Enter amount to deposit"))
    account.deposit(amount)
    account.diplay_balance()
    
  elif choice==2:
        
      amount=float(input("Enter amount to withdraw"))
      account.withdraw(amount)
  elif choice==3:
      account.diplay_balance()
  else:
      print('Good Bye')
      break