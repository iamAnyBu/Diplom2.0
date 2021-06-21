from django.views.generic.list import ListView
from ..models import Questionnaire

class QuestionnaireListView(ListView):


    model = Questionnaire
    context_object_name = 'questionnaires'
    template_name='questionnaire/questionnaire-list-view.html'

    def get_queryset(self):
        """
        Вывод только обуликованных групп вопросов
        """

        return self.model.objects.filter(is_published=True)