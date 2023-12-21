from flask import Flask, render_template, redirect, url_for, request
import numpy as np
import pandas as pd
import os
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.String(10))
    semester = db.Column(db.String(10))
    subject = db.Column(db.String(50))
    matrix_data = db.Column(db.PickleType())


class Submission1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.String(10))
    semester = db.Column(db.String(10))
    subject = db.Column(db.String(50))
    matrix_data = db.Column(db.PickleType())

class Submission2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    batch = db.Column(db.String(10))
    semester = db.Column(db.String(10))
    subject = db.Column(db.String(50))
    matrix_data = db.Column(db.PickleType())

with app.app_context():
    db.create_all()


@app.route('/')
def  login():
    return render_template('login.html')

@app.route('/form2', methods=['GET', 'POST'])
def form2():
    if request.method == 'POST':
        return redirect(url_for('form2'))
    return render_template('form2.html')


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/direct', methods=['GET', 'POST'])
def direct():
    return render_template('direct.html')


@app.route('/direct2', methods=['GET', 'POST'])
def direct2():
    batch = request.args.get('batch')
    return render_template('direct2.html',batch=batch)

@app.route('/result')
def result():
    submissions = Submission.query.all()
    return render_template('result.html', submissions=submissions)

@app.route('/result1')
def result1():
    submissions = Submission1.query.all()
    return render_template('result1.html', submissions=submissions)
@app.route('/result2')
def result2():
    submissions = Submission2.query.all()
    return render_template('result2.html', submissions=submissions)

@app.route('/indirect')
def co_indirect_form1():
    return render_template('indirect.html')

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

semester_data = {
            "Semester 1": {
                "Subjects": {
                    "Advanced Data Structure": np.array([  # co_po_matrix for Subject 1
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        ]),
        "Computer Networks": np.array([  # co_po_matrix for Subject 2
            [1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0]
        ]),
        "Mathematical Foundations for Computing": np.array([  # co_po_matrix for Subject 3
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
        ]),
        "Data Anayltics and Visualization": np.array([  # co_po_matrix for Subject 4
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0]
        ]),
        "Programming in Python": np.array([  # co_po_matrix for Subject 5
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
        ]),
        "Linux Commands and Shell Scripting": np.array([  # co_po_matrix for Subject 6
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0],
            [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        ]),
        "Professional Communication and Business Etiquette": np.array([  # co_po_matrix for Subject 7
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1]
        ])
            }
        },
        "Semester 2": {
            "Subjects": {
        "Web Application Development": np.array([  # co_po_matrix for Subject 1
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1]
        ]),
        "Advanced Database Management System": np.array([  # co_po_matrix for Subject 2
            [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]),
        "Cloud Computing": np.array([  # co_po_matrix for Subject 3
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0]
        ]),
        "Applied Statistics with R": np.array([  # co_po_matrix for Subject 4
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]
        ]),
        "Virtualization and containers": np.array([  # co_po_matrix for Subject 5
            [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0],
            [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0]
        ]),
        "Design and Analysis of Algorithms": np.array([  # co_po_matrix for Subject 6
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0]
        ]),
        "Object Oriented Programming (JAVA)": np.array([  # co_po_matrix for Subject 7
            [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0]
        ]),
        "Functional Programming": np.array([  # co_po_matrix for Subject 7
            [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
            [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1]
        ]),
        "Advanced Operating System": np.array([  # co_po_matrix for Subject 7
            [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]
        ])
            }
        },
        "Semester 3": {
            "Subjects": {
            "Data Science & Machine Learning": np.array([  # co_po_matrix for Subject 1
                [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
            ]),
            "Design & and Analysis of Algorithms": np.array([  # co_po_matrix for Subject 2
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
            ]),
            "Operations and Research": np.array([  # co_po_matrix for Subject 3
                [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
            ]),
            "Deep Learning": np.array([  # co_po_matrix for Subject 4
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
            ]),
            "Data Science Lab": np.array([  # co_po_matrix for Subject 5
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0]
            ]),
            "Mobile Application Development Lab": np.array([  # co_po_matrix for Subject 6
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0]
            ]),
            "Mini Project": np.array([  # co_po_matrix for Subject 7
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
            ])
                }
            },
            "Semester 4": {
                "Subjects": {
            "Main Project": np.array([  # co_po_matrix for Subject 7
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0],
                [1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
            ])
                }
            }
        }

@app.route('/calculate',  methods=['GET', 'POST'])
def calculate():
    if request.method == 'POST':
        
        batch1 = request.form.get('batch')
        choice = int(request.form['semester'])
        selected_semester = list(semester_data.keys())[choice - 1]
        selected_subject_data = semester_data[selected_semester]["Subjects"]

        selected_subject = (request.form['subject'])

        selected_co_po_matrix = selected_subject_data[selected_subject]

        co_po_matrix = selected_co_po_matrix.astype(float)

        attainment_levels_internal = []

        n = int(request.form['numStudents'])

        co = selected_co_po_matrix.shape[0]

        file = request.files['internalScoresFile']

        # Check if the file is allowed and has a filename
        if file and allowed_file(file.filename):
            # Generate a secure filename and save the file to the UPLOAD_FOLDER
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Load internal marks from CSV
            internal_data = pd.read_csv(file_path, skiprows=1, header=None)
        print(internal_data)
        # Extract Roll numbers, CO marks, and maximum marks from the DataFrame
        co_marks = internal_data.iloc[1:, 1:].values.astype(float)
        selected_data = internal_data.iloc[:, 1:]
        max_marks = selected_data.max().values.astype(float)

        # Initialize an empty array to store attainment levels for internal assessment
        attainment_levels_internal = []

        # Iterate through COs and calculate attainment levels
        for i in range(co):
            # Calculate 60% of the maximum marks for the current CO
            result_internal_co = max_marks[i] * 0.6
            # Create an empty array to store the internal assessment marks for the current CO
            co_internal_scores = co_marks[:, i]

            # Initialize a count variable to keep track of how many students scored greater than or equal to 60% of the maximum marks for internal assessment
            count_internal = np.sum(co_internal_scores >= result_internal_co)

            # Calculate the percentage for internal assessment
            percentage_internal = (count_internal / n) * 100

            # Check the conditions and assign the attainment level for internal assessment
            if percentage_internal >= 50 and percentage_internal < 60:
                attainment_level_internal = 1
            elif percentage_internal >= 60 and percentage_internal < 70:
                attainment_level_internal = 2
            elif percentage_internal >= 70:
                attainment_level_internal = 3
            else:
                attainment_level_internal = 0

            # Append the attainment level to the array
            attainment_levels_internal.append(attainment_level_internal)

        #co_attainment_external
        file1 = request.files['externalScores']

        # Check if the file is allowed and has a filename
        if file1 and allowed_file(file1.filename):
            # Generate a secure filename and save the file to the UPLOAD_FOLDER
            filename1 = secure_filename(file1.filename)
            file_path1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
            file1.save(file_path1)

        external_data = pd.read_csv(file_path1)
        # Assume that the first column contains student IDs, and the second contains external marks
        external_scores = external_data.iloc[:, 1].values.astype(float)

        # Calculate the sum of external assessment scores
        sixtypercent_mark = 60

        # Initialize a count variable to keep track of how many students scored greater than or equal to the average external assessment score
        count_external = 0

        # Loop through the external assessment scores and count students with scores greater than or equal to the average external assessment score
        for score in external_scores:
            if score >= sixtypercent_mark:
                count_external += 1

        # Calculate the percentage for external assessment
        percentage_external = (count_external / n) * 100

        # Check the conditions and assign the attainment level for external assessment
        if percentage_external >= 50 and percentage_external < 60:
            attainment_level_external = 1
        elif percentage_external >= 60 and percentage_external < 70:
            attainment_level_external = 2
        elif percentage_external >= 70:
            attainment_level_external = 3
        else:
            attainment_level_external = 0 

        #co_attainment_direct
        co_attainment_direct = []  # Initialize an empty list to store CO Attainment (Direct)

        for i in range(co):
            co_attainment = 0.8 * attainment_levels_internal[i] + 0.2 * attainment_level_external  # Calculate CO Attainment
            co_attainment_rounded = round(co_attainment, 2)  # Round to two decimal places
            co_attainment_direct.append(co_attainment_rounded)  # Append the rounded CO Attainment to the list

        for i in range(co_po_matrix.shape[0]):  # Iterate through rows
            for j in range(co_po_matrix.shape[1]):  # Iterate through columns
                if co_po_matrix[i][j] == 1:
                    co_po_matrix[i][j] = co_attainment_direct[i]

        # Create a new matrix to hold both the original and updated values
        combined_matrix = []

        # Iterate through rows of the co_po_matrix
        for i in range(co_po_matrix.shape[0]):
            combined_matrix.append([float(x) for x in co_po_matrix[i].tolist()])
        
        # Create a matrix to store the average values, initialized with zeros
        average_column_matrix = np.zeros((1, co_po_matrix.shape[1]))

        # Loop through the co-po matrix and calculate the column averages
        for j in range(co_po_matrix.shape[1]):  # Iterate through columns
            column_values = co_po_matrix[:, j]  # Get all values in the column
            non_zero_values = column_values[column_values != 0]  # Filter out non-zero values
            if non_zero_values.size > 0:
                average = np.mean(non_zero_values)  # Calculate the average of non-zero values
                average_column_matrix[0, j] = average  # Store the average in the result matrix
        
        batch = batch1
        additional_value1 = batch    
        additional_value2 = choice
        additional_value3 = selected_subject
        rounded_average_column_matrix = [[round(val, 2) for val in average_column_matrix[0]]]

        submission = Submission(
            batch=batch,
            semester=choice,
            subject=selected_subject,
            matrix_data=[[round(val, 2) for val in average_column_matrix[0]]]
        )

        db.session.add(submission)
        db.session.commit()

        return render_template('success.html', average_column_matrix=rounded_average_column_matrix,additional_value1=additional_value1,additional_value2=additional_value2,additional_value3=additional_value3)

@app.route('/submit', methods=['POST'])
def submit_form():
    import numpy as np
    import pandas as pd
    # Retrieve data from the submitted form
    batch2 = request.form.get('batch')
    semester1 = request.form.get('semester')
    subject1 = request.form.get('subject')
    survey_file = request.files['surveyFile']

    # Process the CSV file
    if survey_file:
        # Load the CSV data into a DataFrame
        df = pd.read_csv(survey_file)

        # Specify the columns to check
        columns_to_check = ["CO1", "CO2", "CO3", "CO4", "CO5"]

        # Specify the strings to count
        strings_to_count = ["Strongly Agree", "Agree", "Neutral", "Disagree", "Strongly Disagree"]

        # Initialize a dictionary to store the counts for each string in each column
        count_dict = {column: {string: 0 for string in strings_to_count} for column in columns_to_check}

        # Loop through each column and count the occurrences of the specified strings
        for column in columns_to_check:
            for string in strings_to_count:
                count_dict[column][string] += df[column].eq(string).sum()

        # Initialize a list to store the co_indirect_rounded values
        co_indirect_values = []

        # Calculate CO indirect for each CO
        co_counts = {column: sum(count_dict[column].values()) for column in columns_to_check}

        for column in columns_to_check:
            num_s = count_dict[column]["Strongly Agree"]
            num_a = count_dict[column]["Agree"]
            num_n = count_dict[column]["Neutral"]
            num_d = count_dict[column]["Disagree"]
            num_x = count_dict[column]["Strongly Disagree"]

            num_co = co_counts[column]

            co_indirect = 1.5 * ((-2 * num_x + -1 * num_d + 0 * num_n + 1 * num_a + 2 * num_s) / num_co)

            # Round the co_indirect to two decimal places
            co_indirect_rounded = round(co_indirect, 2)

            co_indirect_values.append(co_indirect_rounded)

# Convert the semester value to the corresponding string
        semester_str = f"Semester {semester1}"

# Retrieve the co_po_matrix for the selected semester and subject
        co_po_matrix = semester_data.get(semester_str, {}).get("Subjects", {}).get(subject1, np.array([]))
    #print("Original CO-PO Matrix:")
     #print(co_po_matrix)

# Convert the CO-PO matrix to a float type
        updated_co_po_matrix = co_po_matrix.astype(float)

    for i in range(5):
       indices_to_update = np.where((updated_co_po_matrix[i] == 1) & (co_indirect_values[i] != 0))
       updated_co_po_matrix[i,indices_to_update] = co_indirect_values[i]

#print("\nUpdated CO-PO Matrix:")
#print(updated_co_po_matrix)

# Create a matrix to store the average values, initialized with zeros
    po_matrix = np.zeros((1,12))

# Loop through the co-po matrix and calculate the column averages
    for j in range(12):  # Iterate through columns
           column_values = updated_co_po_matrix[:, j]  # Get all values in the column
           non_zero_values = column_values[column_values != 0]  # Filter out non-zero values
           if non_zero_values.size > 0:
               average = np.mean(non_zero_values)  # Calculate the average of non-zero values
               average_rounded = np.round(average, 2)
               po_matrix[0, j] = average_rounded  # Store the average in the result matrix


    submission = Submission1(
        batch=batch2,
        semester=semester1,
        subject=subject1,
        matrix_data=po_matrix
    )
    db.session.add(submission)
    db.session.commit()

    # Render the result.html template with the obtained values
    return render_template('success1.html',
                       average_column_matrix=po_matrix,
                       additional_value1=batch2,
                       additional_value2=semester1,
                       additional_value3=subject1)

@app.route('/calculate1',  methods=['GET', 'POST'])
def calculate1():
    file = request.files['input_file']
    batch1 = request.form.get('batch')
    choice = request.form.get('semester')
    selected_subject = request.form.get('subject')
    
    if file and allowed_file(file.filename):
            # Generate a secure filename and save the file to the UPLOAD_FOLDER
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            df = pd.read_csv(file_path, index_col=0, )

    co_po_matrix = df.values
    c_p_matrix = co_po_matrix

    # Now 'matrix' contains the values from the CSV file excluding the first row and first column
    print(co_po_matrix)

    co = df.shape[0]
    attainment_levels_internal = []

    n = int(request.form['numStudents'])

    file1 = request.files['internalScoresFile']
    if file1 and allowed_file(file1.filename):
            # Generate a secure filename and save the file to the UPLOAD_FOLDER
            filename1 = secure_filename(file1.filename)
            file_path1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
            file1.save(file_path1)

    internal_data = pd.read_csv(file_path1, skiprows=1, header=None)
    # Extract Roll numbers, CO marks, and maximum marks from the DataFrame
    co_marks = internal_data.iloc[1:, 1:].values.astype(float)
    selected_data = internal_data.iloc[:, 1:]
    max_marks = selected_data.max().values.astype(float)

    # Iterate through COs and calculate attainment levels
    for i in range(co):
            # Calculate 60% of the maximum marks for the current CO
        result_internal_co = max_marks[i] * 0.6
            # Create an empty array to store the internal assessment marks for the current CO
        co_internal_scores = co_marks[:, i]

            # Initialize a count variable to keep track of how many students scored greater than or equal to 60% of the maximum marks for internal assessment
        count_internal = np.sum(co_internal_scores >= result_internal_co)

            # Calculate the percentage for internal assessment
        percentage_internal = (count_internal / n) * 100

            # Check the conditions and assign the attainment level for internal assessment
        if percentage_internal >= 50 and percentage_internal < 60:
            attainment_level_internal = 1
        elif percentage_internal >= 60 and percentage_internal < 70:
                attainment_level_internal = 2
        elif percentage_internal >= 70:
                attainment_level_internal = 3
        else:
                attainment_level_internal = 0

            # Append the attainment level to the array
        attainment_levels_internal.append(attainment_level_internal)

    # co_attainment_external
    file2 = request.files['externalScores']
    if file2 and allowed_file(file2.filename):
            # Generate a secure filename and save the file to the UPLOAD_FOLDER
            filename2 = secure_filename(file2.filename)
            file_path2 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
            file2.save(file_path2)

    external_data = pd.read_csv(file_path2)       
    # Assume that the first column contains student IDs, and the second contains external marks
    external_scores = external_data.iloc[:, 1].values.astype(float)

    total_external = sum(external_scores)
    average_external = round(total_external / n, 2)

        # Initialize a count variable to keep track of how many students scored greater than or equal to the average external assessment score
    count_external = 0

        # Loop through the external assessment scores and count students with scores greater than or equal to the average external assessment score
    for score in external_scores:
        if score >= average_external:
            count_external += 1

        # Calculate the percentage for external assessment
    percentage_external = (count_external / n) * 100

        # Check the conditions and assign the attainment level for external assessment
    if percentage_external >= 50 and percentage_external < 60:
            attainment_level_external = 1
    elif percentage_external >= 60 and percentage_external < 70:
            attainment_level_external = 2
    elif percentage_external >= 70:
            attainment_level_external = 3
    else:
            attainment_level_external = 0

        #co_attainment_direct
    co_attainment_direct = []  # Initialize an empty list to store CO Attainment (Direct)

    for i in range(co):
            co_attainment = 0.8 * attainment_levels_internal[i] + 0.2 * attainment_level_external  # Calculate CO Attainment
            co_attainment_rounded = round(co_attainment, 2)  # Round to two decimal places
            co_attainment_direct.append(co_attainment_rounded)  # Append the rounded CO Attainment to the list

    for i in range(co_po_matrix.shape[0]):  # Iterate through rows
        for j in range(co_po_matrix.shape[1]):  # Iterate through columns
            if co_po_matrix[i][j] == 1:
                co_po_matrix[i][j] = co_attainment_direct[i]

        # Create a new matrix to hold both the original and updated values
    combined_matrix = []

        # Iterate through rows of the co_po_matrix
    for i in range(co_po_matrix.shape[0]):
        combined_matrix.append([float(x) for x in co_po_matrix[i].tolist()])

        # Create a matrix to store the average values, initialized with zeros
    average_column_matrix = np.zeros((1, co_po_matrix.shape[1]))

        # Loop through the co-po matrix and calculate the column averages
    for j in range(co_po_matrix.shape[1]):  # Iterate through columns
        column_values = co_po_matrix[:, j]  # Get all values in the column
        non_zero_values = column_values[column_values != 0]  # Filter out non-zero values
        if non_zero_values.size > 0:
            average = np.mean(non_zero_values)  # Calculate the average of non-zero values
            average_column_matrix[0, j] = average  # Store the average in the result matrix

    batch = batch1
    additional_value1 = batch    
    additional_value2 = choice
    additional_value3 = selected_subject
    rounded_average_column_matrix = [[round(val, 2) for val in average_column_matrix[0]]]

    submission = Submission2(
            batch=batch,
            semester=choice,
            subject=selected_subject,
            matrix_data=[[round(val, 2) for val in average_column_matrix[0]]]
        )

    db.session.add(submission)
    db.session.commit()

    return render_template('success2.html', average_column_matrix=rounded_average_column_matrix,additional_value1=additional_value1,additional_value2=additional_value2,additional_value3=additional_value3)

if __name__ == '__main__':
    app.run(debug=True)