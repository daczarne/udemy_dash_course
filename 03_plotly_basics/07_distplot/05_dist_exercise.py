#######
# Objective: Using the iris dataset, develop a Distplot
# that compares the petal lengths of each class.
# File: 'iris.csv'
# Fields: 'sepal_length','sepal_width','petal_length','petal_width','class'
# Classes: 'Iris-setosa','Iris-versicolor','Iris-virginica'
######

# Import libraries and modules
import plotly.offline as pyo
import plotly.figure_factory as ff
import pandas as pd

# Read data
df = pd.read_csv("iris.csv")

# Define the traces
trace_0 = df[df['class']=='Iris-setosa']['petal_length']
trace_1 = df[df['class']=='Iris-versicolor']['petal_length']
trace_2 = df[df['class']=='Iris-virginica']['petal_length']

# Define the data variable
hist_data = [trace_0, trace_1, trace_2]
group_labels = ["Setosa", "Versicolor", "Virginica"]

fig = ff.create_distplot(
  hist_data = hist_data,
  group_labels = group_labels
)

# Save the plot
pyo.plot(fig, filename = "05_dist_exercise.html")
