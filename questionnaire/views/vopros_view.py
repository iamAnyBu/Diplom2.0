# from django.views.generic.list import ListView
# from ..models import Voprosi
#
# class VoprosiListView(ListView):
#
#
#     model = Voprosi
#     context_object_name = 'voprosiii'
#     template_name= 'questionnaire/vopros_view.html'
#
#     def get_queryset(self):
#         """
#         Вывод только обуликованных групп вопросов
#         """
#
#         return self.model.objects.filter(is_published=True)