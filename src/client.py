import zmq
import time
from charts import Series, Chart


def send_data(method, protocol="tcp", port=5556, **kwargs):
    with zmq.Context().socket(zmq.REQ) as socket:
        socket.bind("tcp://*:{port}".format(protocol=protocol, port=port))
        kwargs["method"] = method
        socket.send_json(kwargs)


class Dashboard:
    _default = None

    @classmethod
    def default(cls):
        if cls._default is None:
            cls._default = cls()
        return cls._default

    def add_chart(self, chart):
        send_data("create_chart", data=chart.to_dict())

    def add_series(self, series):
        send_data("create_series", data=series.to_dict())

    def append_series(self, series_key, data):
        self.extend_series(series_key, [data])

    def extend_series(self, series_key, data):
        send_data("extend_series", data=list(data), key=series_key)

    def save(self, filename):
        send_data("read", filename=filename)

    def update(self):
        send_data("update")


if __name__ == "__main__":
    import numpy as np
    x = np.linspace(-1, 1)
    y1 = np.sin(np.pi * x)
    y2 = np.sin(2 * np.pi * x)
    y3 = np.sin(3 * np.pi * x)
    Dashboard.default().add_series(Series("x", x))
    Dashboard.default().add_series(Series("y1", y1))
    Dashboard.default().add_series(Series("y2", y2))
    Dashboard.default().add_series(Series("y3", y3))
    Dashboard.default().add_series(
        Series(
            "thisisareallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallyreallylongname",
            y3))
    for i in range(50):
        Dashboard.default().add_series(
            Series(f"example_{i}", np.linspace(0, 1)))
    Dashboard.default().add_chart(Chart("chart1", [["x", "y1"], ["x", "y2"]]))
    Dashboard.default().add_chart(Chart("chart2", [["y2", "y3"]]))
    Dashboard.default().add_chart(Chart("chart3", [["y2", "y3"]]))
    Dashboard.default().add_chart(Chart("chart4", [["y2", "y3"]]))
    Dashboard.default().add_chart(Chart("chart5", [["y2", "y3"]]))
    Dashboard.default().add_chart(Chart("chart6", [["y2", "y3"]]))
    Dashboard.default().add_chart(Chart("chart7", [["y2", "y3"]]))
    Dashboard.default().add_chart(Chart("chart8", [["y2", "y3"]]))
    Dashboard.default().add_chart(Chart("chart9", [["y2", "y3"]]))

    x_new = np.linspace(1.1, 2.0)
    y1_new = np.sin(np.pi * x_new)
    y2_new = np.sin(2 * np.pi * x_new)
    y3_new = np.sin(3 * np.pi * x_new)
    Dashboard.default().extend_series("x", x_new)
    Dashboard.default().extend_series("y1", y1_new)
    Dashboard.default().extend_series("y2", y2_new)
    Dashboard.default().extend_series("y3", y3_new)
    Dashboard.default().update()
    Dashboard.default().save("/tmp/test.json")
