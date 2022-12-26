#import the flask module

from flask import Flask, render_template, request


app = Flask(__name__)

#make a route and render all the html templates in this route


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('city')

        #take a variable to show the json data
       
        json_object = {"coord": {"lon": 77.2167, "lat": 28.6667}, "weather": [{"id": 701, "main": "Mist", "description": "mist", "icon": "50d"}], "base": "stations", "main": {"temp": 285.2, "feels_like": 284.73, "temp_min": 285.2, "temp_max": 285.2, "pressure": 1018, "humidity": 87}, "visibility": 1200, "wind": {
            "speed": 2.57, "deg": 270}, "clouds": {"all": 1}, "dt": 1672055440, "sys": {"type": 1, "id": 9165, "country": "IN", "sunrise": 1672018912, "sunset": 1672056059}, "timezone": 19800, "id": 1273294, "name": "Delhi", "cod": 200}
       
        #read the json object
        #json_object = r.json()

        #take some attributes like temperature,humidity,pressure of this
        # this temparetuure in kelvin
        temperature = int(json_object['main']['temp']-273.15)
        humidity = int(json_object['main']['humidity'])
        pressure = int(json_object['main']['pressure'])
        wind = int(json_object['wind']['speed'])

        #atlast just pass the variables
        condition = json_object['weather'][0]['main']
        desc = json_object['weather'][0]['description']

        return render_template('home.html', temperature=temperature, pressure=pressure, humidity=humidity, city_name=city_name, condition=condition, wind=wind, desc=desc)
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
