#!/bin/python3
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    upcase_it.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pibouill <pibouill@student.42prague.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/11 07:53:52 by pibouill          #+#    #+#              #
#    Updated: 2025/03/11 07:53:52 by pibouill         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].upper())
