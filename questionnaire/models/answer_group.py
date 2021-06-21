from django.db import models
from django.utils.translation import gettext as _
from .helpers import DateCreatedMixin


class AnswerGroup(DateCreatedMixin,models.Model):
    """
    Модель ответов
    """

    last_name = models.CharField(_("Фамилия"), max_length=150)
    first_name = models.CharField(_("Имя"), max_length=150)
    second_name = models.CharField(
        _("Отчество"), max_length=150, blank=True, null=True, default=""
    )


    class Meta:
        verbose_name = _("Ответ на группу вопросв")
        verbose_name_plural = _("Ответы на группу вопросв")

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.second_name}"

