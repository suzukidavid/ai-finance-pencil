from django.db import models


class Expenses(models.Model):
    TYPE_CHOICES = [
        ('parents', 'Giving Parents'),
        ('wife', 'Giving Wife Pocket Money'),
        ('self', 'My own Pocket Money'),
        ('utility', 'utility bills'),
        ('saving', 'Saving'),
        ('tour', 'Saving for Tour'),
        ('medical', 'Saving for Medical Staff'),
        ('external', 'Saving for External Costs like Restaurant or Other'),
        ('donation', 'Donation'),
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_made = models.DateField()

    def __str__(self):
        return f'{self.type}: {self.amount}'
