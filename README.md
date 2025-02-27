# Music Library Web App

## Setup

```shell
; git clone https://github.com/mantaslv/music_web_app_html.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Set up the virtual environment
; python -m venv .venv

# Activate the virtual environment
; source .venv/bin/activate 

# Install dependencies
(html-application-starter-venv); pip install -r requirements.txt
# Read below if you see an error with `python_full_version`

# Install the virtual browser we will use for testing
; playwright install

# Create a test and development database
(html-application-starter-venv); createdb YOUR_PROJECT_NAME
(html-application-starter-venv); createdb YOUR_PROJECT_NAME_test

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
(html-application-starter-venv); open lib/database_connection.py

# Seed the development database
(html-application-starter-venv); python seed_dev_database.py

# Run the tests (with extra logging)
(html-application-starter-venv); pytest -sv

# Run the app
(html-application-starter-venv); python app.py
# Now visit http://localhost:5001/albums in your browser
```
