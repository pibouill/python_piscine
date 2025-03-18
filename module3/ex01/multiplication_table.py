#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    multiplication_table.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 11:27:47 by pibouill          #+#    #+#              #
#    Updated: 2025/03/10 11:27:47 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

print("Enter a number")
number = int(input())

mult = 0

while mult <= 9:
    print("%d x %d = %d" % (mult, number, mult * number))
    mult = mult + 1
