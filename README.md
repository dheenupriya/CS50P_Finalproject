# CALLER TUNE


#### Video Demo:  <https://youtu.be/Ixo3P9Fu4OU?si=JrYfAOlGZs-lBDRP>


#### Description:

Caller Tune is a Python-based command-line application inspired by the caller tune feature commonly used in India, where music is played to the caller while waiting for the receiver to answer the call. The goal of this project is to simulate a similar experience by playing country-specific music based on the caller’s mobile number.

The program begins by asking the user to enter a mobile number along with the country code. The `is_mobile_no` function validates the entered mobile number using regular expressions that are customized for a limited set of supported countries. This ensures that only valid mobile numbers are accepted.

Once the mobile number is validated, the `extract_country_code` function extracts the country code from the number. The extracted country code is then passed to the `find_the_country` function, which maps the code to a corresponding country identifier.

After determining the country, the `play_country_music` function is responsible for playing music from that country. This function sends a request to the iTunes Search API provided by Apple, using the country code as a query parameter. The API returns a list of songs available for that country. To keep the program lightweight and fast, the results are limited to 10 songs.

From the API response, a random song is selected using Python’s `random.choice` function. The program then retrieves the song’s `previewUrl`, which contains a 30-second audio preview. This preview URL is opened automatically in the user’s default web browser, allowing the music to play.

This project demonstrates the use of regular expressions, API integration, JSON data handling, randomness, browser redirection, and unit testing. It also reflects concepts learned throughout CS50, such as modular design, error handling, and test-driven development.
