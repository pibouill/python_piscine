#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multiplication_table.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/02 14:11:55 by pibouill          #+#    #+#              #
#    Updated: 2024/09/02 14:11:55 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

number = int(input("Enter a number: "))

mult = 0

while mult < 10:
	print(mult, "x", number, "=", mult * number)
	mult += 1
