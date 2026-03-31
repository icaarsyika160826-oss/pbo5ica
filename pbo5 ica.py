class BankAccount:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def deposit(self, jumlah):
        self.saldo += jumlah

    def withdraw(self, jumlah):
        if jumlah > self.saldo:
            raise ValueError("Saldo tidak cukup")
        self.saldo -= jumlah

    def get_balance(self):
        return self.saldo

    import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_deposit(self):
        acc = BankAccount(100)
        acc.deposit(50)
        self.assertEqual(acc.get_balance(), 150)

    def test_withdraw(self):
        acc = BankAccount(100)
        acc.withdraw(50)
        self.assertEqual(acc.get_balance(), 50)

    def test_withdraw_gagal(self):
        acc = BankAccount(100)
        with self.assertRaises(ValueError):
            acc.withdraw(200)

if __name__ == "__main__":
    unittest.main()