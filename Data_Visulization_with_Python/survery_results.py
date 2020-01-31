# Imports
import pandas as pd

# load data into dataframe
survey_results_df = pd.read_csv(
    "/home/sean/software/coursera/IBM_Data_Science/Data_Visualization_with_Python/final_project/IBM_Data_Science_Specialization/Topic_Survey_Assignment.csv",
    index_col = 0
    )

print(survey_results_df)