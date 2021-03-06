# URL shortener

A Flask API URL shortener.

## Getting Started 

Install Docker and Docker-compose if you don't have them installed (https://docs.docker.com/compose/install/) and clone the repository:
```
git clone https://github.com/ipandzic/flask-url-shortener.git
```

Cd into the flask-url-shortener folder and start the API on port 5000 by running:
```
make start
```

## Using the API

To create a new account, send a POST request to http://127.0.0.1:5000/account with an "account_id" parameter: 
```
{
	"account_id": "User"
}
```

To shorten a URL send a POST request to http://127.0.0.1:5000/register with a "url" parameter, and an optional "redirect_type" parameter (Basic authentication required): 
```
{
	"url": "https://www.vecernji.hr/",
	"redirect_type": 301
}
```

To view url statistics for an account, send a GET request to http://127.0.0.1:5000/statistics/{account_id}/ (Basic authentication required):

## Shutting down the API

To shut down the API use:
```
make stop
```

To shut down the API and delete the database use:
```
make clean
```