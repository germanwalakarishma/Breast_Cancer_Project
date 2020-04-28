import numpy as np
import pandas as pd

# Answer 1
consecutiveNaturalNum = np.arange(18).reshape(6, 3)
print("consecutive Natural Numbers::\n{}".format(consecutiveNaturalNum))

# Answer 2
df = pd.read_excel("Week 1 Dataset.xlsx")

df2 = df.rename(columns={"Name": "FirstName", "Income per month": "Income",
                         "State": "State_name", "Age": "Age_Num", "Sex": "Gender", "Number of siblings": "Siblings"})
print(df2)


# Answer 3

df.rename(columns={"Name": "FirstName", "Income per month": "Income",
                   "State": "State_name", "Age": "Age_Num", "Sex": "Gender",
                   "Number of siblings": "Siblings"}, inplace=True)
print(df)
print(df[["FirstName", "State_name", "Age_Num"]])

# Answer 4
df4 = pd.read_excel("Week 1 Dataset.xlsx")
df4 = df4.iloc[0:10, -2:]
print("iloc\n", df4)

# Answer 5
df5 = pd.read_excel("Week 1 Dataset.xlsx")
df5 = df5.iloc[3:10, 1:5]
print("iloc\n", df5)

# Answer 6
df6 = pd.read_excel("Week 1 Dataset.xlsx")
# print("Sum :: ", sum(df6["Number of siblings"]))
print("Count :: \n", df6["Number of siblings"].value_counts())

# Answer 7
# Answer -> Dependant variables - number of siblings
#           Independant variables - Income per month,age


# Answer 8
# Each square shows correlation between variables in the dataset.
# As correlation value ranges from -1 to +1 so
# value close to 1 means more positively correlated the variables are,
# closer to 1 means stronger the relationship is.
# A correlation closer to -1 is similar,
# but instead of both increasing one variable will decrease as the other increases.
# According to graph shown, all diagonals shown as 100% in squares(cream white) are correlating each variable to itself
# which means they are perfectly or strongly correlated.
# For rest, larger the percentage number, higher the correlation between two variables.
# As 86% is more close to 100%, higher is the correlation between those variables.
# -57% implies that the relationship between the variables are negatively correlated to each other.
# For -77%, since its approaching to -100%, more strongly and negatively correlation is between two variables.
