class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def subtract(self):
        return self.first - self.second

    def multiply(self):
        return self.first * self.second

    def divide(self):
        if self.second == 0:
            return 'Error!Not divisible by zero!'
        else:
            return self.first / self.second


while True:
    print('---------------------')
    print('Welcome to Calculator')
    print('---------------------')
    print('1. Add ')
    print('2. Subtract ')
    print('3. Multiply ')
    print('4. Divide')
    print('5. Exit')
    print('---------------------')

    try:
        choice = int(input('Enter your choice (1-5): '))
    except ValueError:
        print('!!!!')
        print('Please enter a NUMBER between 1 and 5.')
        continue

    if choice == 5:
        print('Bye!')
        break

    if choice < 1 or choice > 5:
        print('Invalid choice! Please enter a number between 1 and 5.')
        continue

    try:
        first = int(input('Enter the first number: '))
        second = int(input('Enter the second number: '))
    except ValueError:
        print('!!!!')
        print('Please enter a valid number.')
        continue

    calculator = Calculator(first, second)

    if choice == 1:
        print(f'Result : {calculator.add()}')
    elif choice == 2:
        print(f'Result : {calculator.subtract()}')
    elif choice == 3:
        print(f'Result : {calculator.multiply()}')
    elif choice == 4:
        print(f'Result : {calculator.divide()}')
