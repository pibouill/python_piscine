#!/usr/bin/env python
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    i_got_that.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/02 14:16:18 by pibouill          #+#    #+#              #
#    Updated: 2024/09/02 14:16:18 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

str = input("What you gotta say? : ")
while 1:
	if str == "STOP":
		break
	else:
		str = input("I got that! Anything else? : ")


