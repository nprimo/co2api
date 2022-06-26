from cmath import nan
import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

def get_co2_data(country_code='PT'):
	url_base = "https://api.co2signal.com/v1/latest"
	url_country_code = "?countryCode=" 
	url_header = {"auth-token": os.getenv("TOKEN")}
	response = requests.get(
		url_base + url_country_code + country_code, headers=url_header)
	if (response):
		data = json.loads(response.text)
	else:
		data = nan
	return data


def get_carbon_intenisty(response):
	response_json = json.loads(response.text)
	return response_json["data"]["carbonIntensity"]


def get_carbon_intensity_unit(response):
	response_json = json.loads(response.text)
	return response_json["units"]["carbonIntensity"]


def get_datetime(response):
  response_json = json.load(response.text)
  return response_json["data"]["datetime"]
