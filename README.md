# Дипломная работа 
на тему: 
**“Анализ и сравнение написания web-приложений с использованием разных фреймворков”** 
Выполнил: Кулаков Сергей Иванович

----

## Содержание: 
### 1. Введение
#### 1.1 Обоснование выбранной темы
#### 1.2 Цели дипломной работы
#### 1.3 Задачи дипломной работы
#### 1.4 Основные определения
### 2. Свойства и особенности фреймворков
#### 2.1 Django
#### 2.2 FastAPI  
#### 2.3 Flask
### 3. Примеры написанных программ на Django, Flask и FastAPI
#### 3.1 Пример работы на Django
#### 3.2 Пример работы на Flask
#### 3.3 Пример работы на FastAPI
### 4. Анализ и сравнение работы на Django, Flask и FastAPI
#### 4.1 FLASK - FASTAPI
#### 4.2 DJANGO - FLASK
#### 4.3 DJANGO - FASTAPI
### 5. Вывод

----

### 1. Введение
----

#### 1.1 Обоснование выбранной темы

#### 1.2 Цели дипломной работы

#### 1.3 Задачи дипломной работы

#### 1.4 Основные определения

###2. Свойства и особенности фреймворков
----

#### 2.1 Django

#### 2.2 FastAPI  

#### 2.3 Flask

### 3. Примеры написанных программ на Django, Flask и FastAPI
----

#### 3.1 Пример работы на Django

Для того, чтобы начать работу с Dgango следует его установить введя pip install django в консоль. После чего 
при помощи команд на рис 1.1.2 и рис 1.1.3 создаем проект dizain и приложения dizain_app. Данные папки представляют из себя готовые Django шаблоны с структурированной "начинкой", что очень помогает разработчику делать качественный продукт.

![image](https://github.com/user-attachments/assets/73988a24-6528-4988-9168-fdb37acea83d)

(рис 1.1.1)

![image](https://github.com/user-attachments/assets/f02d0b61-7f31-41e8-a2a6-436d5c51cf7a)

(рис 1.1.2)

![image](https://github.com/user-attachments/assets/03b2e68b-5746-4445-987b-22f1b60659e3)

(рис 1.1.3)

Django - требовательнй фреймворк, который желает абсолютного выполнения всех правил написания кода в нем, это и касается проектов.
У каждого .py есть свои определенные функции, к примеру в settings.py хранятся основные настройки Django. В них мы можем как подключить 
новые приложения, так и прописывать пути к нужным папкам. Проекты dizain.urls.py и dizain_app.views.py взаимосвязаны между собой, в urls.py прописиваются пути по которым пользователи будут получать доступ к сайтам, а в views.py прописаны функции, в которых идет обработка информации, полученной либо с сайта либо из базы данных, и последующее введение этой информации в html-шаблон. 

![image](https://github.com/user-attachments/assets/0cda3723-a21b-4d3d-b629-543a04060d99)

(рис 1.2)

Обязательно перед запуском сервера стоит преверить в верном ли месте (папке) Django будет искать html-шаблоны. Для этого
следует зайти в settings.py -> TEMPLATES и в пункте 'DIRS' ввести путь к папке, в которой храняться нужные
html-шаблоны, как показано на рис 1.3. В данном случае: [BASE_DIR / 'templates'].

![image](https://github.com/user-attachments/assets/f2498644-bf71-4af8-8528-879f6e2539e1)

(рис 1.3)

В forms.py и models.py описывабтся классы и характеристики объектов, которые разработчик в последствии будет использовать при работе с базами данных.

![image](https://github.com/user-attachments/assets/7e64801f-e356-44a2-9bf6-7cdf6fe32c79)

(рис 1.4.1)

![image](https://github.com/user-attachments/assets/636a75ef-efcd-484d-b5ff-9c538cd2f963)

(рис 1.4.2)

Одно из главный преимуществ Django заключается в удобной работе с базами данныл при помощи QuerySet запросов.
Перед работы с ними стоит перейти в интерактивную консоль, введя в терминал команду python manage.py shell. После чего (если верно были 
созданы миграции) появится доступ к записи/редактированию/удалению информации из базы данных. 
На рис 1.5 предоставлены первоначальные индексы и таблицы базы даннных, которые Django создает самостоятельно после совершения миграции.

![image](https://github.com/user-attachments/assets/167cef3c-9580-45e0-acdb-d312c982ede1)

(рис 1.5)

Структура готового проекта, написанного на Django

```
Django/               
 │
 └── dizain/        
    │ 
    ├── dizain/
    │   ├── __pycache__/   
    │   ├── __init__.py
    │   ├── asgi.py 
    │   ├── settings.py    
    │   ├── urls.py        
    │   └── wsgi.py        
    │
    └── dizain_app/
    │   ├── __pycache__/     
    │   ├── migrations/    
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── forms.py        
    │   ├── models.py
    │   ├── tests.py     
    │   └── views.py      
    │                 
    └── static/         
    │   └── photo/       
    │      
    └── templates/    
    │    ├── contacts.html
    │    ├── example.html
    │    ├── main.html
    │    ├── registration.html
    │    ├── sample.html
    │    ├── services.html
    │    └── vhod.html
    │
    │── db.sqlite3
    └── manage.py
```
#### Пример рабочего сайта
----
Далее в Flask и FastAPI будут использованы аналогичные html-шаблоны. Было принято решение пока не использовать язык стилей CSS, так как целью данной работя является сравнения самих фреймворков. Если интересует содержание данных шаблонов, то следует перейти в Django->dizain->templates проекта, который находится в файлах, приложенных к данному диплому. 

![image](https://github.com/user-attachments/assets/2ef58bae-a15d-4b81-9e20-b44463015240)
(рис 2.1)

![image](https://github.com/user-attachments/assets/6157c3bf-cef4-48a0-8c7c-ba2a8cf87d02)
(рис 2.2)

![image](https://github.com/user-attachments/assets/3e9fe3a3-cd4d-4261-91fc-f5759a5cc879)
(рис 2.3)

![image](https://github.com/user-attachments/assets/91786cb9-5a6c-4f9a-b750-92758dcc1604)
(рис 2.4)

![image](https://github.com/user-attachments/assets/66caeb1e-4df3-49ce-ab60-a2d5b2506224)
(рис 2.5)

![image](https://github.com/user-attachments/assets/9cb99d78-b359-4a41-8f81-c1c961b435a7)
(рис 2.6)

#### 3.2 Пример работы на Flask

![image](https://github.com/user-attachments/assets/dfc6af37-bb40-4a8f-a14a-3f432aa40aea)
(рис 3.1)



#### 3.3 Пример работы на FastAPI

### 4. Анализ и сравнение работы на Django, Flask и FastAPI
----


#### 4.1 FLASK - FASTAPI

#### 4.2 DJANGO - FLASK

#### 4.3 DJANGO - FASTAPI

### 5. Вывод
----


