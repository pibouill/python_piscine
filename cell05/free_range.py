#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    free_range.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/03 13:03:40 by pibouill          #+#    #+#              #
#    Updated: 2024/09/03 13:03:40 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) == 3:
	arr = list(range(int(sys.argv[1]), int(sys.argv[2]) + 1))
	print(arr)
else:
	print("none")
