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