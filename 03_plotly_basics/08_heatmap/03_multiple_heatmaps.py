# Import libraries and modules
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools
import pandas as pd

# Read data
df_1 = pd.read_csv("2010SitkaAK.csv")
df_2 = pd.read_csv("2010SantaBarbaraCA.csv")
df_3 = pd.read_csv("2010YumaAZ.csv")

# Build traces
trace_1 = go.Heatmap(
    x = df_1["DAY"],
    y = df_1["LST_TIME"],
    z = df_1["T_HR_AVG"].values.tolist(),
    colorscale = "Jet",
    zmin = 5,
    zmax = 40
)

trace_2 = go.Heatmap(
    x = df_2["DAY"],
    y = df_2["LST_TIME"],
    z = df_2["T_HR_AVG"].values.tolist(),
    colorscale = "Jet",
    zmin = 5,
    zmax = 40
)

trace_3 = go.Heatmap(
    x = df_3["DAY"],
    y = df_3["LST_TIME"],
    z = df_3["T_HR_AVG"].values.tolist(),
    colorscale = "Jet",
    zmin = 5,
    zmax = 40
)

# Build the figure
fig = tools.make_subplots(
  rows = 1,
  cols = 3,
  subplot_titles = ["Sitka, AK", "Santa Barbara, CA", "Yuma, AZ"],
  shared_yaxes = True
)

fig.append_trace(trace_1, 1, 1)
fig.append_trace(trace_2, 1, 2)
fig.append_trace(trace_3, 1, 3)

fig["layout"].update(
  title = "Temperatures"
)

# Save the plot
pyo.plot(fig, filename = "03_multiple_heatmaps.html")
