from app import app
from flask import render_template, request
from app.models import model

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/nolikethis')
def secret():
    return render_template('nolikethis.html')
    
@app.route('/sendHoroscope', methods = ['GET','POST'])
def horoscope():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        userdata = dict(request.form)
        month=userdata['month']
        day=userdata['day']
        sign=model.getSign(month,day)
        horoscope=model.getHoroscope(sign)
        media=model.getMedia(sign)
        print(userdata)
        return render_template('theresults.html',month=month.upper(),day=day,sign=sign,horoscope=horoscope,media=media)