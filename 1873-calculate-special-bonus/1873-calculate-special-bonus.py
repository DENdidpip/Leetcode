import pandas as pd
import numpy as np

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees[['employee_id', 'name', 'salary']].rename(columns = {'salary':'bonus'})
    df['bonus'] = np.where(
    (employees['name'].str[0] != 'M') &
    (employees['employee_id'] % 2 == 1),
    employees['salary'],
    0)
    return df[['employee_id', 'bonus']].sort_values(['employee_id'], ascending=[True])