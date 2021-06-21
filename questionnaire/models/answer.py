from django.db import models
from django.utils.translation import gettext as _
from .helpers import DateCreatedMixin
from .answer_enum import AnswerEnum


class Answer(DateCreatedMixin, models.Model):

    answer_group = models.ForeignKey(
        "questionnaire.AnswerGroup",
        verbose_name=_("Вопрос"),
        on_delete=models.CASCADE,
        related_name="answers",
    )
    question = models.ForeignKey(
        "questionnaire.Question",
        verbose_name=_("Вопрос"),
        on_delete=models.CASCADE,
        related_name="answers",
    )
    value = models.IntegerField(_("Значение ответа"), choices=AnswerEnum.choices)

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = "Ответ группы вопросов"
        verbose_name_plural = "Ответы группы вопросов"
