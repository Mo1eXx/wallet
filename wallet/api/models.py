import uuid
from django.db import models


class Wallet(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00
    )

    def __str__(self):
        return f'Wallet {self.id} - Balance: {self.balance}'

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Неверная сумма')
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError('Неверная сумма')
        if self.balance < amount:
            raise ValueError('Недостаточно средств')
        self.balance -= amount
        self.save()
