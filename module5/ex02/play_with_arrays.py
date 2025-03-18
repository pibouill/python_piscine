#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    play_with_arrays.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 13:49:29 by pibouill          #+#    #+#              #
#    Updated: 2025/03/10 13:49:29 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

og_array = [2, -2, 11111, 42, 43, -432, 342, 4]
new_arr = []

for num in og_array:
    if num > 5:
        new_arr.append(num + 2)

print("Original array:", og_array)
print("New array:", new_arr)
