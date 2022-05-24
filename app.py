# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    app.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: nprimo <nprimo@student.42lisboa.com>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/05/24 22:46:27 by nprimo            #+#    #+#              #
#    Updated: 2022/05/24 22:54:55 by nprimo           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, render_template
from src.api_calls import get_carbon_intenisty, get_carbon_intensity_unit

app = Flask(__name__)

@app.route('/')
def index():
	return render_template(
		'index.html',
		carbon_intensity=get_carbon_intenisty(),
		carbon_intensity_unit=get_carbon_intensity_unit())