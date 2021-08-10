const express = require("express");
const socket = require("socket.io");

// App setup.
const app = express();

const server = app.listen(8080, () => {
  console.log("Server starting on port 8080")
});

// Accessing the webpage.
app.use(express.static(__dirname));

app.get('/', (req, res) => {
  res.sendFile(__dirname + "/Webpage/webpage.html");
});

// Socket setup.
const io = socket(server);

io.on("connection", (socket) => {
  console.log(socket.id);

  // Socket Receive
  socket.on("joystickData", (joystickJSON) => {
    console.log(joystickJSON);
  });
});