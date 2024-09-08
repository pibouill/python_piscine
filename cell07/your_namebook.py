#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    your_namebook.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.c      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/05 13:55:09 by pibouill          #+#    #+#              #
#    Updated: 2024/09/05 13:55:09 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	array_of_names(persons):
	full_names = []
	for first_name, last_name in persons.items():
		full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
		full_names += [full_name]
	return full_names

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier",
"jean": "luc",
"bad": "benny"
}

print(array_of_names(persons))
