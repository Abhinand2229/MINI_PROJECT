import numpy as np
import pandas as pd
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
            internal_data = pd.read_csv(file_path, skiprows=2, header=None)

        # Extract Roll numbers, CO marks, and maximum marks from the DataFrame
        co_marks = internal_data.iloc[:, 1:].values.astype(float)
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
        result_internal = 60

        # Initialize a count variable to keep track of how many students scored greater than or equal to the average external assessment score
        count_external = 0

        # Loop through the external assessment scores and count students with scores greater than or equal to the average external assessment score
        for score in external_scores:
            if score >= result_internal:
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