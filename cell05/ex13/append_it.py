#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    append_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/03 12:39:58 by pibouill          #+#    #+#              #
#    Updated: 2024/09/03 12:39:58 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

if len(sys.argv) > 1:
	args = sys.argv[1:]
	for arg in args:
		if not arg.endswith("ism"):
			print(f"{arg}ism")
else:
	print("none")
