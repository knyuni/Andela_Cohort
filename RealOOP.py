class Bank():
  def deposit():
    pass
  
  def deposit():
    pass
  
class Mshwari(Bank):
  def __init__(self):
    self.balance = 1000
    
  
  def deposit(self,deposit):
    if type(deposit) == int and deposit !="":
      if deposit >= 0:
        self.balance += deposit
        return self.balance

      else:
        return 'Invalid Amount'

    else:
      raise ValueError()

  def withdraw(self,amount):
    if type(amount) == int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:
          if (self.balance -amount) > 1000:
            self.balance-=amount
            return self.balance
          else:
            return 'Insufficient funds in Account'
        else:
          return 'Enter Amount below Actual balance'
      else:
        return 'Invalid Amount'
    else:
      raise ValueError()
      
class CurrentAccount(Bank):
  def __init__(self):
    self.balance = 0
    
  
  def deposit(self,deposit):
    if type(deposit) == int and deposit !="":
      if deposit >= 0:
        self.balance += deposit
        return self.balance

      else:
        return 'Invalid deposit amount'

    else:
      raise ValueError()

  def withdraw(self,amount):
    if type(amount) ==  int and amount != "":
      if amount > 0:
        if (self.balance-amount) > 0:

          self.balance-=amount
          return self.balance

        else:
          return 'Enter Amount below Actual balance'
      else:
        return 'Invalid withdraw amount'
    else:
raise ValueError()