const express = require('express');
const WebSocketServer = require('ws').Server;
const wss = new WebSocketServer({port: 40510});

wss.on('connection', function(ws) {
  ws.on('message', function(message) {
    console.log('server received: ' + message);
    ws.send('hello from server');
  })
});

const app = express();

// app.use(express.urlencoded({
//   extended: true
// }))
// app.use(express.json())
app.use(express.static(__dirname));

app.get('/', (req, res)=> {
  res.sendFile(__dirname + '/index.html');
})

app.listen(8080,()=>{
    console.log("Server starting on port 8080")
});