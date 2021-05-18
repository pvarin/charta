var socket = new WebSocket("ws://localhost:" + location.port + "/websocket");

function handle_data(method, data) {
	console.log(`Handling request: ${method}`);
	if (method == "delete") {
		global_state.clear();
		update_charts(d3.select("#charts"), global_state.chart_list());
	}
	if (method == "delete_charts") {
		global_state.clear_charts();
		update_charts(d3.select("#charts"), global_state.chart_list());
	}
	if (method == "read") {
		return socket.send(JSON.stringify(global_state));
	}
	if (method == "create_series") {
		Series.from_obj(data);
	}

	if (method == "create_chart") {
		global_state.add_chart(Chart.from_obj(data));
		update_charts(d3.select("#charts"), global_state.chart_list());
	}
	window.localStorage.setItem("context", JSON.stringify(global_state));
}

socket.onopen = function() {
	console.log("connection established");
};

socket.onclose = function() {
	console.log("connection closed");
};

socket.onerror = function(error) {
	console.log("Error:");
	console.log(error);
};

socket.onmessage = function(e) {
	let data = JSON.parse(e.data)
	handle_data(data.method, data.data);
};

window.onload = function() {
	// Try loading data from local storage.	
	global_state = Context.from_obj(window.localStorage.getItem("context"));
	update_charts(d3.select("#charts"), global_state.chart_list());
};
