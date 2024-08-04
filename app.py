from flask import Flask, request, render_template, make_response, redirect, url_for
import json
from function import get_weatherData, getTime

app = Flask(__name__)

# main route that will load in the home page
@app.route("/", methods=["POST", "GET"])
def home():
    
# default values when first loading the page
    infos = {
        'status': "None",
        'searched': "",
        'weather': "",
        'temperature': "",
        'humidity': "",
        'min_temp': "",
        'max_temp': "",
        'date': "",
        'time': ""
    }
    
    # using cookies to store user's log
    search_logs = request.cookies.get('search_logs')
    if search_logs:
        search_logs = json.loads(search_logs)
    else: 
        search_logs = []

    if request.method == "POST":
        city = request.form.get("city")
        zip = request.form.get("zip")
        
        data = get_weatherData(city=city, zip_code=zip)
        
        if data['cod'] == 200:
            infos['status'] = data['name']
            infos['weather'] = data['weather'][0]['description']
            infos['temperature'] = f"{data['main']['temp']}°F"
            infos['humidity'] = f"{data['main']['humidity']}%"
            infos['min_temp'] = f"{data['main']['temp_min']}°F"
            infos['max_temp'] = f"{data['main']['temp_max']}°F"
            
            # Get the current local time
            timeInfo = getTime()
            infos['date'] = timeInfo[0]
            infos['time'] = timeInfo[1]
            
            # append the searched data into our user's cookies
            search_logs.append(infos)
        else:
            # status code 404 means that the zip or city was invalid
            if data['cod'] == '404':
                data['message'] = "Invalid City or Zip"
            infos['status'] = data['message']
        
        
        response = make_response(render_template("home.html", infos=infos, logs=search_logs))
        response.set_cookie('search_logs', json.dumps(search_logs))
        
        return response
    else:
        return render_template("home.html", infos=infos, logs=search_logs)

    
# route to clear the logs 
@app.route("/clear_logs", methods = ["POST"])
def clear_logs():
    response = make_response(redirect(url_for("home")))
    response.set_cookie("search_logs", "", expires = 0)
    return response


if __name__ == "__main__":
    app.run(debug=True)
