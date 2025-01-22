from sqlalchemy import SQLAlchemy
from flask import UserMixin

db = SQLAlchemy()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    price = db.Column(db.Float)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(100))
    age = db.Column(db.Integer)
    cart = db.relationship('Book', secondary='cart')

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))



# from sqlalchemy import Column, Integer, Boolean,  create_engine, String, Float
# from sqlalchemy.orm import declarative_base, sessionmaker
# from wtforms import StringField, PasswordField, IntegerField, EmailField
# from wtforms.validators import DataRequired, Email, Length, EqualTo
# from sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
#
# engine = create_engine('sqlite:///./Flask.db')
#
# Session = sessionmaker(bind=engine)
#
# Base = declarative_base()
#
# class BuyerRegister(Base):
#
#     login = EmailField('Введите email', validators=[DataRequired(), Email(), Length(max=100)])
#     name = StringField('Введите имя', validators=[DataRequired(), Length(max=40)])
#     password = PasswordField('Введите пароль', validators=[DataRequired(), Length(min=8)])
#     second_password = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
#     phone = StringField('Введите номер телефона', validators=[Length(max=12)])
#     age = IntegerField('Введите возраст', validators=[DataRequired()])
#
#     flag_zakaz = Column(Boolean, default=False)
#     flag_sdelano = Column(Boolean, default=False)
#
# class Buyer(Base):
#
#     __tablename__ = 'Buyers'
#     id = Column(Integer, primary_key=True)
#     login = Column(String, nullable=False, info={'label': 'Email'})
#     name = Column(String, nullable=False, info={'label': 'Имя'})
#     password = Column(String, nullable=False, info={'label': 'Пароль'})
#     phone = Column(Integer, nullable=False, primary_key=False, info={'label': 'Номер телефона'})
#     age = Column(Integer, nullable=False, primary_key=False, info={'label': 'Возраст'})
#
#     flag_zakaz = Column(Boolean, default=False)
#     flag_sdelano = Column(Boolean, default=False)
#
# Base.metadata.create_all(bind=engine)