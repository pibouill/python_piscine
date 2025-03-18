#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    free_range.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 09:08:58 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 09:08:58 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) < 3:
    print("none")
else:
    try:
        start = int(sys.argv[1])
        end = int(sys.argv[2])
        if start > end:
            arr = list(range(start, end - 1, -1))
        else:
            arr = list(range(start, end + 1, 1))
        print(arr)
    except ValueError:
        print("input error")
