
from django.shortcuts import render, redirect

from questionnaire.forms import UserLoginForm, UserRegisterForm


def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserRegisterForm()
    return render(request, 'questionnaire/registration.html', {"form": form})