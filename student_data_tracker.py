import streamlit as st
import pandas as pd

# Initialize session state for storing students if not already done
if 'students' not in st.session_state:
    st.session_state.students = []

# App title
st.title("Student Score Tracker")
st.write("Add student scores and filter by minimum score.")

st.write("### Add Student Data")
# Input fields for student name and score
name = st.text_input("Student Name")
score = st.number_input("Score", min_value=0, max_value = 100)

# Button to add student
if st.button("Add Student"):
    if not name:  
        st.warning("Please enter a student name.")  
    elif score < 0 or score > 100:  
        st.warning("Please enter a valid score between 0 and 100.")  
    else:
        st.session_state.students.append({"Name": name, "Score": score})
        st.success(f'Added: {name} with Score: {score}')

# Display students in a table
if st.session_state.students:
    df = pd.DataFrame(st.session_state.students)
    st.write("### Student Data")
    st.write(df)
    
    # Slider for filtering students by minimum score 
    st.write('### Filter by Minimum Score')
    min_score = st.slider("Minimum Score", min_value=0, max_value=100, value=0)
    filtered_df = df[df["Score"] >= min_score]
    st.write(f"Sudents with scores ({min_score})")
    st.dataframe(filtered_df)
else:
    st.info("No students added yet.") 