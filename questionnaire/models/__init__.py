from .answer_group import AnswerGroup
from .answer import Answer
from .answer_enum import AnswerEnum
from .questionnaire import Questionnaire
from .question import Question
# from .otvet_group import OtvetGroup
# from .otvet_test import Otvet
# from .otvet_num import OtvetNum
# from .voprosi_test import Voprosi
# from .vopros_test import Vopros
from .client import Client
from .departament import Department
from .position import Position
from .person import Person
from .level import Level
from .topic import Topic
from .finish_test import FinishTest
from .f_question import FQuestion
from .f_var_answer import FVarAnswer
from .f_result import FResult
from .f_test_answer import FTestAnswer
from .program import Program

# Список публичных компонетов модуля
__all__ = [
    "AnswerGroup",
    "Answer",
    "AnswerEnum",
    "Questionnaire",
    "Question",
    "Client",
    "Department",
    "Position",
    "Person",
    "Level",
    "Topic",
    "FinishTest",
    "FQuestion",
    "FVarAnswer",
    "FResult",
    "FTestAnswer",
    "Program",


    # "OtvetGroup",
    # "Otvet",
    # "OtvetNum",
    # "Voprosi",
    # "Vopros",

]