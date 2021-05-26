import numpy as np
from charta import Dashboard, Series, Chart

# Create some data.
x = np.linspace(0, np.pi)
y = np.sin(x)

# Get a reference to the dashboard.
dash = Dashboard.default()

# Add data to the dashboard.
dash.add_series(Series("x", x))
dash.add_series(Series("y", y))
dash.add_chart(Chart("chart", ["x", "y"]))
