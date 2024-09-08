#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/09/03 11:15:39 by pibouill          #+#    #+#              #
#    Updated: 2024/09/03 11:15:39 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

og_array = [2, 8, 9, 48, 8, 22, -12, 2]

print("Original array:", og_array)

i = 0

new_arr = og_array

while i < len(og_array):
	new_arr[i] = og_array[i] + 2
	i += 1

print("New array:", new_arr)
