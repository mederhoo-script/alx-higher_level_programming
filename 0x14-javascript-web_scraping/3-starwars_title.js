#!/usr/bin/node

const episodeNumber = process.argv[2];
const request = require('request');

// Make the request to the Star Wars API with the provided episode number
request(`https://swapi-api.alx-tools.com/api/films/${episodeNumber}`, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the JSON response body
  const filmData = JSON.parse(body);

  // Print the title of the movie
  console.log(filmData.title);
});
