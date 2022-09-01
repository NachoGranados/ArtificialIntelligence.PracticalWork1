from cmath import exp
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Initialize figure with 4 3D subplots
fig = make_subplots(
    rows=2, cols=1,
    specs=[[{'type': 'surface'}],
           [{'type': 'surface'}]])

# Generate data
x1 = x2 = np.arange(-10.0, 10.0, 0.1)
x1Grid, x2Grid = np.meshgrid(x1, x2)

# function definition
f1 = (x1Grid - 0.7) ** 2 + (x2Grid - 0.5) ** 2
f2 = x1Grid * np.exp(-(x1Grid ** 2) - (x2Grid**2))

# add f1 surfaces to subplot.
fig.add_trace(
    go.Surface(x = x1, y = x2, z = f1, colorscale='Viridis', showscale=False),
    row=1, col=1)

# add f2 surfaces to subplot.
fig.add_trace(
    go.Surface(x = x1, y = x2, z = f2, colorscale='YlOrRd', showscale=False),
    row=2, col=1)

# add title and dimensions to subplot.
fig.update_layout(
    title_text='Graficación de funciones',
    height=1300,
    width=1000
)

# show plot
fig.show()
