from django.shortcuts import render

def empl(request):
    return render(request, 'questionnaire/empl.html')
