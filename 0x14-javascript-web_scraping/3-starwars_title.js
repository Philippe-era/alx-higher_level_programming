#!/usr/bin/node
const request = require('request');
const www = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(www, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});

