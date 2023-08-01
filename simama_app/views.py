from django.shortcuts import render, redirect
from .models import User, Task
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
import random
from datetime import datetime, timedelta
from django.contrib.auth.decorators import login_required



def get_date_range():
    start_date = datetime(2021, 1, 1)
    end_date = datetime(2023, 7, 31)
    delta = timedelta(days=1)

    date_range = []
    current_date = start_date
    while current_date <= end_date:
        date_range.append(current_date)
        current_date += delta

    return date_range

 
date_range = get_date_range()
print(date_range)

 
def home(request):
    return render(request, 'home.html')


def user_login(request):
    if request.user.is_authenticated:
        return redirect('already_logged_in')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Email atau password salah'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def register(request):
    if request.user.is_authenticated:
        return redirect('already_logged_in')

    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        phone_number = request.POST['phone_number']

        user = User.objects.create_user(username=email, email=email, password=password)
        user.full_name = full_name
        user.save()

        return redirect('login')

    return render(request, 'register.html')


@login_required
def already_logged_in(request):
    return redirect('dashboard')


@login_required
def dashboard(request):
    if Task.objects.count() == 0:
        generate_random_tasks()

    start_date = datetime(2021, 1, 1)
    end_date = datetime(2023, 7, 31)
    min_reward = 9000
    max_reward = 200000

    tasks = Task.objects.filter(
        reward__gte=min_reward,
        reward__lte=max_reward
    ).order_by('name')

    total_reward = sum(task.reward for task in tasks)
    if total_reward > 6213654: 
        tasks = tasks.order_by('-reward')
        for task in tasks:
            total_reward -= task.reward
            if total_reward <= 6213654:
                break

    context = {'tasks': tasks, 'total_reward': total_reward}
    return render(request, 'dashboard.html', context)


@login_required
def edit_profile(request): 
    return render(request, 'edit_profile.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


def generate_random_tasks():
    categories = ['IT', 'Pertanian', 'Kedokteran']
    rewards = [4000, 5000, 10000, 15000, 20000, 25000, 30000, 40000, 50000, 75000, 100000, 150000, 200000, 250000, 500000]
    tasks = []

    for i in range(15):
        name = f'TugasAcak {i+1}'  
        category = random.choice(categories)
        reward = random.choice(rewards)
        task = Task(name=name, category=category, reward=reward)
        tasks.append(task)

    Task.objects.bulk_create(tasks)
