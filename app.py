import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Student Scores Manager",
    page_icon="📚",
    layout="wide"
)

# Initialize session state for students if it doesn't exist
if 'students' not in st.session_state:
    st.session_state.students = []

def add_student(name, score):
    """Add a student and their score to the session state."""
    if name and score is not None:  # Ensure both fields are filled
        st.session_state.students.append({"name": name, "score": score})
        return True
    return False

def main():
    st.title("Student Scores Manager 📚")
    
    # Create two columns for input fields
    col1, col2 = st.columns(2)
    
    with col1:
        # Input for student name
        student_name = st.text_input("Student Name", key="name_input")
        
    with col2:
        # Input for student score
        student_score = st.number_input("Score", min_value=0, max_value=100, key="score_input")
    
    # Add student button
    if st.button("Add Student"):
        if add_student(student_name, student_score):
            st.success(f"Added {student_name} with score {student_score}")
        else:
            st.error("Please fill in both name and score")
    
    # Display student data if we have any
    if st.session_state.students:
        st.subheader("Student Records")
        
        # Convert the student data to a DataFrame
        df = pd.DataFrame(st.session_state.students)
        
        # Add minimum score filter
        min_score = st.slider(
            "Filter by minimum score",
            min_value=0,
            max_value=100,
            value=0,
            step=5
        )
        
        # Filter and display the DataFrame
        filtered_df = df[df['score'] >= min_score]
        
        # Display statistics
        st.markdown("### Class Statistics")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Average Score", f"{filtered_df['score'].mean():.1f}")
        with col2:
            st.metric("Highest Score", filtered_df['score'].max())
        with col3:
            st.metric("Number of Students", len(filtered_df))
        
        # Display the filtered DataFrame with styling
        st.dataframe(
            filtered_df.style.highlight_max(subset=['score'], color='lightgreen')
                          .highlight_min(subset=['score'], color='pink'),
            hide_index=True
        )
        
        # Add a button to clear all data
        if st.button("Clear All Data"):
            st.session_state.students = []
            st.experimental_rerun()

if __name__ == "__main__":
    main() 