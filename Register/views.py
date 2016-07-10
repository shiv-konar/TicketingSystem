from django.shortcuts import render
from .forms import RegisterForm
# Create your views here.


def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save(commit=True)

    context = {
        "form" : form
    }
    return render(request, 'register.html', context)