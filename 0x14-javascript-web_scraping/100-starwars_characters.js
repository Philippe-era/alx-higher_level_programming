#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
let done = {};
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const alpha = JSON.parse(body);
    alpha.characters.forEach(function (item, index, array) {
      request(item, function (error, response, content) {
        if (error) {
          console.log(error);
        } else {
          done = JSON.parse(content);
          console.log(done.name);
        }
      });
    });
  }
});
