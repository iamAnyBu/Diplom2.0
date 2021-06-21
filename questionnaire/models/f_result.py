from django.db import models

class FResult(models.Model):
    Finished = models.BooleanField()

    def __str__(self):
        return str(self.Finished)