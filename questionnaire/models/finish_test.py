from django.db import models

class FinishTest(models.Model):
    Data = models.DateTimeField()
    Number = models.IntegerField()

    def __str__(self):
        return str(self.Number)

    class Meta:
        verbose_name = "Финишный тест"
        verbose_name_plural = "Финишные тесты"