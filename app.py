from flask import Flask, render_template, request, redirect, url_for,jsonify
from utils.db import db
from models.report import *
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///report.db'

@app.route('/')
def home():
    return render_template('home.html', page="Home")


@app.route('/about')
def about():
    return render_template('about.html', page="About")


@app.route('/application')
def application():
    return render_template('application.html', page="Application")



@app.route("/submit", methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    print(f"form_data: {form_data}")

    Aadhar_number = form_data.get('Aadhar_number')
    state = form_data.get('state')
    city = form_data.get('city')
    date = form_data.get('date')
    description = form_data.get('description')


    report = Report.query.filter_by(Aadhar_number=Aadhar_number).first()
    if not report:
        report = Report(Aadhar_number=Aadhar_number, state=state, city=city, date=date, description=description)
        db.session.add(report)
        db.session.commit()
    print("submitted successfully")
    return redirect('/')










@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html', page="Thank You")


if __name__ == '__main__':
    app.run(debug=True)