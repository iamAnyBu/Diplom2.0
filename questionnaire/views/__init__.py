from .save_answer_view import SaveAnswerView
from .questionnaire_list_view import QuestionnaireListView
from .base import base
from .base_login import base_login
from .empl import empl
from .login import login
from .logout import logout
from .registration import registration
from .shef import shef
from .whoau import whoau
from .reflex import reflex
#from .vopros_view import VoprosiListView
#from .otvet_view import SaveOtvetView
from .users import users

from .plan import plan
from .plan_p import plan_p
from .prog import prog

# Список публичных компонетов модуля
__all__ = ["SaveAnswerView","QuestionnaireListView","base",'base_login','empl','login','logout','registration','shef','whoau', 'reflex', 'users','plan', 'plan_p', 'prog', ]#'VoprosiListView','SaveOtvetView',]
