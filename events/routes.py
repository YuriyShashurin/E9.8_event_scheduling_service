from events import db, app, login_manager,bcrypt
from flask import render_template,redirect,request,flash, url_for
from events.models import User, Event, get_user
from events.forms import UserForm, EventForm, LoginForm
from flask_login import login_required, current_user, login_user,logout_user
import datetime

@login_manager.user_loader
def user_loader(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        return user
    return None


@app.route('/', methods=["GET", "POST"])
def show_all_events():
    events = Event.query.all()
    data = {
        'events': events,

    }

    return render_template('index.html',data=data)


@app.route('/create_event', methods=["GET", "POST"])
@login_required
def create_event():
    form = EventForm()
    if form.validate_on_submit(): ##почему не работает form.validate_or_submit
        title = form.title.data
        description = form.description.data
        date_start = form.date_start.data
        time_start = form.time_start.data
        date_end = form.date_end.data
        time_end = form.time_end.data
        event = Event(
            owner=current_user,
            title=title,
            description=description,
            date_start=date_start,
            time_start=time_start,
            date_end=date_end,
            time_end=time_end
        )
        db.session.add(event)
        db.session.commit()
        return redirect("/")
    return render_template("create_event.html", form=form)

@app.route('/signup', methods=["GET", "POST"])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        try:
            username = form.username.data
            email = form.email.data
            password = form.password.data
            user = User(username=username, email=email, password=bcrypt.generate_password_hash(password).decode('utf-8'))
            db.session.add(user)
            db.session.commit()
            return redirect("/")
        except:
            flash('Введенный email уже существует')
    return render_template("signup.html", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect("/")
            else:
                flash('Введен неправильный логин/пароль')
    return render_template("login.html", form=form)

@app.route('/logout', methods=["GET"])
@login_required
def logout():
    """Logout the current user."""
    user = User.query.filter_by(id=current_user.id).first()
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect('/')


@app.route('/delete/<id>', methods=['GET', 'POST'])
def delete(id):
    event = Event.query.filter_by(id=id).first()
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for('show_all_events'))

@app.route('/edit_event/<id>', methods=['GET', 'POST'])
def edit_event(id):
    event = Event.query.filter_by(id=id).first()
    print(event)
    form = EventForm(obj=event)
    if form.validate_on_submit():
        event.title = form.title.data
        event.description = form.description.data
        event.date_start = form.date_start.data
        event.time_start = form.time_start.data
        event.date_end = form.date_end.data
        event.time_end = form.time_end.data
        db.session.commit()
        return redirect(url_for('show_all_events'))

    return render_template("edit_event.html", form=form, event=event)

@app.route('/events/today', methods=["GET", "POST"])
def show_today_events():
    current_date = datetime.date.today()
    events = Event.query.all()

    data = {
        'events': events,
        'current_date': current_date
    }

    return render_template('today.html',data=data)

@app.route('/events/tommorow', methods=["GET", "POST"])
def show_tommorow_events():
    current_date = datetime.date.today() + datetime.timedelta(days=1)
    events = Event.query.all()

    data = {
        'events': events,
        'current_date': current_date
    }

    return render_template('tommorow.html',data=data)