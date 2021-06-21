from django.db import models

class Topic(models.Model):
    Name = models.CharField(max_length=80)
    Description = models.TextField()
    Level = models.ForeignKey('Level', on_delete=models.CASCADE)
    Image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return str(self.Name)

    class Meta:
        verbose_name = "Тема"
        verbose_name_plural = "Темы"