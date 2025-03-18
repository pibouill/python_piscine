#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    password.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 10:56:15 by pibouill          #+#    #+#              #
#    Updated: 2025/03/10 10:56:15 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

password = "Python is awesome"

u_input = input()

print(u_input.strip("\""))
if u_input.strip("\"") == password:
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")
