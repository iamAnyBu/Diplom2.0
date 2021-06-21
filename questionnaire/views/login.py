from django.shortcuts import render, redirect

from questionnaire.forms import UserLoginForm, UserRegisterForm
from django.contrib.auth import login as dj_login, logout as log


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            dj_login(request, user)
            return redirect('whoau')
    else:
        form = UserLoginForm()
    return render(request, 'questionnaire/login.html', {"form": form})
