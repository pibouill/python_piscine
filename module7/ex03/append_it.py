#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    append_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 09:02:16 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 09:02:16 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) < 2:
    print("none")
else:
    for string in sys.argv[1:]:
        if string.endswith("ism"):
            continue
        else:
            print(string + "ism")
