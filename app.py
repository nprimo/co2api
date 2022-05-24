# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nprimo <nprimo@student.42lisboa.com>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/24 22:46:27 by nprimo            #+#    #+#              #
#    Updated: 2022/05/24 22:46:53 by nprimo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask
from src.api_calls import get_carbon_intenisty, get_carbon_intensity_unit

app = Flask(__name__)

@app.route('/')
def index():
	text = "Electrical grid carbon intensity is currently {} {} in Portugal!".format(get_carbon_intenisty(), get_carbon_intensity_unit())
	return text