from flask import Flask, render_template, redirect, url_for, request
from models import db, Book, User
from flask import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/main/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('main'))
    return render_template('vhod.html')

@app.route('main/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main'))

@app.route('/main/shop')
def shop():
    books = Book.query.all()
    return render_template('shop.html', books=books)

@app.route('/main/cart')
@login_required
def cart():
    books = current_user.cart
    return render_template('cart.html', books=books, total_price=  sum(book.price for book in books))

@app.route('/main/remove_from_cart/<int:book_id>')
@login_required
def remove_from_cart(book_id):
    book = Book.query.get(book_id)
    current_user.cart.remove(book)
    db.session.commit()
    return redirect(url_for('cart'))

@app.route('/main/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        age = request.form['age']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if len(username) <= 30 and password == confirm_password and len(password) >=8 and age.isdigit() and len(age) <=3:
            hashed_password = generate_password_hash(password, method='sha256')
            new_user = User(username=username, password=hashed_password, age=int(age))
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('registration.html')


@app.route('/main/add_to_cart/<int:book_id>')
@login_required
def add_to_cart(book_id):
    book = Book.query.get(book_id)
    current_user.cart.append(book)
    db.session.commit()
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)


