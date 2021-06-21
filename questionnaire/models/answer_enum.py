from django.db import models
from django.utils.translation import gettext as _


class AnswerEnum(models.IntegerChoices):
    ICAN = 1, _('Умею')
    WANT = 2, _('Хочу научиться')
    NEEDLESSLY = 3, _('Не востребовано')