const http = require('http');
const fs = require('fs');
const db = process.argv[2];
const countStudents = require('./3-read_file_async.js');
const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  if (req.url == '/') {
    res.end('Hello Holberton School!');
  } else if (req.url == '/students') {
    countStudents(db)
      .then((result) => {
        res.write('This is the list of our students');
        res.end(result);
      })
      .catch((err) => {
        res.end('Cannot load the database');
      });
  }
});

app.listen(1245);
module.exports = app;
