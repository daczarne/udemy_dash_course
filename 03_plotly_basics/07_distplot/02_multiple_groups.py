# Import libraries and modules
import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

# Generate random data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200) + 0
x3 = np.random.randn(200) + 2
x4 = np.random.randn(200) + 4

hist_data = [x1, x2, x3, x4]
group_labels = ["X1", "X2", "X3", "X4"]

# Build the figure
fig = ff.create_distplot(
  hist_data = hist_data,
  group_labels = group_labels
)

# Save the plot
pyo.plot(fig, filename = "02_multiple_groups.html")
