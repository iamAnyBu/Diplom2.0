from django.shortcuts import render

from questionnaire.models import Topic


def plan(request):
    article = Topic.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'questionnaire/plan.html', context)