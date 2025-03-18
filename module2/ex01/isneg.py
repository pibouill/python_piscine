#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    isneg.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 10:42:15 by pibouill          #+#    #+#              #
#    Updated: 2025/03/10 10:42:15 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

number = int(input())

if number < 0:
    print("This number is negative.")
elif number == 0:
    print("This number is both positive and negative.")
else:
    print("This number is positive")

