from flask import Flask, request, url_for, session, redirect, render_template
from weather import get_weatherData

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def home():
    infos = {
            'weather': "",
            'temperature': "",
            'humidity': "",
            'min_temp': "",
            'max_temp': "",
            
        } 
    if request.method == "POST":
        city = request.form.get("city")
        zip = request.form.get("zip")
        
        if city:
            datas = get_weatherData(city)
            print(datas)
        
        infos['weather'] = datas['weather'][0]['description']
        infos['temperature'] = f"{datas['main']['temp']}°F"
        infos['humidity'] = f"{datas['main']['humidity']}%"
        infos['min_temp'] = f"{datas['main']['temp_min']}°F"
        infos['max_temp'] = f"{datas['main']['temp_max']}°F"
        
        return render_template("home.html", location = city, infos = infos)

    else:
        return render_template("home.html", location = "None", infos = infos)












if __name__ == "__main__":
    app.run(debug=True)