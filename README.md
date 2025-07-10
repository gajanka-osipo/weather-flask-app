# Weather API Flask App

A simple Flask web app that shows the weather of your current city based on your IP address using an external Weather API.

## Features

- Shows weather using your IP
- Enter other cities to check their weather
- Uses WTForms for forms
- Uses Jinja2 for templates
- Stores last search in cookies

## Technologies

- Python
- Flask
- WTForms
- Jinja2
- Cookies
- Requests

## Installation

1. Clone the repository:

   git clone https://github.com/gajanka-osipo/weather-flask-app.git

2. Change directory to the project folder:

   cd weather-flask-app

3. (Optional but recommended) Create and activate a virtual environment:

   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate

4. Install the required dependencies:

   pip install -r requirements.txt

5. Create a `config.py` file in the root folder with the following content, and add your own API keys:
   ```python
   import os
    
   class Config(object):
      OWM_TOKEN = 'YOUR_OPENWEATHERMAP_TOKEN'
      IPINFO_TOKEN = 'YOUR_IPINFO_TOKEN'
      SECRET_KEY = os.environ.get('SECRET_KEY') or 'any_key'```

7. Run the Flask app:

   python app.py

8. Open your browser and go to:

   http://127.0.0.1:5000
