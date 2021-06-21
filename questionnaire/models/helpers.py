from django.db import models
from django.utils.translation import gettext as _


class NameRequiredMixin(models.Model):
    """
    Name Mixin;
    Required to fill;
    Contain 'name' field;
    Обязательно к заполнению
    Содержит поле 'Имя'
    """

    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
    )

    class Meta:
        abstract = True


class NameMixin(models.Model):
    """
    Name Mixin;
    Contain 'name' field;
    Содержит поле 'Наименование'
    """

    name = models.CharField(
        verbose_name=_("Наименование"), max_length=125, blank=True, null=True
    )

    class Meta:
        abstract = True


class NameMixin(models.Model):
    """
    Name Mixin;
    Contain 'name' field;
    Содержит поле 'Наименование'
    """

    name = models.CharField(
        verbose_name=_("Наименование"), max_length=125, blank=True, null=True
    )

    class Meta:
        abstract = True


class ShortNameMixin(models.Model):
    """
     Short Name Mixin;
    Contain 'short_name' field;
    Содержит поле 'short_name' - (Краткое наименование)
    """

    short_name = models.CharField(
        verbose_name=_("Краткое наименование"), max_length=125, blank=True, null=True
    )

    class Meta:
        abstract = True


class DescriptionMixin(models.Model):
    """
    Description Mixin;
    Contain 'description' field;
    Содержит поле 'description' - (Описание)
    """

    description = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )

    class Meta:
        abstract = True


class OrderMixin(models.Model):
    """
    Order Mixin;
    Contains 'order' field;
    Содержит поле 'order' - (Сортировка)
    """

    order = models.PositiveIntegerField(verbose_name=_("Order"),blank=True, null=True)

    class Meta:
        abstract = True


class DateCreatedMixin(models.Model):
    """
    Date Created Mixin;
    Contains 'date_created' field;
    Содержит поле 'date_created' - (Дата Создания)
    """

    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class DateUpdatedMixin(models.Model):
    """
    Date Updated Mixin;
    Contains 'date_updated' field;
    Содержит поле 'date_updated' - (Дата последнего обновления)
    """

    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PublishedMixin(models.Model):
    """
    Published Mixin;
    Contains 'is_published' field;
    Содержит поле 'is_published' - (Опубликовано на сайте)
    """

    is_published = models.BooleanField(_("Опубликовано на сайте"), default=False)

    class Meta:
        abstract = True