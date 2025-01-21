from django import forms

class UserRegister(forms.Form):
    login = forms.CharField(max_length=30, label='Введите логин')
    password = forms.CharField(min_length=8, label='Введите пароль')
    second_password = forms.CharField(min_length=8, label='Введите пароль')
    name = forms.CharField(label='Введите имя')
    age = forms.IntegerField(max_value=999)
    phone = forms.IntegerField(max_value=89999999999, label='Введите телефон')
