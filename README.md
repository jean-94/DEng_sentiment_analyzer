# DEng_sentiment_analyzer
A repository for "Data Engineering 2" project. It is a text sentiment analyzer

## Goals :

- The application is a sentiment analysis application, which, given a piece of text, should be able to reply with its sentiment as being positive, negative, or neutral.
- The text language used must be English
- The application should have a web interface with an input form and a submit button, where users can input their sentences, and hit submit, and the sentiment of their sentence will be presented.
- The accuracy of the sentiment analyzer should be above 80%
- The application must be easily deployable

## Project architecture :

- Deng_sentiment_analyzer : the root directory of the project
  - js : folder containing a javscript script which can allow us to use jquery
    - jquery-3.6.0.min.js : javascript for jquery
  - templates : contains the html of the docker
    - index.html : front and functionalities  of the website
  - Dockerfile : Docker image of the application
  - SentimentAnalyser.py : Python script containing the sentiment analyser (VADER)
  - app.py : Flask server
  - docker-compose.yaml : requirements of the docker-compose
  - requirements.txt  : dependencies of the docker
  - testConnec.py : unittest for the website
  - testModel.py : test of the model 

## How to set up the project :

- Git clone the project into a directory using the following command : `git@github.com:jean-94/DEng_sentiment_analyzer.git`

- Install docker

- ``docker-compose up`` in the folder to test the website

- To launch the tests, you have to pip install :

  - flask
  - nltk
  - statistics
  - numpy
  - beautifulsoup4

  



