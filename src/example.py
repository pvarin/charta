import numpy as np
from charts import Series, Chart
from client import Dashboard

x = np.linspace(-1, 1)
y1 = np.sin(np.pi * x)
y2 = np.sin(2 * np.pi * x)
y3 = np.sin(3 * np.pi * x)

# Clear all of the plots and data.
Dashboard.default().reset()

# Add some series.
Dashboard.default().add_series(Series("x", x))
Dashboard.default().add_series(Series("y1", y1))
Dashboard.default().add_series(Series("y2", y2))
Dashboard.default().add_series(Series("y3", y3))
Dashboard.default().add_series(Series("thisisareallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallylongname", y3))

# Add a couple of charts
Dashboard.default().add_chart(Chart("chart1", [["x", "y1"], ["x", "y2"]]))
Dashboard.default().add_chart(Chart("chart2", [["y2", "y3"]]))

# Add multiple series at once.
Dashboard.default().add_series([Series(f"example_{i}", np.linspace(0, 1)) for i in range(50)])

# Add multiple charts at once.
Dashboard.default().add_chart([Chart(f"chart{i}", [["y2", "y3"]]) for i in range(3,10)])

# x_new = np.linspace(1.1, 2.0)
# y1_new = np.sin(np.pi * x_new)
# y2_new = np.sin(2 * np.pi * x_new)
# y3_new = np.sin(3 * np.pi * x_new)
# Dashboard.default().extend_series("x", x_new)
# Dashboard.default().extend_series("y1", y1_new)
# Dashboard.default().extend_series("y2", y2_new)
# Dashboard.default().extend_series("y3", y3_new)
# Dashboard.default().update()
# Dashboard.default().save("/tmp/test.json")
