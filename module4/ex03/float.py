#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    float.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 13:11:44 by pibouill          #+#    #+#              #
#    Updated: 2025/03/10 13:11:44 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:
    u_input = input("Give me a number: ")
    number =  float(u_input)
    if number.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    print("I said, a number.")
