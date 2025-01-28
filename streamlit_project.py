import streamlit as st
import pandas as pd

# Initialize session state for storing student data
if 'students' not in st.session_state:
    st.session_state.students = []

def main():
    st.title("Student Score Tracker") 
    st.write("Add students scores and filter by minimum score")
    
    # Create input section
    st.header("Add New Student")
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Student Name")
    with col2:
        score = st.number_input("Score (0-100)", min_value=0, max_value=100, value=0)
    
    # Add student button
    if st.button("Add Student"):
        if name and score >= 0:
            st.session_state.students.append({"name": name, "score": score})
            st.success(f"Added {name} with score {score}")
        else:
            st.error("Please enter both name and score")
    
    # Display student data
    if st.session_state.students:
        st.header("Filter by Minimum Score")
        
        # Convert the list of students to a DataFrame
        df = pd.DataFrame(st.session_state.students)
        
        # Add score filter
        min_score = st.slider(
            "Minimum Score",
            min_value=0,
            max_value=100,
            value=0
        )
        
        # Filter and display the DataFrame
        filtered_df = df[df['score'] >= min_score]
        
        # Display statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Students", len(df))
        with col2:
            st.metric("Average Score", f"{df['score'].mean():.1f}")
        with col3:
            st.metric("Students Shown", len(filtered_df))
            
        # Display the text exactly as requested
        st.write(f"Students with scores >={min_score}:")
        
        # Display the filtered table
        st.dataframe(
            filtered_df,
            column_config={
                "name": "Student Name",
                "score": st.column_config.NumberColumn(
                    "Score",
                    format="%d"
                )
            },
            hide_index=True
        )
        
        # Add a button to clear all data
        if st.button("Clear All Data"):
            st.session_state.students = []
            st.experimental_rerun()
    
    else:
        st.info("No students added yet. Add some students to see them listed here.")

if __name__ == "__main__":
    main() 