#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    count_it.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/03 12:16:13 by pibouill          #+#    #+#              #
#    Updated: 2024/09/03 12:16:13 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


if len(sys.argv) > 1:
	print("parameters:", len(sys.argv) - 1)

	args = sys.argv[1:]

	for param in args:
		print(f"{param}: {len(param)}")

else:
	print("none")
