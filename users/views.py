from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    
    form = AuthenticationForm()
    return render(request=request, template_name='users/sign_in.html', context={
        'form': form,
    })


def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request=request, user=user)
            return redirect('home')
    
    form = UserCreationForm()
    return render(request=request, template_name='users/sign_up.html', context={
        'form': form
    })
