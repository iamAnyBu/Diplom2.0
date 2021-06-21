from django.db import models
from django.utils.translation import gettext as _
from .helpers import NameRequiredMixin, PublishedMixin


class Questionnaire(NameRequiredMixin, PublishedMixin, models.Model):
    """
    Модель группы вопросов
    """

    slug = models.SlugField(_("Ссылка на группу вопросов"))

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Группа вопросов'
        verbose_name_plural = 'Группы вопросов'