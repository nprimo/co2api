from flask import Flask
import datetime

from main import routine

app = Flask('')

@app.route('/')
def home():
    return "Hello. I am alive!"

@app.route('/update_co2_db')
def update_co2_db():
	now_dt = datetime.datetime.now()
	routine(now_dt)
	return "Updating CO2 database..."

def run():
  app.run(host='0.0.0.0',port=8080)


if __name__ == "__main__":
	run()