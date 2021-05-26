import zmq
import time


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
        if (type(chart) == list):
            send_data("create_chart", data=[c.to_dict() for c in chart])
        else:
            send_data("create_chart", data=chart.to_dict())

    def add_series(self, series):
        if (type(series) == list):
            send_data("create_series", data=[s.to_dict() for s in series])
        else:
            send_data("create_series", data=series.to_dict())

    def append_series(self, series_key, data):
        self.extend_series(series_key, [data])

    def extend_series(self, series_key, data):
        send_data("extend_series", data=list(data), key=series_key)

    def save(self, filename):
        send_data("read", filename=filename)

    def update(self):
        send_data("update")

    def reset(self):
        self.delete_series()
        self.delete_charts()

    def delete_charts(self):
        send_data("delete_charts")

    def delete_series(self):
        send_data("delete_series")

