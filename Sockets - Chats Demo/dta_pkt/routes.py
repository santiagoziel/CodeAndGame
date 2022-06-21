from flask import render_template, url_for, redirect
from flask_login import login_user, login_required, logout_user, current_user

from dta_pkt import app, db, login_manager
from dta_pkt.forms import RegisterForm
from dta_pkt.models import User

db.create_all()

login_manager.login_view = "log_in"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/', methods = ['GET', 'POST'])
def log_in():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user:
            login_user(user)
        else:
            new_user = User(username = form.username.data)
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(username = form.username.data).first()
        login_user(user)
        return redirect(url_for("chat"))
    return render_template('index.html', form = form)

@app.route('/chat', methods = ['GET', 'POST'])
@login_required
def chat():
    #gets all conected users exept self
    users = User.query.filter(User.room != "", User.id != current_user.id).all()
    return render_template('chat.html', user = current_user, users = users)
