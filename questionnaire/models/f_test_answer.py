from django.db import models

class FTestAnswer(models.Model):
    FinishTest = models.ForeignKey('FinishTest', on_delete=models.CASCADE)
    FVarAnswer = models.ForeignKey('FVarAnswer', on_delete=models.CASCADE)
    FQuestion = models.ForeignKey('FQuestion', on_delete=models.CASCADE)
    FResult = models.ForeignKey('FResult', on_delete=models.CASCADE)