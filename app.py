from flask import Flask, render_template, redirect, url_for, flash, request
from forms import LoginForm, RegisterForm, ContactForm

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for CSRF protection in forms

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/program1')
def program1():
    return render_template('program1.html')

@app.route('/program2')
def program2():
    return render_template('program2.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        if form.submit.data:
            flash('Your message has been sent!', 'success')
            return redirect(url_for('contact'))
        elif form.cancel.data:
            flash('Cancelled.', 'info')
            return redirect(url_for('contact'))
    return render_template('contact.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Registered successfully! Please login.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/enroll1')
def enroll1():
    message = request.args.get('message', '')
    return render_template('enroll1.html', message=message)


@app.route('/enroll2')
def enroll2():
    message = request.args.get('message', '')
    return render_template('enroll2.html', message=message)

@app.route('/submit-payment', methods=['POST'])
def submit_payment():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    return render_template('payment_success.html', name=name, email=email, phone=phone)


if __name__ == '__main__':
    app.run(debug=True)
