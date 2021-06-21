from django.contrib import admin
from .models import Questionnaire, AnswerGroup, Answer, Question#, Vopros, Voprosi, Otvet, OtvetGroup

from .models import Client
from .models import Person
from .models import Position
from .models import Department
from .models import Topic
from .models import Level
from .models import Program
from .models import FinishTest
from .models import FTestAnswer
from .models import FQuestion
from .models import FVarAnswer
from .models import FResult

class QuestionInline(admin.TabularInline):
    model = Question


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    """
    Группа вопросов
    """

    list_display = ("name", "slug", "is_published")
    inlines = (QuestionInline,)


class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(AnswerGroup)
class AnswerGroupAdmin(admin.ModelAdmin):
    """
    Группа ответов
    """

    list_display = ("last_name", "first_name", "second_name", "date_created")
    inlines = (AnswerInline,)


###################################################################################################

# class VoprosInline(admin.TabularInline):
#     model = Vopros
#
#
# @admin.register(Voprosi)
# class VoprosiAdmin(admin.ModelAdmin):
#     """
#     Группа вопросов
#     """
#
#     list_display = ("name", "slug", "is_published")
#     inlines = (VoprosInline,)
#
#
# class OtvetInline(admin.TabularInline):
#     model = Otvet
#
#
# @admin.register(OtvetGroup)
# class OtvetGroupAdmin(admin.ModelAdmin):
#     """
#     Группа ответов
#     """
#
#     list_display = ("last_name", "first_name", "second_name", "date_created")
#     inlines = (OtvetInline,)

########################################################################################################

admin.site.register(Client)
admin.site.register(Person)
admin.site.register(Position)
admin.site.register(Department)
admin.site.register(Topic)
admin.site.register(Level)
admin.site.register(Program)
admin.site.register(FinishTest)
admin.site.register(FTestAnswer)
admin.site.register(FQuestion)
admin.site.register(FVarAnswer)
admin.site.register(FResult)