from flask import Flask, render_template, request, url_for, flash, redirect
from flask_bootstrap import Bootstrap5
from backend import project
from datetime import date

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, SelectField, widgets
from wtforms.validators import InputRequired

import secrets




app = Flask(__name__)
foo = secrets.token_urlsafe(16)
app.secret_key = foo

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)

csrf = CSRFProtect(app)

csrf.init_app(app)

class CompanyForm(FlaskForm):
    name = SelectField('Company', validators=[InputRequired(message=None)], choices=[('Microsoft', 'Microsoft'), ('Apple', 'Apple'), ('Amazon', 'Amazon'), ('Tesla', 'Tesla')])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CompanyForm()
    message = ""
    company = ""
    pprice= ""
    if form.validate_on_submit():
        name = form.name.data
        print(name)

    return render_template("index.html", form=form, message=message, pprice=pprice)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/predict' , methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        predicted_price = 0
        name = request.form['name']
        if name == 'Microsoft':
            predicted_price = project.models.get('microsoftpredictor').predict({'Date': date.today()})
        elif name == 'Apple':
            predicted_price = project.models.get('applepredictor').predict({'Date': date.today()})
        elif name == 'Amazon':
            predicted_price = project.models.get('amazonpredictor').predict({'Date': date.today()})
        else:
            predicted_price = project.models.get('teslapredictor').predict({'Date': date.today()})

 
        pprice = "The predicted price for today's " + name + " stocks  is: " + f"{predicted_price}"

      
    return render_template("predict.html" , pprice=pprice)



if __name__ == '__main__':
    app.run(debug=True)
