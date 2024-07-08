import pandas as pd
import camelot
import numpy as np
import streamlit as st
logo = '/Users/muhammadahmed/Desktop/Projects/foxtrot/time_table/giki.png'
st.image(logo,use_column_width=True)
pdf_path = '/Users/muhammadahmed/Desktop/Projects/foxtrot/time_table/time.pdf'

# Read all pages into a list of DataFrames
tables = camelot.read_pdf(pdf_path, flavor='stream', pages='all')

# Create empty DataFrames for each day
Monday, Tuesday, Wednesday, Thursday, Friday = pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

# Loop through each table in the list
for i, table in enumerate(tables):
    # Convert the table to a DataFrame
    df = table.df

    # Drop the first row (table heading)
    df = df.drop(0)

    # Reset the index
    df = df.reset_index(drop=True)

    # Assign the DataFrame to the corresponding day
    if i == 0:
        Monday = df
    elif i == 1:
        Tuesday = df
    elif i == 2:
        Wednesday = df
    elif i == 3:
        Thursday = df
    elif i == 4:
        Friday = df

    # Print or process the modified DataFrame
  

# Now you have separate DataFrames for each day: Monday, Tuesday, Wednesday, Thursday, and Friday.





days = [Monday, Tuesday, Wednesday, Thursday, Friday]

for day in days:
    day = day.iloc[:, 1:-1]

Monday = Monday.iloc[:, 1:-1]
Tuesday = Tuesday.iloc[:, 1:-1]
Wednesday = Wednesday.iloc[:, 1:-1]
Thursday = Thursday.iloc[:, 1:-1]
Friday = Friday.iloc[:, 1:-1]

# Print the result
num_rows, num_columns = Thursday.shape
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_columns}")

# Days of the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Time slots
time_slots = ["8:00-8:50", "9:00-9:50", "10:30-11:20", "11:30-12:20",
              "12:30-13:20", "14:30-15:20", "15:30-16:20", "16:30-17:20"]

# Create a DataFrame with time_slots as columns and days_of_week as index
df_time = pd.DataFrame(columns=time_slots, index=days_of_week)

# Create a DataFrame with the "days" column
df_time = pd.DataFrame({'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']})

# Define the new column names
new_column_names = ['8:00-8:50', '9:00-9:50', '10:30-11:20', '11:30-12:20',
                    '12:30-13:20', '14:30-15:20', '15:30-16:20', '16:30-17:20']

# Add columns for each time slot
df_time[new_column_names] = pd.DataFrame([[None] * len(new_column_names)] * len(df_time), columns=new_column_names)

# Streamlit app
st.title("GIKI Timetable : in a few clicks :)")

# Sidebar for course input
num_courses = st.sidebar.number_input("Enter the number of courses:", min_value=1, value=1)

course_codes = []
for i in range(num_courses):
    course_code = st.sidebar.text_input(f"Enter course code {i + 1}:", key=f"course_{i}")
    course_codes.append(course_code)

# Update df_time based on user input
for k in range(num_courses):
    course_code = course_codes[k]
    for j in range(5):
        row_indices, col_indices = np.where(days[j] == course_code)
        if len(row_indices) != 0:
            row_idx, col_idx = row_indices[0], col_indices[0]
            df_time.iloc[j, [col_idx]] = course_code

# Display df_time as a table
st.dataframe(df_time, width=800, height=400)

# Save df_time as PDF
if st.button("Download as PDF"):
    st.write("Downloading PDF...")
    df_time.to_pdf("course_schedule.pdf")

    
