from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

company_name = '"Лучший выбор"'

def main(request):
    text = ''
    context = {
        'title': 'Главная страница',
        'text': text,
    }
    return render(request, 'main.html', context)

def exampl(request):
    text = (f'В данном разделе вы можете ознакомиться с ранее созданными проектами, созданными дизайнерами компании {company_name}')
    objects = ['Частные дома', 'Бизнесс', 'Рабочие помещения', 'Квартиры']
    context = {
        'title': '',
        'text': text,
        'objects': objects,
    }
    return render(request, 'example.html', context)

def servis(request):
    text = f'Компания {company_name} предоставляет услуги: '
    objects = ['Частные дома', 'Бизнесс', 'Рабочие помещения', 'Квартиры']
    context = {
        'title': 'Услуги',
        'text': text,
        'objects': objects
    }
    return render(request, 'services.html', context)

def registration(request):
    Buyers = Buyer.objects.all()
    info = {'error': None}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            second_password = form.cleaned_data['second_password']
            age = form.cleaned_data['age']

            for buyer in Buyers:
                if login.lower() == buyer.name.lower():
                    info['error'] = 'Данный пользователь уже существует'
                    break
                elif password != second_password:
                    info['error'] = 'Пароли не совпадают'
            if info['error'] == None:
                Buyer.objects.create(email=login, password = password, age=age)
                return HttpResponse(f'Регистрация прошла успешно. Приветствуем, {login}')
    else:
        form = UserRegister()
    context = {
        'Buyers': Buyers,
        'form': form,
        'info': info['error']
    }
    return render(request, 'registration.html', context)

def vhod(request):
    Buyers = Buyer.objects.all()
    info = {'error': None}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']

            for buyer in Buyers:
                if login.lower() == buyer.name.lower():
                    if password == buyer.password:
                        form = UserRegister()
                        return render(request, 'vhod.html', {'Buyers': Buyers, 'form': form, 'info': info['error']})
                    else:
                        info['error'] = 'Пароли не совпадают'
                        break
                else:
                    info['error'] = 'Данного пользователя нет'

    else:
        form = UserRegister()
    context = {
        'Buyers': Buyers,
        'form': form,
        'info': info['error']
    }
    return render(request, 'vhod.html', context)

def contacts(request):
    text = ''

    context = {
        'title': 'Контакты',
        'text': text,
    }
    return render(request, 'contacts.html', context)






