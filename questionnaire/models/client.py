from django.db import models


class Client(models.Model):
    SecondName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=70)

    def __str__(self):
        return self.SecondName

    class Meta:
        verbose_name = "Работодатель"
        verbose_name_plural = "Юр.лица"