from django.shortcuts import render

def reflex(request):
    return render(request, 'questionnaire/reflex.html')