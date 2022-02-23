# Project Setup

[![Run Tests, Build Dockerfile, Run on Heroku](https://github.com/kaw393939/docker_flask/actions/workflows/test-build-deploy.yml/badge.svg)](https://github.com/kaw393939/docker_flask/actions/workflows/test-build-deploy.yml)

## Setting up CI/CD

1. Clone this repo to your local (DO NOT FORK THIS REPO, IF YOU DO YOU HAVE TO ENABLE ACTIONS BEFORE ANYTHING RUNS)
2. Create a new repo on your own account
3. Remove the origin remote and replace it with your own new repo.  (Do not add a readme or anything it should be empty)
4. Create an account with Heroku, create an app, create a heroku API key (see notes)
5. Create a new repo in Docker hub

### In the Repository Settings under Action -> Secret

6. Add repository settings for action secrets for DOCKER_USERNAME, DOCKER_PASSWORD, HEROKU_API_KEY (put the appropriate
   values in)

### In this file .github/workflows/test-build-deploy.yml

6. Change line 45 to have your docker repo address in: .github/workflows/test-build-deploy.yml
7. change lines 61 to have your heroku app name in: .github/workflows/test-build-deploy.yml
8. change line 62 to have your heroku email in: .github/workflows/test-build-deploy.yml

9. change line 19 of readme.md (this file) to have the link to your heroku app (click on the app and then there is a
   button to open the app in the upper right)  This will not work until it successfully deploys
10. Push your local repo and fix any errors that appear when the workflow is running. You can check the workflow in the
    actions tab

### Heroku Notes: Get the heroku API key from account in: -> applications -> create authorization button

### GitHub Notes:  Set the action secrets repository in: -> settings -> actions -> secrets

## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint .coveragerc is the config for coverage setup.py is a config file for pytest

[My App](https://kwilliam-flask.herokuapp.com)

# Test Change