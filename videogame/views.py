from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import Games, Genres
from .forms import UserForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('welcome')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'authentication/login.html')

def logout(request):
    auth.logout(request)
    messages.info(request, 'Successfully logged out')
    return redirect('login')

# registration will be done using the built-in User model provided by Django
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken, must be unique')
                return redirect('register')
            else:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                         password=password1)
                messages.info(request, 'User was successfully created')
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'register.html')
    '''form = PeopleForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('login')
    else:
        return render(request, 'register.html', {'form': form})'''

    '''if form.password != form.confirm_Password:
        messages.info(request, 'Passwords do not match!')
        return redirect('register')
    else:
        if People.objects.filter(user_name=form.user_name).exists():
            messages.info(request, 'Username is taken, must be unique')
            return redirect('register')
        elif form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})'''

def delete_user(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        user.delete()
        return redirect('users')

    return render(request, 'delete_confirm.html', {'user': user})

def update_user(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('users')
    return render(request, 'user_form.html', {'form': form, 'user': user})

def view_games(request):
    allGames = Games.objects.all()
    # allGenres = Genres.objects.all()

    context = {'games': allGames}
    template = 'index.html'
    return render(request, template, context)

def view_users(request):
    users = User.objects.all()
    context = {'users': users}
    return render(request, 'view_users.html', context)

def welcome(request):
    context = {'name': 'Mark'}
    template = 'Welcome.html'
    return render(request, template, context)