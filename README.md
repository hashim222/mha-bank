# MHA Bank



## Introduction
MHA Bank is a simple Python terminal bank app that runs on the Code Institute's mock terminal Heroku.


MHA Bank stands for Muhammad Hashim Aslam Bank, which is very simple bank app.

The app asks for a username at the beginning. If the user already exists, their previous balance will be shown. If not, the app creates a username for them, and then there are four options for them to choose from: deposit, withdraw, view balance, and exit bank.

## Live Preview
Live preview for MHA Bank [Here](https://mha-bank.herokuapp.com/)


## Features 
* ### Existing Features
* ### Future Features

## Data Model
* I used GoogleSheets to store and retrieve the user's data. Each time the user deposits money or withdraws money, these transactions are stored in the spreadsheet.

![image for googlesheets that iused](/readme-images/googlesheet-image.png)
## Flowchart

## Validator Testing

* I confirmed that my code passes with no errors using the PEP8 online Python Validator. 

![image for validator i used to check my project](/readme-images/python-validator.png)

## Bugs


* ### Fixed Bugs
    * The first time I made use of the validator, I got too many warnings for "long lines", as well as a "trailing space" warning. Eventually, I managed to fix all of those warnings.
* ### Unfixed Bugs

## Technologies Used
* These are the technologies that were used to make this project.
    * [Python](https://www.python.org/)
    * [Googlesheets](https://www.google.co.uk/sheets/about/)
    * [W3School](https://www.w3schools.com/)
    * [MDN Web Docs](https://developer.mozilla.org/en-US/)
    * [Stackoverflow](https://stackoverflow.com/)
    * [Git](https://git-scm.com/)
    * [Github](https://github.com/)
    * [Gitpod workspace](https://gitpod.io/workspaces)
    * [Heroku](https://dashboard.heroku.com/apps)

## Libraries Used

* These are the Python modules/libraries used for this project.

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

* With help from the [Code Institute Love sandwich](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) project, I created a function called validate_data() that handles errors.

* The idea of building a bank app with Python comes from a video on [youtube](https://www.youtube.com/watch?v=xTh-ln2XhgU).

* By making this project I had plenty of help from the [Slack Community](https://slack.com/intl/en-gb/) and tutor supprot from Code Institute.
## Acknowledgment

