#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    family_affairs.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.c      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/05 15:20:09 by pibouill          #+#    #+#              #
#    Updated: 2024/09/05 15:20:09 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def	find_the_redheads(family):
	red_heads = []
	for name, color in family.items():
		if color == 'red':
			red_heads += [name]
	return red_heads

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red",
}

print(find_the_redheads(dupont_family))
