from flask import Flask, render_template, redirect, make_response, request
from flask_bootstrap import Bootstrap
import requests
from form import CityForm
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

@app.route('/', defaults={'city_by_search': None}, methods=['GET','POST'])
@app.route('/home', defaults={'city_by_search': None}, methods=['GET','POST'])
@app.route('/home/index', defaults={'city_by_search': None}, methods=['GET','POST'])
@app.route('/weather_at/<city_by_search>', methods=['GET','POST'])
def index(city_by_search):
    form = CityForm()
    
    if city_by_search:
        ip_city = city_by_search
    else:
        ipinfo_data = requests.get(f'https://ipinfo.io/?token={app.config["IPINFO_TOKEN"]}').json()
        ip_city = ipinfo_data['city']

    if request.cookies.get('user_city'):
        ip_city = request.cookies.get('user_city')

    if form.validate_on_submit():
        ip_city = form.search.data
        res = make_response(redirect(f'/weather_at/{ip_city}'))
        res.set_cookie('user_city', ip_city, max_age = 60*60*24*365)
        return res

    owm_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={ip_city}&appid={app.config["OWM_TOKEN"]}&units=metric&lang=eng').json()
    temperature = owm_data['main']['temp']
    weather = owm_data['weather'][0]['description']
    name = owm_data['name']
    wind = owm_data['wind']['speed']
    icon = owm_data['weather'][0]['icon']

    res = make_response(render_template('index.html',
                                        ip_city = ip_city,
                                        temperature = temperature,
                                        weather = weather,
                                        name = name,
                                        wind = wind,
                                        icon = icon,
                                        form = form))
    if not request.cookies.get('user_city'):
        res.set_cookie('user_city', ip_city, max_age = 60*60*24*365)
    return res

@app.route('/what_city', methods=['GET','POST'])
def what_city():
    form = CityForm()

    if form.validate_on_submit():
        ip_city = form.search.data
        res = make_response(redirect(f'/weather_at/{ip_city}'))
        res.set_cookie('user_city', ip_city, max_age = 60*60*24*365)
        return res
    
    return render_template('city_form.html', form=form)

@app.route('/delete_cookie')
def delete_cookie():
    res = make_response(redirect('/'))
    res.set_cookie('user_city', '', max_age=0)
    return res

if __name__ == '__main__':
   app.run(host='127.0.0.1', port=5000, debug=True)