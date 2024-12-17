import pandas as pd




def gpa_hours_sleep_student(students_data):
    df = pd.DataFrame(students_data)

    # Calculate the average GPA and Sleep Hours
    average_gpa = df['GPA'].mean()
    average_sleep_hours = df['Sleep_Hours_Per_Day'].mean()

    # Filter students: GPA > average and Sleep Hours < average
    filtered_df = df[(df['GPA'] > average_gpa) & (df['Sleep_Hours_Per_Day'] < average_sleep_hours)]
    print(filtered_df)
