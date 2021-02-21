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
pyo.plot(fig, filename = "02_basic_scatter_layout.html")
