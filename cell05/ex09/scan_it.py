#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    scan_it.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/03 11:54:11 by pibouill          #+#    #+#              #
#    Updated: 2024/09/03 11:54:11 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

if len(sys.argv) > 2:

	matches = re.findall(sys.argv[1], sys.argv[2])
	if len(matches) > 0:
		print(len(matches))
	else:
		print("none")
else:
	print("none")

