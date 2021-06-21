from django.db import models

class Position(models.Model):
    Name = models.CharField(max_length=50)
    Department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"