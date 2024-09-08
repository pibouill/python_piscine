#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/03 11:22:36 by pibouill          #+#    #+#              #
#    Updated: 2024/09/03 11:22:36 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

og_array = [2, 8, 9, 48, 8, 22, -12, 2]

print("Original array:", og_array)

i = 0

new_array = []

while i < len(og_array):
	if og_array[i] > 5:
		new_array.append(og_array[i])
	i += 1

i = 0

while i < len(new_array):
	new_array[i] = new_array[i] + 2
	i += 1

myset = set((new_array))

print("New array:", myset)
