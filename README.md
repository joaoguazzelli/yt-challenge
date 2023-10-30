# yt-challenge
## google api key needed
#### Info on how to get it avaliable at: https://console.cloud.google.com/apis/dashboard?hl=pt-br&pli=1

## .env file
#### create a .env file in the project root with the following variables
``GOOGLE_API_KEY=<YOUR_API_KEY>``

## Executing
### Create a virtual env
``python -m venv venv``
### Install the dependencies
``pip install -r requirements.txt``
### Execute
``python main.py``

## Architecture explanation
the main file is just an example of a simple application to be made, since the project is structured in a microsservice 
architecture.

Since the scope of development is very broad, this architecture was chosen to provide more flexibility in the use of it,
providing simplicity in the integration of new services, such as an API, more complex data analysis services, etc.

