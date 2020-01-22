Steps for setting up environment:
1. Clone repo

2. Make sure you have python 3.7 installed

3. Run "pip install virtualenv" - this manages "Virtual Environments" for Python and keeps all of your dependencies separate

4. Navigate to ./server in the repository

5. Run the command "mkvirtualenv AEC_Qualifier" - makes a new virtual environment
    - If the virtual environment is running you will see (AEC_Qualifier) to the left of the directory name in your terminal
    - to stop the venv run "deactivate", to start it again run "workon AEC_Qualifier"
6. To install the dependencies run the command "pip install -r requirements.txt" - this installs all of the listed modules in the requirements 
file

7. Install dependencies (navigate to ./client)
    - If you don't have npm installed go to https://www.npmjs.com/get-npm
    - "npm install" will install all of the packages that you need for getting the project up and running
    - The Vue application is using a component library called Vuetify https://vuetifyjs.com/en so we don't have to much around with any of the       styling stuff
    
8. To run the vue server navigate to ./client and run "npm run serve" - this builds it in development so that any changes are updated when the file is saved (this means you don't have to keep stopping and starting the server)

9. To run the flask server navigate to ./server and run "python app.py" - it is configured to build in debug mode so that any changes are reflected when files are saved

*For this to work you need to have both the Vue server and the Flask server running at the same time*

For debugging install the Vue dev tools extension for Chrome https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd

Also recommend syntax highlighting for Vue with VS code - https://marketplace.visualstudio.com/items?itemName=jcbuisson.vue
And python syntax highlighting -https://marketplace.visualstudio.com/items?itemName=ms-python.python

This whole thing was setup with https://testdriven.io/blog/developing-a-single-page-app-with-flask-and-vuejs/ which may serve as a good reference!

Pandas data analysis - https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html"# AEC_Template" 
