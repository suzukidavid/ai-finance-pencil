from django.db import models


class Income(models.Model):
    SOURCE_CHOICES = [
        ('salary', 'Salary'),
        ('freelance', 'Freelance Work'),
        ('other', 'Other'),
    ]

    source = models.CharField(max_length=50, choices=SOURCE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_received = models.DateField()

    def __str__(self):
        return f'{self.source}: {self.amount}'
