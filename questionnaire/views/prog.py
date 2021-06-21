from django.shortcuts import render

from questionnaire.models import Program


def prog(request):
    article = Program.objects.all()
    context = {
        'articles': article
    }
    return render(request, 'questionnaire/prog.html', context)