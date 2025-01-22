from main import app
from models import db, Book

with app.app_context():

    db.create_all()
    book1 = Book(title='Гарри потер и Философский камень', author='Дж. К. Роулинг', price=500)
    book2 = Book(title='Удивительный волшебник из страны ОЗ', author='Л. Ф. Баум.', price=1200)
    book3 = Book(title='Преступление и наказание', author='Достоевский Ф.М.', price=8000)
    book4 = Book(title='Горе от ума', author='А.С. Грибоедов', price=100000)

    db.session.add_all([book1, book2, book3, book4])
    db.session.commit()