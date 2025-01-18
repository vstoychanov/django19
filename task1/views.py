from django.shortcuts import render
from .forms import UserRegister
from .models import Buyer
from .models import Game
from django.http import HttpResponse

def main_page(request):
    title = 'Главная страница'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {
        'title': title,
        'cart': cart,
        'shop': shop
    }
    return render(request, 'fourth_task/main_page.html', context)

def second_page(request):
    title = 'Игры'
    shop = 'Магазин'
    cart = 'Корзина'
    games = Game.objects.all()
    buy = 'Купить'
    back = 'Вернуться'
    contex = {
        'title': title,
        'games': games,
        'buy': buy,
        'back': back,
        'shop': shop,
        'cart': cart
    }
    return render(request, 'fourth_task/second_page.html', contex)

def third_page(request):
    title= 'Корзина'
    back = 'Вернуться'
    shop = 'Магазин'
    cart = 'Корзина'
    context = {
        'title': title,
        'back': back,
        'cart': cart,
        'shop': shop
    }
    return render(request, 'fourth_task/third_page.html', context)


def sign_up_by_django(request):
    form = UserRegister(request.POST)
    info = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            buyers = Buyer.objects.all()
            exesting_username = [buyer.name for buyer in buyers]

            if username in exesting_username:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            else:
                Buyer.objects.create(name=username, age=age, balance=0.00)
                return render(request, 'fifth_task/registration_page.html',
                              {'message': f'Приветствуем, {username}!'})

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        buyers = Buyer.objects.all()
        exesting_username = [buyer.name for buyer in buyers]

        if username  in exesting_username:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        else:
            Buyer.objects.create(name=username, age=age, balance=0.00)
            return render(request, 'fifth_task/registration_page.html',
                          {'message': f'Приветствуем, {username}!'})

    return render(request, 'fifth_task/registration_page.html', info)