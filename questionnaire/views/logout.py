from django.shortcuts import render, redirect

from questionnaire.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login as dj_login, logout as log

def logout(request):
    log(request)
    return redirect('base')