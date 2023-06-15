from django.db import models

# Create your models here.


class Prediction(models.Model):
    PREDICT_OPTIONS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]

    temp_max = models.DecimalField(decimal_places=2, max_digits=4)
    temp_min = models.DecimalField(decimal_places=2, max_digits=4)
    wind = models.DecimalField(decimal_places=2, max_digits=4)
    prediction = models.CharField(choices=PREDICT_OPTIONS, max_length=10)