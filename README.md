# MHA Bank



## Introduction
MHA Bank is a simple Python terminal bank app that runs on the Code Institute's mock terminal Heroku.


This is a very simple bank app. At the beginning, the app asks for a username. If the user already exists, their previous balance will be shown. If not, the app will create the username for them, and then asks them to deposit the amount. When they input their deposit amount, it will ask them if they want to withdraw. In the end, the app will show how much money the user has in his bank account

## Live Preview

## User Goals

## Owner Goals

## Features 
* ### Existing Features
* ### Future Features

## Data Model

## Flowchart

## Testings

## Bugs

* ### Fixed Bugs
* ### Unfixed Bugs
* ### Validator Testing

## Technologies Used
* [Python](https://www.python.org/)
* [googlesheets](https://www.google.co.uk/sheets/about/)

## Libraries Used

* [gspread](https://docs.gspread.org/en/v3.7.0/api.html)

* [credentials](https://pypi.org/project/credentials/)

* [pyfiglet](https://pypi.org/project/pyfiglet/0.7/)

* [time/sleep](https://www.programiz.com/python-programming/time/sleep)

## Deployments
Git and GitHub are used for version control. Python is the backend language, and can't be displayed with GitHub alone, To live preview my project, I used Heroku.
* ### Github
    * Clone the project
        * In order to clone this project, the user must locate the repository Code button on the [MHA-Bank](https://github.com/hashim222/mha-bank) and select either download zip or open with Github Desktop. 
        * A user can copy and paste the link into their git terminal by clicking GitHub CLI and the Copy button in the Code Dropdown menu.

* ### Heroku
    * Deployment steps on Heroku. 

        * Set up a Heroku account (if needed).

        * In the top right corner of the dashboard, click "New" and choose "Create new app."

        * The name of your application must be unique. Click "Create App" after selecting your region.

        * Click the "Settings" tab and scroll down to "Config Vars" on your project page.

        * Enter "PORT" in the KEY input field, followed by "8000" in the VALUE input field and Add the Config Vars by clicking the "Add" button.

        * Add the Python and Node.js buildpacks to the buildpacks section, ensuring that the Python builds are listed above the Node.js builds.


        * Go back to the tabs at the top of the page, then select the "Deploy" tab and choose Github deployment.

        * Then click the "Connect" button to link your repository.

        * Select either Automatic Deployment or Manual Deployment at the bottom of the page. Whenever a project is pushed to Github, Automatic Deployment will deploy it to Heroku. Wait for your project to be deployed.

        * The following steps have been used due to an issue with Heroku's login process: click on "Details" to see what steps have been used👇<details>IF YOU ARE CREATING A NEW DEPLOYMENT/APP<br><br>
Run the command heroku login -i and login when prompted. Then run the command heroku create your_app_name_here to create a new app, replacing your_app_name_here with the name you want to give your app. This will create a new Heroku app and link it to your Gitpod terminal. You can then access the app via the Heroku dashboard and set up your config vars.<br><br>
IF YOU ALREADY HAVE AN APP CREATED WHICH USES AUTOMATIC DEPLOYS.<br>
Run the command heroku login -i and login when prompted. Then run the following command: heroku git:remote -a your_app_name_here and replace your_app_name_here with the name of your Heroku app. This will link the app to your Gitpod terminal.
Once you have followed the appropriate step above, your Heroku app will be linked to your Gitpod workspace.
HOW TO DEPLOY
After linking your app to your workspace with one of the above steps, you can then deploy new versions of the app by running the command git push heroku main and your app will be deployed to Heroku.</details>

## Credits
## Acknowledgment
