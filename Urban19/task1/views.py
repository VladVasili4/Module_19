from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse
from .models import *


def index_reg(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Получаем всех покупателей
            existing_buyers = Buyer.objects.values_list('name', flat=True)

            if password != repeat_password:
                info['error'] = "Пароли не совпадают"
            elif age < 18:
                info['error'] = "Вы должны быть старше 18"
            elif username in existing_buyers:
                info['error'] = "Пользователь уже существует"
            else:
                # Создаем нового покупателя
                Buyer.objects.create(name=username, balance=0.00, age=age)
                info['welcome_message'] = f"Приветствуем, {username}!"  

        info['form'] = form
    else:
        form = UserRegister()
        info['form'] = form

    return render(request, 'registration_page.html', context=info)


def index(request):
    title = 'Games'
    my_buyers = Buyer.objects.all()
    context = {
        'title': title,
        'my_buyers': my_buyers,
    }
    return render(request, 'platform.html', context)


def index_game(request):
    games_all = Game.objects.all()
    return render(request, 'games.html', context={'games_menu': games_all})


def index_cart(request):
    title = 'Cart'
    context = {
        'title': title,
    }
    return render(request, 'cart.html', context)


