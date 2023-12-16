from flask import Flask, render_template, request, redirect, url_for
import numpy

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html')
@app.route('/process_form', methods=['POST'])
def process_form():
    if request.method == 'POST':
        # Access form data using request.form
        batch = request.form['batch']
        #semester = request.form['semester']
        #subject = request.form['subject']
        choose_option = request.form['chooseOption']

        # Now you can do something with the form data, such as process it or save it to a database
        # ...

        import numpy as np
        # Define a dictionary to store information about semesters and their respective subjects
        semester_data = {
            "1": {
                "Subjects": {
                    "Advanced Data Structure": np.array([  # co_po_matrix for Subject 1
                [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0]
            ]),
            "Advanced Software Engineering": np.array([  # co_po_matrix for Subject 2
                [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
                [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0],
                [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
                [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
            ]),
            "Mathematical Foundations for Computing": np.array([  # co_po_matrix for Subject 3
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
            ]),
            "Digital Fundamentals & Computer Architecture": np.array([  # co_po_matrix for Subject 4
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
            ]),
            "Programming Lab": np.array([  # co_po_matrix for Subject 5
                [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0]
            ]),
            "Data Structure Lab": np.array([  # co_po_matrix for Subject 6
                [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0]
            ]),
            "Web Programming Lab": np.array([  # co_po_matrix for Subject 7
                [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1]
            ])
                }
            },
            "2": {
                "Subjects": {
            "Advanced Computer Networks": np.array([  # co_po_matrix for Subject 1
                [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
            ]),
            "Advanced Database Management System": np.array([  # co_po_matrix for Subject 2
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],
                [1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]),
            "Virtualisation and Containers": np.array([  # co_po_matrix for Subject 3
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0]
            ]),
            "Artificial Intelligence": np.array([  # co_po_matrix for Subject 4
                [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1]
            ]),
            "Networking and System Administration Lab": np.array([  # co_po_matrix for Subject 5
                [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
            ]),
            "Advanced DBMS Lab": np.array([  # co_po_matrix for Subject 6
                [1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0],
                [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1],
                [1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
                [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1]
            ]),
            "Object Oriented Programming Lab": np.array([  # co_po_matrix for Subject 7
                [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0],
                [1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0]
            ]),
            "Applied Statistics": np.array([  # co_po_matrix for Subject 7
                [1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0]
            ]),
            "IPR and Cyber Laws": np.array([  # co_po_matrix for Subject 7
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0]
            ])
                }
            },
            "3": {
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
            "4": {
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

        #choice = request.form['semester']
        selected_semester = request.form['semester']

        # Input the subject selection for the selected semester
        selected_subject_data = semester_data[str(selected_semester)]["Subjects"]

        selected_subject = request.form['subject']
        selected_co_po_matrix = selected_subject_data[selected_subject]

        # Retrieve the co_po_matrix for the selected subject
        co_po_matrix = selected_co_po_matrix.astype(float)

        # Initialize an empty array to store attainment levels for internal assessment
        attainment_levels_internal = []

        # n =   data from form 2.1.1.html

        # Number of course outcomes
        co = selected_co_po_matrix.shape[0]

        for i in range(co):
            max_mark_internal = float(input(f"Enter the maximum mark for internal assessment of CO{i + 1}: "))
            # Calculate 60% of the maximum mark for internal assessment
            result_internal = max_mark_internal * 0.6
            # Create an empty array to store the internal assessment marks
            internal_scores = []

            # Input the internal assessment scores for each student with error handling
            for j in range(n):
                score = float(input(f"Enter the internal assessment score for student {j + 1}: "))
                internal_scores.append(score)

                # Initialize a count variable to keep track of how many students scored greater than or equal to 60% of the maximum mark for internal assessment
                count_internal = 0

                # Loop through the internal assessment scores and count students with scores greater than or equal to 60% of the maximum mark for internal assessment
                for score in internal_scores:
                    if score >= result_internal:
                        count_internal += 1

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

            # Print the attainment levels for each iteration
            print("Attainment Levels for internal assessment:")
            print(attainment_levels_internal)

            #co_attainment_external
            # Create an empty array to store the external assessment marks
            external_scores = []

            # Input the external assessment scores for each student with error handling
            for i in range(n):
                score = float(input(f"Enter the external assessment score for student {i + 1}: "))
                external_scores.append(score)

            # Calculate the sum of external assessment scores
            total_external = sum(external_scores)

            # Calculate the average external assessment score
            average_external = total_external // n  # Use integer division to get an integer result
            print("")

            # Print the average external assessment score
            print(f"The average external assessment score is: {average_external}")

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

            print("")

            # Print the attainment level for external assessment
            print(f"Attainment level for external assessment: {attainment_level_external}")


            #co_attainment_direct
            co_attainment_direct = []  # Initialize an empty list to store CO Attainment (Direct)

            for i in range(co):
                co_attainment = 0.8 * attainment_levels_internal[i] + 0.2 * attainment_level_external  # Calculate CO Attainment
                co_attainment_rounded = round(co_attainment, 2)  # Round to two decimal places
                co_attainment_direct.append(co_attainment_rounded)  # Append the rounded CO Attainment to the list

            print("")

            # Print 'CO Attainment (Direct)' for each course outcome with two decimal places
            print("CO Attainment (Direct) for each course outcome:")
            number = 0
            for co_attainment in co_attainment_direct:
                number = number + 1
                print("CO", number, ": ", co_attainment)

            print("CO-PO corelation matrix:")
            # Print the co-po_matrix
            for row in co_po_matrix:
                print(row)

            for i in range(co_po_matrix.shape[0]):  # Iterate through rows
                for j in range(co_po_matrix.shape[1]):  # Iterate through columns
                    if co_po_matrix[i][j] == 1:
                        co_po_matrix[i][j] = co_attainment_direct[i]

            # Create a new list to store PO labels
            po_labels = ["PO_1", "PO_2", "PO_3", "PO_4", "PO_5", "PO_6", "PO_7", "PO_8", "PO_9", "PO10", "PO11", "PO12"]

            # Create a new matrix to hold both the original and updated values
            combined_matrix = []

            # Iterate through rows of the co_po_matrix
            for i in range(co_po_matrix.shape[0]):
                combined_matrix.append([float(x) for x in co_po_matrix[i].tolist()])

            # Print the combined matrix
            print("Updated CO-PO Matrix:")
            for row in combined_matrix:
                print(row)

            # Create a matrix to store the average values, initialized with zeros
            average_column_matrix = np.zeros((1, co_po_matrix.shape[1]))

            # Loop through the co-po matrix and calculate the column averages
            for j in range(co_po_matrix.shape[1]):  # Iterate through columns
                column_values = co_po_matrix[:, j]  # Get all values in the column
                non_zero_values = column_values[column_values != 0]  # Filter out non-zero values
                if non_zero_values.size > 0:
                    average = np.mean(non_zero_values)  # Calculate the average of non-zero values
                    average_column_matrix[0, j] = average  # Store the average in the result matrix

            # Print the average of each column
            print("Final PO Aggregate:")

            # Print PO labels for the first row with three spaces as separators
            print("   ".join(po_labels))

            # Print the average values for the second row, aligning with labels and using three spaces as separators
            print("   ".join([f"{value:.2f}" for value in average_column_matrix[0]]))





        # Pass selected semester and subject to the success.html template
        return render_template('success.html', semester=selected_co_po_matrix, subject=subject)

if __name__ == '__main__':
    app.run(debug=True)

