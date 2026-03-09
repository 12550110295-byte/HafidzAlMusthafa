import unittest

# =========================
# CLASS BANK ACCOUNT
# =========================
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError("Jumlah deposit harus lebih dari 0")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Saldo tidak cukup")
        self.balance -= amount
        return self.balance

    def check_balance(self):
        return self.balance


# =========================
# CONTOH PENGGUNAAN PROGRAM
# =========================
def main():
    print("=== SIMULASI BANK ACCOUNT ===")

    account1 = BankAccount("Hafidz", 1000)

    print("Pemilik:", account1.owner)
    print("Saldo awal:", account1.check_balance())

    account1.deposit(500)
    print("Setelah deposit 500:", account1.check_balance())

    account1.withdraw(300)
    print("Setelah tarik 300:", account1.check_balance())