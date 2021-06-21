# from django.db import models
# from django.utils.translation import gettext as _
#
#
# class Vopros(models.Model):
#     """
#     Вопрос
#     """
#
#     voprosi = models.ForeignKey(
#         "voprosi.Voprosi",
#         verbose_name=_("Группа вопросов"),
#         on_delete=models.CASCADE,
#         related_name="voprosii",
#     )
#     text = models.TextField(
#         verbose_name=_("Текст вопроса")
#     )
#
#     def __str__(self):
#         return f"{self.text}"
#
#     class Meta:
#         verbose_name = 'Вопросов2'
#         verbose_name_plural = 'Вопросы2'