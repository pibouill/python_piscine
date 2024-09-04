#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    hello_all.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/04 11:22:54 by pibouill          #+#    #+#              #
#    Updated: 2024/09/04 11:22:54 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	hello():
	print("Hello Everyone!")

class	c_greeting:
	my_method = hello

hello()
c_greeting.hello()
