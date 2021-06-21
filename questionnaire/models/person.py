from django.db import models

class Person(models.Model):
    SecondName = models.CharField(max_length=50)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Client = models.ForeignKey("Client", on_delete=models.CASCADE)
    Position = models.ForeignKey('Position', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.SecondName)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Физ.лица"