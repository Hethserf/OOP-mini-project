class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.balance * rate
        self.balance += interest
        return interest

account = SavingsAccount('Angel', 0)

while True:
    print('----Bank Account----')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Get balance')
    print('4. Exit')
    print('--------------------')
    print(f'{account.owner} Your current balance is : ${account.get_balance()}')

    try:
        choice = int(input('Choice (1-4): '))
    except ValueError:
        print('Please enter a number.')
        continue

    if choice == 4:
        print('Have a nice day!')
        break

    if choice < 1 or choice > 4:
        print('Please enter a number between 1 and 4.')
        continue

    if choice == 1:
        amount = int(input('Amount to deposit: '))
        account.deposit(amount)
    elif choice == 2:
        amount = int(input('Amount to withdraw: '))
        account.withdraw(amount)
    elif choice == 3:
        print(f'Balance: {account.get_balance()}')
    else:
        print('Please enter a number between 1 and 4.')
