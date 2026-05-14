const http = require('http');
const fs = require('fs');
const path = require('path');
const mime = {
  '.html':'text/html',
  '.css':'text/css',
  '.js':'application/javascript',
  '.jpg':'image/jpeg',
  '.jpeg':'image/jpeg',
  '.png':'image/png',
  '.svg':'image/svg+xml'
};
http.createServer((req,res)=>{
  let filePath = path.join(__dirname, req.url === '/' ? 'index.html' : decodeURIComponent(req.url));
  fs.readFile(filePath, (err,data)=>{
    if(err){
      res.writeHead(404,{'Content-Type':'text/plain'});
      res.end('Not found');
    } else {
      const ext = path.extname(filePath).toLowerCase();
      res.writeHead(200,{'Content-Type': mime[ext]||'application/octet-stream'});
      res.end(data);
    }
  });
}).listen(8000,()=>{console.log('Server running on http://localhost:8000');});
