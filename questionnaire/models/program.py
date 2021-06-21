from django.db import models

class Program(models.Model):
    Name = models.CharField(max_length=80)
    Level = models.ForeignKey('Level', on_delete=models.CASCADE)
    Topic = models.ManyToManyField('Topic')
    Person = models.ManyToManyField('Person')
    FinishTest = models.OneToOneField('FinishTest', on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name = "Программа"
        verbose_name_plural = "Программы"