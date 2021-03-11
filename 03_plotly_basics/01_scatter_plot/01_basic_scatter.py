# Import libraries and modules
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Generate random data
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

# Build a plotly graph
data = [
	go.Scatter(
		x = random_x,
		y = random_y,
		mode = "markers"
	)
]

# Save the graph
pyo.plot(data, filename = "01_basic_scatter.html")
