from django.db import models

class FVarAnswer(models.Model):
    Name = models.CharField(max_length=80)
    FQuestion = models.ForeignKey('FQuestion', on_delete=models.CASCADE)
    Point = models.IntegerField()

    def __str__(self):
        return self.Name