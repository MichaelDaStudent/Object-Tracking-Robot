var ws = new WebSocket("ws://192.168.1.45:40510");

ws.onopen = function () {
    console.log("websocket is connected....");
    ws.send("client connected");
};

ws.onmessage = function (ev) {
    console.log(ev);
};