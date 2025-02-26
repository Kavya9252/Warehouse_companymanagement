from django.db import models

class Company(models.Model):
    company_id = models.CharField(max_length=50, unique=True)
    company_name = models.CharField(max_length=100)
    company_address = models.TextField()

    def __str__(self):
        return self.company_name
