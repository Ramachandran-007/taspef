from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    subscription = models.DecimalField(max_digits=10, decimal_places=2)
    joining_date = models.DateField()
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.designation}"
