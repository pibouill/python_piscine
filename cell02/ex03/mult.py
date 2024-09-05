#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    mult.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/02 13:50:56 by pibouill          #+#    #+#              #
#    Updated: 2024/09/02 13:50:56 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

print(first_number, "x", second_number, "=", first_number * second_number)

if (first_number * second_number) > 0:
	print("The result is positive.")
elif (first_number * second_number) < 0:
	print("The result is negative.")
else:
	print("The result is both positive and negative")
