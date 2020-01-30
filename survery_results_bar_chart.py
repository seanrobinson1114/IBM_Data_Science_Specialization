# imports
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt

# load data into dataframe
survey_results_df = pd.read_csv(
    "/home/sean/software/coursera/IBM_Data_Science/Data_Visualization_with_Python/final_project/IBM_Data_Science_Specialization/Topic_Survey_Assignment.csv",
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
ax = survey_results_sorted_percentage_df.plot(
    kind="bar",  
    width=0.8, 
    fontsize=12,
    color=[(0.36078,0.72157,0.36078),(0.35686,0.75294,0.87059),(0.85098,0.32549,0.30980)]
)

# style chart
plt.title(label="Percentage of Respondents' Interest in Data Science Areas", fontsize=16)
plt.legend(fontsize=14)
plt.gca().spines['right'].set_color('none')
plt.gca().spines['left'].set_color('none')
plt.gca().spines['top'].set_color('none')
plt.gca().axes.get_yaxis().set_visible(False)

# add labels to each bar
for p in ax.patches:
    ax.annotate(str(int(round(p.get_height() * 100)))+"%", (p.get_x() + 0.055, p.get_height() + 0.005))

# ensure fits in window
plt.tight_layout()

# display chart
plt.show() 
