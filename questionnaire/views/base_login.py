from django.shortcuts import render, redirect

def base_login(request):
    return render(request, 'questionnaire/base_login.html')
