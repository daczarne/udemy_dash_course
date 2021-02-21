# Import libraries and modules
import numpy as np
from numpy.core.fromnumeric import size
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
        mode = "markers",
        marker = dict(
            size = 12,
            color = "rgb(51, 204, 153)",
            symbol = "pentagon",
            line = dict(
                width = 2
            )
        )
    )
]

layout = go.Layout(
    title = "Hello world!",
    xaxis = {
        "title": "X axis"
    },
    yaxis = {
        "title": "Y axis"
    },
    hovermode = "closest"
)

fig = go.Figure(
    data = data,
    layout = layout
)

# Save the graph
pyo.plot(fig, filename = "03_scatter_points.html")
