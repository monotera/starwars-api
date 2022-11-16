# Star wars API

Starwars API is a basic Django based API for all the star wars fans. This API allows the user to to see a list of all the characters related to the Star Wars universe, each character allows to see the movies in which said character participates and each movie has a detail where the opening text is shown, the planets that are shown in each film, the director and the producers.

## Requirements
- You must have python3.8 or higher
- The machine must have make install.
- If you want to use the make file, you need to have WSL or be in a Debian distribution.

## Running the API

It's quite easy, you just have to run the command `make serve`. This will install all the requiered dependencies, it will create a virtual enviorment and it will run the Django command `python3 manage.py runserve` on the virtual env. If it's the first time you are running it, you must run the command `make migrate`.</br>

If you want to try the endpoints there is a postman collection in the file `star_wars_api.postman_collection.json`.

## Testing

There are two kind of test, the first one will test the functionalities of the app using Django testing and the second one will make a black-box test of the endpoints using pytest. For running this test you can use the following commands. For more information checkout the API doc in `http://127.0.0.1:8000/swagger/` (the api must be running).

### Run all test
`make test`

### Run planets test
`make test_planets`

### Run movies test
`make test_movies`

### Run characters test
`make test_characters`

