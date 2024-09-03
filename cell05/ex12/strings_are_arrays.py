#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    strings_are_arrays.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/03 12:30:52 by pibouill          #+#    #+#              #
#    Updated: 2024/09/03 12:30:52 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

count = 0

if len(sys.argv) == 2:
	for z in sys.argv[1]:
		if z == 'z':
			print("z", end='')
			count += 1
	if count == 0:
		print("none")
	else:
		print()
else:
	print("none")
