import zmq
import time
from charts import Series, Chart


def send_data(method, data, protocol="tcp", port=5556):
    with zmq.Context().socket(zmq.REQ) as socket:
        socket.bind("tcp://*:{port}".format(protocol=protocol, port=port))
        socket.send_json({"method": method, "data": data})
        return socket.recv_string()


class Context:
    _default = None

    @classmethod
    def default(cls):
        if cls._default is None:
            cls._default = cls()
        return cls._default

    def add_chart(self, chart):
        send_data("create_chart", chart.to_dict())

    def add_series(self, series):
        data = send_data("create_series", series.to_dict())

    def save(self, filename):
        data = send_data("read", "")


if __name__ == "__main__":
    import numpy as np
    x = np.linspace(-1, 1)
    y1 = np.sin(np.pi * x)
    y2 = np.sin(2 * np.pi * x)
    y3 = np.sin(3 * np.pi * x)
    Context.default().add_series(Series("x", x))
    Context.default().add_series(Series("y1", y1))
    Context.default().add_series(Series("y2", y2))
    Context.default().add_series(Series("y3", y3))
    Context.default().add_chart(Chart("chart1", [["x", "y1"], ["x", "y2"]]))
    Context.default().add_chart(Chart("chart2", [["y2", "y3"]]))
    Context.default().save("test.json")
