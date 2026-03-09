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


# =========================
# UNIT TESTING
# =========================
class TestBankAccount(unittest.TestCase):

    def test_deposit(self):
        account = BankAccount("Hafidz", 1000)
        account.deposit(500)
        self.assertEqual(account.balance, 1500)

    def test_withdraw(self):
        account = BankAccount("Hafidz", 1000)
        account.withdraw(200)
        self.assertEqual(account.balance, 800)

    def test_withdraw_too_much(self):
        account = BankAccount("Hafidz", 1000)
        with self.assertRaises(ValueError):
            account.withdraw(2000)


# =========================
# MENJALANKAN PROGRAM
# =========================
if __name__ == "__main__":
    main()

    print("\n=== MENJALANKAN UNIT TEST ===")
    unittest.main(argv=['first-arg-is-ignored'], exit=False)