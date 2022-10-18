from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.validators import validate_email


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts/login.html')

    user = request.POST.get('user')
    password = request.POST.get('password')

    # Checking the authentication of the fields
    user = auth.authenticate(request, username=user, password=password)

    if not user:
        messages.error(request, 'User or password invalids!')
        return render(request, 'accounts/login.html')
    else:
        auth.login(request, user)
        messages.success(request, 'Successfully login!')
        return redirect('email_input')


def logout(request):
    auth.logout(request)
    messages.info(request, 'Você desconectou sua conta! Faça login aqui!')
    return redirect('login')


def register(request):
    if request.method != 'POST':
        return render(request, 'accounts/register.html')

    name = request.POST.get('name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    user = request.POST.get('user')
    password = request.POST.get('password')
    password2 = request.POST.get('password2')

    # Checking if it is empty
    if not name or not last_name or not email or not user or not password or not password2:
        messages.error(request, 'Any field can stay empty!')
        return render(request, 'accounts/register.html')

    # Checking the validity of the fields
    try:
        validate_email(email)
    except:
        messages.error(request, 'Invalid email!')
        return render(request, 'accounts/register.html')

    if len(user) < 6:
        messages.error(request, 'The user field needs to have 6 or more characters!')
        return render(request, 'accounts/register.html')

    if len(password) < 6:
        messages.error(request, 'The password field needs to have 6 or more characters!')
        return render(request, 'accounts/register.html')

    if password != password2:
        messages.error(request, 'The passwords field are not the same!')
        return render(request, 'accounts/register.html')

    # Comparing the user created with others
    if User.objects.filter(username=user).exists():
        messages.error(request, 'This username already exists!')
        return render(request, 'accounts/register.html')

    if User.objects.filter(email=email).exists():
        messages.error(request, 'This email already exists!')
        return render(request, 'accounts/register.html')

    # If everything is right
    messages.success(request, 'Successfully registered! you can login your new account!')
    user = User.objects.create_user(username=user, first_name=name,
                                    last_name=last_name, email=email,
                                    password=password)
    user.save()
    return redirect('login')


