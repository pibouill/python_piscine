#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    persons_of_interest.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.c      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/05 17:58:59 by pibouill          #+#    #+#              #
#    Updated: 2024/09/05 17:58:59 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def	famous_births(dic):

	sorted_scientists = sorted(women_scientists.items(), key=lambda item: item[1]["date_of_birth"])
	for key, value in sorted_scientists:
		print(value["name"], "is a great scientist born in", value["date_of_birth"] + '.')


famous_births(women_scientists)
