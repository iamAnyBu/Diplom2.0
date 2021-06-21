from django.shortcuts import render

from questionnaire.models import Topic


def plan_p(request):
    article = Topic.objects.filter(Name='Python. Основы языка программирования')
    context = {
        'articles': article
    }
    return render(request, 'questionnaire/plan_p.html', context)