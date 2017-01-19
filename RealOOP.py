class BankAccount:
  def __init__(self):
    self.balance = 0

  def withdraw(self, amount):
    self.balance -= amount
    return self.balance

  def deposit(self, amount):
    self.balance += amount
    return self.balance

  def make_account():
    return {'balance': 0}

  def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

  def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']
  
class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print 'Sorry, minimum balance must be maintained.'
        else:
            BankAccount.withdraw(self, amount)
