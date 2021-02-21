# Import libraries and modules
import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Read data into a DataFrame
df = pd.read_csv("nst-est2017-alldata.csv")
df = df[df["DIVISION"] == "1"]
df.set_index("NAME", inplace = True)
list_of_pop_cols = [col for col in df.columns if col.startswith("POP")]
df = df[list_of_pop_cols]

# Build traces
data = [
  go.Scatter(
    x = df.columns,
    y = df.loc[name],
    mode = "lines",
    name = name
  )
  for name in df.index
]

# Save the plot
pyo.plot(data, filename = "04_data.html")
