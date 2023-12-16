from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def login():
    # Render the login.html page
    return render_template('login.html')

@app.route('/form2', methods=['GET', 'POST'])
def form2():
    if request.method == 'POST':
        # Handle the form submission (you can add processing logic here if needed)
        # For now, simply redirect to form2.html
        return redirect(url_for('form2'))

    # Render the form2.html page for GET requests
    return render_template('form2.html')

@app.route('/index', methods=['GET', 'POST'])
def index():
    # Render the index.html page
    return render_template('index.html')

@app.route('/direct', methods=['GET', 'POST'])
def direct():
    # Render the direct.html page
    return render_template('direct.html')

@app.route('/direct2', methods=['GET', 'POST'])
def direct2():
    # Render the indirect.html page
    return render_template('direct2.html')

if __name__ == '__main__':
    app.run(debug=True)
