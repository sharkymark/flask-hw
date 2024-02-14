# app.py
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///commissions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Commission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    variable_rate = db.Column(db.Float, nullable=False)
    commission_amt = db.Column(db.Float, nullable=False) 
    attainment = db.Column(db.Float, nullable=False)
    variable_comp = db.Column(db.Float, nullable=False)
    quota = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        quota = float(request.form['quota'])
        variable_comp = float(request.form['variable_comp'])
        deal_revenue = float(request.form['deal_revenue'])

        # Calculate the variable rate
        variable_rate = (variable_comp / quota)

        # Calculate the commission
        commission_amt = (variable_rate * deal_revenue)

        # Calculate quota attained so far
        attainment = (deal_revenue / quota) * 100

        # Save to database
        new_commission = Commission(variable_comp=variable_comp, commission_amt=commission_amt, attainment=attainment, quota=quota, variable_rate=variable_rate)
        db.session.add(new_commission)
        db.session.commit()

        # Redirect to home page to display updated list
        return redirect(url_for('index'))

    # Retrieve commissions from the database
    commissions = Commission.query.all()
    return render_template("index.html", commissions=commissions)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
