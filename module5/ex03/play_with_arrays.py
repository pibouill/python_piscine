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

# sets are unordered by nature
og_array = [2, 8, 9, 48, 8, 22, -12, 2, 42, 24, 22]
new_arr = set()

print(og_array)

for num in og_array:
    if num > 5:
        new_arr.add(num + 2)
new_set = set(new_arr)
print(new_set)
