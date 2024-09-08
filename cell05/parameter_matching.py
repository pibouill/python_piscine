#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    parameter_matching.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/03 12:10:55 by pibouill          #+#    #+#              #
#    Updated: 2024/09/03 12:10:55 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 2:
	param = input("What was the parameter? ")
	if param == sys.argv[1]:
		print("Good job!")
	else:
		print("Nope, sorry...")
else:
	print("none")
