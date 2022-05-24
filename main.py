import requests
from dotenv import load_dotenv
import os

load_dotenv()

url_base = "https://api.co2signal.com/v1/latest"
url_country_code = "?countryCode="
# To be able to choose eventually
country_code = "PT" 
url_header = {"auth-token": os.getenv("TOKEN")}

response = requests.get(
	url_base + url_country_code + country_code,
	headers=url_header)
print(response.text)