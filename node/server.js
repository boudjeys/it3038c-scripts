const http = require("http");
const fs = require("fs");
const os = require("os");
const ip = require('ip');

http.createServer((req, res) => {
  if (req.url === "/") {
      fs.readFile("./public/index.html", "UTF-8", (err, body) => {
      res.writeHead(200, {"Content-Type": "text/html"});
      res.end(body);
    });
  } else if(req.url.match("/sysinfo")) {
    myHostName=os.hostname();
    upDays= Math.floor(os.uptime() / (60*60*60));
    upHours=  Math.floor(os.uptime() / (60*60));
    upMinutes= Math.floor(os.uptime() % (60*60) / 60);
    upSeconds= Math.floor(os.uptime() % 60);
    totalMem = ((os.totalmem()) / 1000000).toFixed(2);
    freeMem = ((os.freemem()) / 1000000).toFixed(2);
    html=`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Node JS Response</title>
      </head>
      <body>
        <p>Hostname: ${myHostName}</p>
        <p>IP: ${ip.address()}</p>
        <p>Server Uptime: Days: ${upDays}, Hours: ${upHours}, Minutes: ${upMinutes}, Seconds: ${upSeconds}</p>
        <p>Total Memory: ${totalMem} MB</p>
        <p>Free Memory: ${freeMem} MB</p>
        <p>Number of CPUs: ${os.cpus().length}</p>
      </body>
    </html>`
    res.writeHead(200, {"Content-Type": "text/html"});
    res.end(html);
  } else {
    res.writeHead(404, {"Content-Type": "text/plain"});
    res.end(`404 File Not Found at ${req.url}`);
  }
}).listen(3000);

console.log("Server listening on port 3000");