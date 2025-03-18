#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    downcase_all.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 10:58:47 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 10:58:47 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys


def downcase_all(str) -> str:
    return (str.lower())


if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        print(downcase_all(arg))
