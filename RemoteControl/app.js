const express = require("express");
const WebSocketServer = require("ws").Server;

const app = express();
app.listen(8080, () => {
  console.log("Server starting on port 8080")
});

app.use(express.static(__dirname));
app.get('/', (req, res) => {
  res.sendFile(__dirname + "/Webpage/webpage.html");
})

const wss = new WebSocketServer({port: 40510});

wss.on("connection", function(ws)
{
  ws.on("message", function(message)
  {
    console.log("server received: " + message);
    ws.send('hello from server');
  })
});