#!/usr/bin/node

const url = process.argv[2];
const request = require('request');
request(url, (err, response, body) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  console.log('code:', response.statusCode);
});
