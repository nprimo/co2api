# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nprimo <nprimo@student.42lisboa.com>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/24 22:46:27 by nprimo            #+#    #+#              #
#    Updated: 2022/06/26 18:15:10 by nprimo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os

from src.api_calls import get_co2_data
from src.database import Database

def get_new_co2_data():
	response = get_co2_data()
	if (response):
		new_data = [
			response["countryCode"],
			response["data"]["datetime"],
			response["data"]["carbonIntensity"],
			response["units"]["carbonIntensity"],
		]
		return (new_data)
	else:
		return None

def update_co2data(new_data, co2_db):
	query = '''
			INSERT INTO {} (countryCode, datetime, carbonIntensity, unit)
			VALUES ('{}', '{}', {}, '{}')
			'''.format('co2data', *new_data)
	try:
		co2_db.queryDB(query)
		return (0)
	except:
		return None

def update_log(log_txt, log_path='./log.txt'):
	if (os.path.isfile(log_path)):
		f = open(log_path, 'a')
		f.write(log_txt)
		f.close()
	else:
		f = open(log_path, 'x')
		f.close()
		return (update_log(log_txt))

	return 

def routine(datetime):
	log_txt = ""
	co2_db = Database("co2data")
	co2_db.createDB()
	new_data = get_new_co2_data()
	if (new_data):
		if (update_co2data(new_data, co2_db) == 0):
			log_txt += "{}	Successful update!\n".format(datetime)
		else:
			log_txt += "{}	Error in update_co2data function!\n".format(datetime)
	else:
		log_txt += "{}	Error in get_new_co2_data function!\n".format(datetime)
	update_log(log_txt)
