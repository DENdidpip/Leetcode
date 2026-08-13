import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students = students.rename(columns={'age' : 'age_in_years', 'id' : 'student_id', 'first' : 'first_name', 'last': 'last_name'})
    return students