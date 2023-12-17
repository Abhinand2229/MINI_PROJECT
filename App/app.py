from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite database file named 'site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result_data = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('results', lazy=True))

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/form2', methods=['GET', 'POST'])
def form2():
    if request.method == 'POST':
        username = request.form['username']
        
        # Save the username in the database
        user = User(username=username)
        db.session.add(user)
        db.session.commit()

        # For now, simply redirect to form2.html
        return redirect(url_for('form2'))

    return render_template('form2.html')

@app.route('/direct', methods=['GET', 'POST'])
def direct():
    if request.method == 'POST':
        # Get the result data from the form submission
        result_data = request.form['result_data']

        # Get the user from the database (assuming you have a way to identify the user)
        user_id = 1  # You need to replace this with a proper way to get the user ID
        user = User.query.get(user_id)

        # Save the result in the database
        new_result = Result(result_data=result_data, user=user)
        db.session.add(new_result)
        db.session.commit()

    return render_template('direct.html')

@app.route('/direct2', methods=['GET', 'POST'])
def direct2():
    # Fetch all results from the database
    results = Result.query.all()
    return render_template('direct2.html', results=results)

if __name__ == '__main__':
    # Create the database tables before running the app
    with app.app_context():
        db.create_all()

    app.run(debug=True)
