from flask import Flask, render_template,jsonify
from formTestApi import start_test
from page_speed import get_load_time

app = Flask(__name__)
app.secret_key = 'this is automationx'


@app.route('/formautomate/',methods=['GET','POST'])
def form_automate():
    t1="shivanshu"
    p1="mishra"
    url = 'https://docs.google.com/forms/d/e/1FAIpQLSeI8_vYyaJgM7SJM4Y9AWfLq-tglWZh6yt7bEXEOJr_L-hV1A/viewform?formkey=dGx0b1ZrTnoyZDgtYXItMWVBdVlQQWc6MQ'
    start_test(url,t1,p1)
    return jsonify({'status':"success"})

@app.route('/getspeed/',methods=['GET','POST'])
def speed_test():
    t1="shivanshu"
    p1="mishra"
    url = 'https://www.facebook.com/'
    get_load_time(url,t1,p1)
    return jsonify({'status':"success"})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)
 