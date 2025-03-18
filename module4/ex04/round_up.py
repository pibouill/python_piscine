#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    round_up.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 13:32:56 by pibouill          #+#    #+#              #
#    Updated: 2025/03/10 13:32:56 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

try:
    number = float(input("Give me a number: "))

    if number.is_integer():
        print(int(number))
    else:
        print(int(number + 1))
except ValueError:
    print("I said, a number.")
