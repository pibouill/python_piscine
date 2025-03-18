#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    methods_everywhere.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 11:13:43 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 11:13:43 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def shrink(str):
    print(str[:8])


def enlarge(str):
    res = str
    while len(res) < 8:
        res += 'Z'
    print(res)


if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if len(arg) == 8:
            print(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            shrink(arg)
