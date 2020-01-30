# imports
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt

# load data into dataframe
survey_results_df = pd.read_csv(
    "/home/sean/software/coursera/IBM_Data_Science/Data_Visualization_with_Python/final_project/Topic_Survey_Assignment.csv",
    index_col = 0
    )
print(survey_results_df)

# sort the dataframe in descending order of Very Interested
survey_results_sorted_df = survey_results_df.sort_values(by=['Very interested'], ascending=False)
print(survey_results_sorted_df)

# convert numbers into percentages (2233 total, round to 2 decimal points)
survey_results_sorted_percentage_df = survey_results_sorted_df.div(2233.00).round(decimals=2)
print(survey_results_sorted_percentage_df)

# create bar chart
# survey_results_sorted_percentage_df.plot(
#     kind="bar", 
#     figsize=(20,8), 
#     width=0.8, 
#     fontsize=14,
#     color=("#5cb85c","5bc0de", "#d9534f")
# )

fig = plt.figure(figsize=(20,8))
ax = fig.add_subplot(111)

plt.title(label="Percentage of Respondents' Interest in Data Science Areas", fontsize=16)
#plt.legend(fontsize=14)
# plt.gca().spines['right'].set_color('none')
# plt.gca().spines['left'].set_color('none')
# plt.gca().spines['bottom'].set_color('none')
# plt.gca().spines['top'].set_color('none')

survey_results_sorted_percentage_df["Very interested"].plot(kind="bar", color="#5cb85c", width=0.8, position=1)
survey_results_sorted_percentage_df["Somewhat interested"].plot(kind="bar", color="#5bc0de", width=0.8, position=0)
survey_results_sorted_percentage_df["Not interested"].plot(kind="bar", color="#d9534f", width=0.8, position=-1)

plt.show() 
