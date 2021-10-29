from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Event(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    datetime = models.DateTimeField()
    priority = models.IntegerField(
        validators=[
            MaxValueValidator(999),
            MinValueValidator(1)
        ]
    )

    STATUS_CHOICES = [
        (0, 'todo'),
        (1, 'in progress'),
        (2, 'done'),
    ]
    status = models.IntegerField(
        default=0,
        choices=STATUS_CHOICES,
    )

    def __repr__(self):
        return self.name
