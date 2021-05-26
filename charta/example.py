import numpy as np
from charta import Dashboard, Series, Chart

x = np.linspace(-1, 1)
y1 = np.sin(np.pi * x)
y2 = np.sin(2 * np.pi * x)
y3 = np.sin(3 * np.pi * x)

# Clear all of the plots and data.
dahs = Dashboard.default()
dash.reset()

# Add some series.
dash.add_series(Series("x", x))
dash.add_series(Series("y1", y1))
dash.add_series(Series("y2", y2))
dash.add_series(Series("y3", y3))
dash.add_series(Series("this_is_a_really_really_really_really_really_really_really_really_long_name", y3))

# Add a couple of charts
dash.add_chart(Chart("chart1", [["x", "y1"], ["x", "y2"]]))
dash.add_chart(Chart("chart2", [["y2", "y3"]]))

# Add multiple series at once.
dash.add_series([Series(f"example_{i}", np.linspace(0, 1)) for i in range(50)])

# Add multiple charts at once.
dash.add_chart([Chart(f"chart{i}", [["y2", "y3"]]) for i in range(3,10)])

# Extend some of the series
x_new = np.linspace(1.1, 2.0, 100)
y1_new = np.sin(np.pi * x_new)
y2_new = np.sin(2 * np.pi * x_new)
y3_new = np.sin(3 * np.pi * x_new)
dash.extend_series("x", x_new)
dash.extend_series("y1", y1_new)
dash.extend_series("y2", y2_new)
dash.extend_series("y3", y3_new)
dash.update()

# Save the data to a json file.
dash.save("/tmp/test.json")
