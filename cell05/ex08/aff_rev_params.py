#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_rev_params.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/03 11:50:15 by pibouill          #+#    #+#              #
#    Updated: 2024/09/03 11:50:15 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 2:
	i = len(sys.argv) - 1
	while i > 0:
		print(sys.argv[i])
		i -= 1
else:
	print("none")

