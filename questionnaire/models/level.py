from django.db import models

class Level(models.Model):
    Name = models.CharField(max_length=30)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"