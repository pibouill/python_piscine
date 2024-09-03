#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    upcase_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/03 11:44:14 by pibouill          #+#    #+#              #
#    Updated: 2024/09/03 11:44:14 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) > 1:
	print(sys.argv[1].upper())
else:
	print("none")
