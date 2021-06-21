from django.urls import include, path

from . import views
from .views import SaveAnswerView, QuestionnaireListView#, SaveOtvetView

urlpatterns = [
    path('', views.base, name='base'),
    path('base_login/',views.base_login, name='base_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('whoau/', views.whoau, name='whoau'),
    path('shef/', views.shef, name='shef'),
    path('empl/', views.empl, name='empl'),
    path("save-answer-view/", SaveAnswerView.as_view(), name="save-answer-view"),
    path("reflex/", views.reflex, name="reflex"),
    path("users/", views.users, name="users"),
    path("plan/", views.plan, name="plan"),
    path("plan_p/", views.plan_p, name="plan_p"),
    path("prog/", views.prog, name="prog"),
    #path("otvet_view/", SaveOtvetView.as_view(), name="otvet_view"),
    #path("", QuestionnaireListView.as_view(), name="questionnaire-list-view"),
]