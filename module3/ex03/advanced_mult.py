#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    advanced_mult.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 11:36:09 by pibouill          #+#    #+#              #
#    Updated: 2025/03/10 11:36:09 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

mult = 0
table = 0

while table <= 10:
    print(f"Table of {table}:", end = ' ')
    mult = 0
    while mult <= 10:
        result = table * mult
        print(f"{result}", end = ' ')
        mult += 1
    print()
    table += 1



