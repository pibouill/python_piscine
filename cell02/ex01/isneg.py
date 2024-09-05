#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    isneg.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/02 12:58:51 by pibouill          #+#    #+#              #
#    Updated: 2024/09/02 12:58:51 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

number = int(input())

if number == 0:
    print("This number is both positive and negative.")
elif number < 0:
    print("This number is negative.")
else:
    print("This number is positive.")
