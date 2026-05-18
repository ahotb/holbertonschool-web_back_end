const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);
      const output = [];
      output.push(`Number of students: ${students.length}`);

      const fields = {};
      students.forEach((line) => {
        const parts = line.split(',');
        const firstName = parts[0];
        const field = parts[3];
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstName);
      });

      Object.keys(fields).forEach((field) => {
        output.push(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
        );
      });

      resolve(output.join('\n'));
    });
  });
}

module.exports = countStudents;
