from django.shortcuts import render, redirect

def whoau(request):
    return render(request, 'questionnaire/whoau.html')

