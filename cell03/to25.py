#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    to25.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/02 14:01:35 by pibouill          #+#    #+#              #
#    Updated: 2024/09/02 14:01:35 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

num = int(input("Enter a number less than 25: "))

if num >= 25:
	print("Error")
else:
	while num <= 25:
		print("Inside the loop, my variable is", num)
		num += 1
