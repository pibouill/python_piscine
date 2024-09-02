#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    float.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/02 16:19:58 by pibouill          #+#    #+#              #
#    Updated: 2024/09/02 16:19:58 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

num = float(input("Give me a number: "))

if num.is_integer():
	print("This number is an integer.")
else:
	print("This number is a decimal.")
