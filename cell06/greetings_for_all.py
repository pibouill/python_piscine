#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    greetings_for_all.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.c      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/05 12:07:33 by pibouill          #+#    #+#              #
#    Updated: 2024/09/05 12:07:33 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	greetings(arg = None):
	if arg is None:
		print("Hello, noble stranger.")
		return
	res = isinstance(arg, str)
	if res == 1:
		print("Hello,", arg)
	else:
		print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)


