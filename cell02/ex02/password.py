#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    password.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/02 13:47:06 by pibouill          #+#    #+#              #
#    Updated: 2024/09/02 13:47:06 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

password = "Python is awesome"

input_password = input()

if input_password == password:
	print("ACCESS GRANTED")
else:
	print("ACCESS DENIED")
