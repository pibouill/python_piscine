#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    to25.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 11:15:38 by pibouill          #+#    #+#              #
#    Updated: 2025/03/10 11:15:38 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

number = int(input("Enter a number less than 25: "))

if number >= 25:
    print("Error")
else:
    i = number
    while i <= 25:
        print("Inside the loop, my variable is %d" % (i))
        i = i + 1
