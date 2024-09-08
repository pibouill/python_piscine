#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_all.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.c      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/05 11:57:43 by pibouill          #+#    #+#              #
#    Updated: 2024/09/05 11:57:43 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def	downcase_all(str):
	return str.lower()

if len(sys.argv) > 1:
	args = sys.argv[1:]

	for param in args:
		print(downcase_all(param))
else:
	print("none")

