class BankAccount:
    def __init__(self, id):
        self.id = id
        self.balance = 0

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        return False

    def deposit(self, amount):
        self.balance += amount
        return True


my_account = BankAccount(1)
my_account.deposit(100)
print(my_account.balance)


def test_insufficient_deposit():
    # Arrange
    a = BankAccount(1)
    a.deposit(100)
    # Act
    outcome = a.withdraw(200)
    # Assert
    assert outcome == False


def test_negative_deposit():
    # Arrange
    a = BankAccount(1)
    # Act
    outcome = a.deposit(-100)
    # Assert
    assert outcome == True
