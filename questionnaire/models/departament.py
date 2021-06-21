from django.db import models

class Department(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"