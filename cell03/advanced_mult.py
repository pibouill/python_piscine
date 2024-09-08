#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    advanced_mult.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/02 14:23:05 by pibouill          #+#    #+#              #
#    Updated: 2024/09/02 14:23:05 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 1:
	table_str = "Table de"
	table = -1

	while table < 10:
		mult = 0
		table += 1
		print(table_str, table, end='')
		print(": ", end='')
		count = 10

		while count >= 0:
			print(mult * table, end=' ')
			mult += 1
			count -= 1
		print("")
else:
	print("none")
