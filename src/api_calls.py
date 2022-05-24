import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

url_base = "https://api.co2signal.com/v1/latest"
url_country_code = "?countryCode="
# To be able to choose eventually
country_code = "PT" 
url_header = {"auth-token": os.getenv("TOKEN")}
response = requests.get(
		url_base + url_country_code + country_code,
		headers=url_header)

def get_carbon_intenisty():
	response_json = json.loads(response.text)
	return response_json["data"]["carbonIntensity"]

def get_carbon_intensity_unit():
	response_json = json.loads(response.text)
	return response_json["units"]["carbonIntensity"]
