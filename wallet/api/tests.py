from django.test import TestCase

from api.models import Wallet


class WalletModelTests(TestCase):
    def setUp(self):
        self.wallet = Wallet.objects.create(
            balance=100.00
        )

    def test_balance(self):
        self.assertEqual(self.wallet.balance, 100.00)

    def test_operation_deposit(self):
        self.wallet.deposit(50.00)
        self.assertEqual(self.wallet.balance, 150.00)

    def test_operation_withdraw(self):
        self.wallet.withdraw(50.00)
        self.assertEqual(self.wallet.balance, 50.00)

    def test_operation_deposit_negative(self):
        with self.assertRaises(ValueError) as context:
            self.wallet.deposit(-50.00)
        self.assertEqual(str(context.exception), 'Неверная сумма')

    def test_operation_withdraw_exceed_balance(self):
        with self.assertRaises(ValueError) as context:
            self.wallet.withdraw(200.00)
        self.assertEqual(str(context.exception), 'Недостаточно средств')

    def test_operation_withdraw_negative(self):
        with self.assertRaises(ValueError) as context:
            self.wallet.withdraw(-10.00)
        self.assertEqual(str(context.exception), 'Неверная сумма')

    def test_operation_deposit_zero(self):
        with self.assertRaises(ValueError) as context:
            self.wallet.deposit(0.00)
        self.assertEqual(str(context.exception), 'Неверная сумма')

    def test_operation_withdraw_zero(self):
        with self.assertRaises(ValueError) as context:
            self.wallet.withdraw(0.00)
        self.assertEqual(str(context.exception), 'Неверная сумма')

    def test_balance_not_negative(self):
        self.wallet.withdraw(100.00)
        self.assertEqual(self.wallet.balance, 0.00)
