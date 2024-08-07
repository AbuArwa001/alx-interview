#!/usr/bin/node

const request = require('request');
const { promisify } = require('util');
const requestPromise = promisify(request);

// Check if the Movie ID is provided as a command-line argument
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Function to get character names
const getCharacterNames = async (characters) => {
  for (let index = 0; index < characters.length; index++) {
    const characterUrl = characters[index];
    try {
      const response = await requestPromise(characterUrl);
      const character = JSON.parse(response.body);
      console.log(character.name);
    } catch (error) {
      console.error(error);
    }
  }
};

// Make the request to the Star Wars API
request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Error: ${response.statusCode}`);
    return;
  }

  const film = JSON.parse(body);
  await getCharacterNames(film.characters);
});
