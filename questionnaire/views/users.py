from django.shortcuts import render, redirect

from questionnaire.models import AnswerGroup


def users(request):
    article = AnswerGroup.objects.all()
    context = {
        'articles': article
    }
    return render(request,'questionnaire/users.html', context)