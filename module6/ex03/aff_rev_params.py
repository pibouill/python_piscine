#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    aff_rev_params.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 08:05:38 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 08:05:38 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) < 3:
    print("none")
else:
    i = len(sys.argv) - 1
    while i >= 1:
        print(sys.argv[i])
        i -= 1

    # python way
    # for arg in reversed(sys.argv[1:]):
    #     print(arg)
