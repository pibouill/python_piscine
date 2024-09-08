#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    methods_everywhere.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.c      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/05 12:59:57 by pibouill          #+#    #+#              #
#    Updated: 2024/09/05 12:59:57 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def	shrink(str):
	print(str[:8])

def	enlarge(str):
	str_len = len(str)
	while str_len < 8:
		str = ''.join((str, 'Z'))
		str_len += 1
	print(str)

if len(sys.argv) > 1:
	params = sys.argv[1:]

	for arg in params:
		if len(arg) > 8:
			shrink(arg)
		elif len(arg) < 8:
			enlarge(arg)
		else:
			print(arg)
else:
	print("none")

