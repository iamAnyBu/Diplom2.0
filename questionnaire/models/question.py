from django.db import models
from django.utils.translation import gettext as _


class Question(models.Model):
    """
    Вопрос
    """

    questionnaire = models.ForeignKey(
        "questionnaire.Questionnaire",
        verbose_name=_("Группа вопросов"),
        on_delete=models.CASCADE,
        related_name="questions",
    )
    text = models.TextField(
        verbose_name=_("Текст вопроса")
    )

    def __str__(self):
        return f"{self.text}"

    class Meta:
        verbose_name = 'Вопросов'
        verbose_name_plural = 'Вопросы'