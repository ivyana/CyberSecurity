from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask import render_template, redirect, url_for, jsonify
from forms import RegistrationForm

csrf = CSRFProtect()

app = Flask('__name__', template_folder="./templates/")
app.config['SECRET_KEY'] = 'ty4425hk54a21eee5719b9s9df7sdfklx'
csrf.init_app(app)


@app.route('/')
def index():
    form = RegistrationForm()
    return render_template('registration.html', form=form)


@app.route('/register', methods=['POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print('Submission successful!')
        return render_template('success.html', form=form)

    return render_template('registration.html', form=form)



