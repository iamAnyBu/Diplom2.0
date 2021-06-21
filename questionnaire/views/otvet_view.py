# from django.views.generic import View
# from django.shortcuts import render
# from ..models import Voprosi, OtvetGroup, Otvet
#
#
# class SaveOtvetView(View):
#     template_name = "questionnaire/otvet_view.html"
#     model = Voprosi
#
#     def get(self, request, *args):
#
#         return render(
#             request,
#             self.template_name,
#             {"voprosi": self.get_voprosi_object()},
#         )
#
#     def post(self, request, *args):
#         voprosi = self.get_voprosi_object()
#         self.save_otvet_group(voprosi, request.POST)
#         return render(request, self.template_name, {"voprosi": voprosi})
#
#     def get_voprosi_object(self):
#         return self.model.objects.get()
#
#     def save_voprosi_group(self, voprosi, request_post):
#         """
#         Сохранение ответов в базу
#         """
#         otvet_group = OtvetGroup.objects.create(
#             last_name=request_post["last_name"],
#             first_name=request_post["first_name"],
#             second_name=request_post["second_name"],
#         )
#         otveti = []
#         for vopros in voprosi.voprosii.all():
#             key_vopros = "vopros_" + str(vopros.pk)
#             otveti.append(
#                 Otvet(
#                     otvet_group=otvet_group,
#                     vopros=vopros,
#                     value=int(request_post.get(key_vopros)),
#                 )
#             )
#
#         Otvet.objects.bulk_create(otveti)
