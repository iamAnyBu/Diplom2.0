# from django.db import models
# from django.utils.translation import gettext as _
# from .helpers import DateCreatedMixin
# from .otvet_num import OtvetNum
#
#
# class Otvet(DateCreatedMixin, models.Model):
#
#     otvet_group = models.ForeignKey(
#         "voprosi.OtvetGroup",
#         verbose_name=_("Вопрос"),
#         on_delete=models.CASCADE,
#         related_name="otvetii",
#     )
#     vopros = models.ForeignKey(
#         "voprosi.Vopros",
#         verbose_name=_("Вопрос"),
#         on_delete=models.CASCADE,
#         related_name="otvetii",
#     )
#     value = models.IntegerField(_("Значение ответа"), choices=OtvetNum.choices)
#
#     def __str__(self):
#         return f"{self.vopros}"
#
#     class Meta:
#         verbose_name = "Ответ группы вопросов2"
#         verbose_name_plural = "Ответы группы вопросов2"