# Import libraries and modules
import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

# Generate random data
x = np.random.randn(1000)
hist_data = [x]
group_labels = ["distplot"]

# Build the figure
fig = ff.create_distplot(
  hist_data = hist_data,
  group_labels = group_labels
)

# Save the plot
pyo.plot(fig, filename = "01_dist_basics.html")
