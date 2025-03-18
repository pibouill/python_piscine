#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    string_are_arrays.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 08:32:04 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 08:32:04 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) < 2:
    print("none")
else:
    z_ret = []
    for char in sys.argv[1]:
        if char == 'z':
            z_ret.append('z')
    if len(z_ret) == 0:
        print("none")
    else:
        print(''.join(z_ret))
